from __future__ import annotations

import hashlib
from pathlib import Path

import pandas as pd

from final_project_stackfuel.pipeline import (
    RAW,
    build_disease_cost,
    build_dimensions,
    build_obesity,
    build_population,
    build_scenario_framework,
    build_wido,
    write_tables,
)


def test_manifest_and_checksums_cover_exactly_eight_raw_files() -> None:
    manifest = pd.read_csv(RAW / "raw_data_manifest.csv", dtype=str)
    assert len(manifest) == 8
    assert manifest["manifest_record_id"].is_unique
    for row in manifest.itertuples():
        path = RAW.parent / row.relative_raw_path
        assert path.is_file()
        assert path.stat().st_size == int(row.file_size_bytes)
        assert hashlib.sha256(path.read_bytes()).hexdigest().upper() == row.sha256


def test_wido_uses_four_rows_from_group_export_only() -> None:
    frame = build_wido()
    assert len(frame) == 4
    assert frame["atc_code"].is_unique
    assert set(frame["atc_code"]) == {"A10BJ01", "A10BJ02", "A10BJ05", "A10BJ06"}
    assert set(frame["year"]) == {2024}
    assert frame["prescriptions_thousand"].sum() == 2674.0
    assert round(frame["net_cost_thousand_eur"].sum(), 1) == 582169.1


def test_population_schema_keys_units_and_coverage() -> None:
    frame = build_population()
    assert set(frame["year"]) == {2021, 2022, 2023, 2024, 2025}
    assert set(frame["unit"]) == {"Anzahl"}
    assert not frame.duplicated(["reference_date", "age_code"]).any()
    assert not frame["age_code"].isna().any()
    assert set(frame.loc[frame["age_label"] == "Insgesamt", "age_code"]) == {"TOTAL"}
    assert set(frame.loc[frame["year"] == 2021, "series_basis"]) == {"Census 2011 basis"}
    assert set(frame.loc[frame["year"] >= 2022, "series_basis"]) == {"Census 2022 basis"}
    assert frame["population_persons"].ge(0).all()


def test_disease_cost_scope_and_coverage() -> None:
    frame = build_disease_cost()
    assert len(frame) == 8
    assert set(frame["year"]) == {2020, 2023}
    assert set(frame["diagnosis_code"]) == {"E10-E14", "E65-E68"}
    assert set(frame["payer_scope"]) == {"all payers"}
    assert not frame.duplicated(["year", "diagnosis_code", "metric_code"]).any()


def test_obesity_estimates_have_valid_intervals() -> None:
    frame = build_obesity()
    assert len(frame) == 9
    assert (frame["ci95_lower_pct"] <= frame["estimate_pct"]).all()
    assert (frame["estimate_pct"] <= frame["ci95_upper_pct"]).all()
    assert frame.loc[frame.date_key == "2023", "estimate_pct"].iloc[0] == 19.7


def test_scenarios_are_not_calculated_without_parameters() -> None:
    frame = build_scenario_framework()
    status = frame.set_index("parameter")["status"]
    assert status["net_budget_impact"] == "not_calculated"
    assert status["weight_change_effect"] == "available_with_limitations"
    blockers = frame.loc[frame["blocks_calculation"], "parameter"]
    assert {"clinical_eligibility_share", "annual_treatment_cost", "avoidable_cost_fraction"}.issubset(set(blockers))


def test_complete_pipeline_outputs(tmp_path: Path, monkeypatch) -> None:
    import final_project_stackfuel.pipeline as pipeline

    monkeypatch.setattr(pipeline, "PROCESSED", tmp_path / "processed")
    monkeypatch.setattr(pipeline, "OUTPUT", tmp_path / "outputs")
    tables = write_tables()
    assert len(tables["fact_wido_observed"]) == 4
    assert (tmp_path / "outputs/fact_wido_observed.csv").is_file()
    assert (tmp_path / "outputs/control_totals.csv").is_file()
    assert (tmp_path / "outputs/validation_summary.json").is_file()
    dictionary = tables["data_dictionary"]
    assert {"is_key", "table_key", "table_granularity", "table_denominator"}.issubset(dictionary.columns)
    assert dictionary.groupby("table")["table_key"].nunique().eq(1).all()
    assert {"control_totals", "scenario_framework"}.issubset(set(dictionary["table"]))
    controls = tables["control_totals"]
    assert len(controls) == 8
    assert set(controls["status"]) == {"pass"}
    assert (controls["actual_value"] - controls["expected_value"]).abs().le(controls["tolerance"]).all()
    facts = [tables[name] for name in ["fact_wido_observed", "fact_population_observed", "fact_obesity_observed", "fact_disease_cost_observed"]]
    dim_date, dim_substance = build_dimensions(facts)
    assert dim_date["date_key"].is_unique
    assert dim_substance["atc_code"].is_unique
