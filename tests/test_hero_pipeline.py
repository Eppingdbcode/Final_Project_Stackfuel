from __future__ import annotations

import hashlib
from pathlib import Path

import pandas as pd

import final_project_stackfuel.hero_pipeline as hero


def test_hero_raw_integrity_and_schema() -> None:
    assert hashlib.sha256(hero.RAW_ZIP.read_bytes()).hexdigest().upper() == hero.EXPECTED_SHA256
    raw = hero.validate_raw()
    assert raw.shape == (22_080, 22)
    assert not raw.duplicated().any()
    assert set(raw["time"]) == {"2021-12-31", "2022-12-31", "2023-12-31", "2024-12-31", "2025-12-31"}


def test_processed_keys_categories_missing_and_break() -> None:
    frame = hero.build_processed()
    key = ["reference_date", "state_code", "sex_code", "age_code_official"]
    assert len(frame) == 22_080
    assert not frame.duplicated(key).any()
    assert not frame[key + ["population_persons"]].isna().any().any()
    assert set(frame["sex_code"]) == {"M", "F", "T"}
    assert frame["state_code"].nunique() == 16
    assert frame["age_code_official"].nunique() == 92
    assert set(frame.loc[frame.year == 2021, "census_basis"]) == {"Census 2011 basis"}
    assert set(frame.loc[frame.year >= 2022, "census_basis"]) == {"Census 2022 basis"}
    assert frame.loc[frame.year == 2022, "series_break_before"].all()


def test_analytical_fact_has_no_artificial_hierarchy_duplication() -> None:
    tables = hero.build_analytical(hero.build_processed())
    fact = tables["fact_population_state_age_sex"]
    assert len(fact) == 14_560
    assert set(fact["sex_code"]) == {"M", "F"}
    assert "TOTAL" not in set(fact["age_code_official"])
    assert len(tables["population_state_summary"]) == 80
    assert len(tables["population_age_sex_summary"]) == 1_280


def test_pandas_sql_reconciliation(tmp_path: Path) -> None:
    processed = hero.build_processed()
    analytical = hero.build_analytical(processed)
    parquet = tmp_path / "population.parquet"
    processed.to_parquet(parquet, index=False)
    sql_tables = hero.run_sql(parquet, tmp_path / "test.duckdb")
    assert set(sql_tables["sql_quality_checks"]["status"]) == {"pass"}
    reconciliation = hero.reconcile(analytical, sql_tables)
    assert len(reconciliation) == 4
    assert set(reconciliation["status"]) == {"pass"}
    assert reconciliation["max_absolute_difference"].lt(1e-9).all()


def test_hero_pipeline_is_idempotent(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(hero, "PROCESSED", tmp_path / "processed")
    monkeypatch.setattr(hero, "ANALYTICAL", tmp_path / "analytical")
    first = hero.write_hero_outputs()
    hashes_first = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (tmp_path / "analytical").glob("*")}
    second = hero.write_hero_outputs()
    hashes_second = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (tmp_path / "analytical").glob("*")}
    assert {name: len(frame) for name, frame in first.items()} == {name: len(frame) for name, frame in second.items()}
    assert hashes_first == hashes_second
