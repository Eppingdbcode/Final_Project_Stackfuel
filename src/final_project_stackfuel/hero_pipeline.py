"""Reproducible processing and SQL reconciliation for GENESIS 12411-0013."""

from __future__ import annotations

import hashlib
import json
import re
import zipfile
from pathlib import Path

import duckdb
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW_ZIP = ROOT / "01_raw_data/destatis/hero/12411-0013_de_flat.zip"
PROCESSED = ROOT / "02_processed_data/hero"
ANALYTICAL = ROOT / "04_outputs/tables"
SQL_DIR = ROOT / "sql"
EXPECTED_SHA256 = "16AA18E56960526B623315F4E16F5799CFCE4964150296C5393933A48898062F"
EXPECTED_RAW_ROWS = 22_080
AGE_BINS = [-1, 17, 29, 44, 64, 74, 84, 89, 200]
AGE_LABELS = ["0-17", "18-29", "30-44", "45-64", "65-74", "75-84", "85-89", "90+"]


def validate_raw(path: Path = RAW_ZIP) -> pd.DataFrame:
    if hashlib.sha256(path.read_bytes()).hexdigest().upper() != EXPECTED_SHA256:
        raise ValueError("Unexpected SHA-256 for GENESIS 12411-0013")
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != 1 or names[0] != "12411-0013_de_flat.csv":
            raise ValueError("Expected exactly the official Flat CSV in the ZIP")
        frame = pd.read_csv(archive.open(names[0]), sep=";", dtype=str, encoding="utf-8-sig")
    if frame.shape != (EXPECTED_RAW_ROWS, 22):
        raise ValueError("Unexpected or truncated GENESIS export")
    if frame.duplicated().any():
        raise ValueError("Duplicate physical rows in GENESIS export")
    if set(frame["statistics_code"]) != {"12411"} or set(frame["value_unit"]) != {"Anzahl"}:
        raise ValueError("Unexpected statistics code or unit")
    return frame


def _age_number(label: str) -> int | None:
    if label == "Insgesamt":
        return None
    if label == "unter 1 Jahr":
        return 0
    if label == "90 Jahre und mehr":
        return 90
    match = re.match(r"(\d+)-Jährige", label)
    if not match:
        raise ValueError(f"Unknown age label: {label}")
    return int(match.group(1))


def build_processed(raw: pd.DataFrame | None = None) -> pd.DataFrame:
    raw = validate_raw() if raw is None else raw.copy()
    out = pd.DataFrame({
        "reference_date": pd.to_datetime(raw["time"], errors="raise"),
        "state_code": raw["1_variable_attribute_code"].str.zfill(2),
        "state_name": raw["1_variable_attribute_label"],
        "sex_code_official": raw["2_variable_attribute_code"].fillna("TOTAL"),
        "sex_label_official": raw["2_variable_attribute_label"],
        "age_code_official": raw["3_variable_attribute_code"].fillna("TOTAL"),
        "age_label_official": raw["3_variable_attribute_label"],
        "population_persons": pd.to_numeric(raw["value"], errors="raise").astype("int64"),
        "unit": raw["value_unit"], "quality_flag": raw["value_q"],
    })
    out["year"] = out["reference_date"].dt.year.astype("int16")
    out["sex_code"] = out["sex_label_official"].map({"männlich": "M", "weiblich": "F", "Insgesamt": "T"})
    out["sex_label"] = out["sex_code"].map({"M": "Male", "F": "Female", "T": "Total"})
    out["age_years"] = out["age_label_official"].map(_age_number)
    out["is_age_total"] = out["age_code_official"].eq("TOTAL")
    out["is_sex_total"] = out["sex_code"].eq("T")
    out["age_group"] = pd.cut(out["age_years"], bins=AGE_BINS, labels=AGE_LABELS).astype("string").fillna("Total")
    out["census_basis"] = out["year"].map({2021: "Census 2011 basis"}).fillna("Census 2022 basis")
    out["series_break_before"] = out["year"].eq(2022)
    out["source_id"] = "DESTATIS-12411-0013"
    out["input_class"] = "official population estimate"
    out["denominator"] = "registered resident population at year end"
    key = ["reference_date", "state_code", "sex_code", "age_code_official"]
    if out.duplicated(key).any() or out[key].isna().any().any():
        raise ValueError("Invalid processed key")
    if out["population_persons"].lt(0).any() or out["sex_code"].isna().any():
        raise ValueError("Invalid population or sex category")
    return out.sort_values(key).reset_index(drop=True)


def build_dimensions(processed: pd.DataFrame) -> dict[str, pd.DataFrame]:
    return {
        "dim_date_hero": processed[["reference_date", "year", "census_basis", "series_break_before"]].drop_duplicates().sort_values("reference_date"),
        "dim_geography": processed[["state_code", "state_name"]].drop_duplicates().sort_values("state_code"),
        "dim_sex": processed[["sex_code", "sex_label", "is_sex_total"]].drop_duplicates().sort_values("sex_code"),
        "dim_age": processed[["age_code_official", "age_label_official", "age_years", "age_group", "is_age_total"]].drop_duplicates().sort_values(["is_age_total", "age_years"], na_position="last"),
    }


def build_analytical(processed: pd.DataFrame) -> dict[str, pd.DataFrame]:
    detail = processed.loc[~processed["is_age_total"] & ~processed["is_sex_total"]].copy()
    fact_columns = ["reference_date", "year", "state_code", "sex_code", "age_code_official", "age_years", "age_group", "population_persons", "unit", "quality_flag", "census_basis", "series_break_before", "source_id", "input_class", "denominator"]
    fact = detail[fact_columns]
    age_summary = detail.groupby(["reference_date", "year", "state_code", "sex_code", "age_group", "census_basis"], observed=True, as_index=False)["population_persons"].sum()
    state_summary = processed.loc[processed["is_age_total"] & processed["is_sex_total"], ["reference_date", "year", "state_code", "population_persons", "census_basis"]].copy()
    state_summary["national_share_pct"] = state_summary.groupby("reference_date")["population_persons"].transform(lambda s: s / s.sum() * 100)
    state_summary["population_rank"] = state_summary.groupby("reference_date")["population_persons"].rank(method="dense", ascending=False).astype("int16")
    return {"fact_population_state_age_sex": fact, "population_age_sex_summary": age_summary, "population_state_summary": state_summary}


def build_profile(raw: pd.DataFrame, processed: pd.DataFrame, analytical: dict[str, pd.DataFrame]) -> dict:
    critical = ["reference_date", "state_code", "sex_code", "age_code_official", "population_persons"]
    return {
        "source_table": "12411-0013", "raw_rows": len(raw), "raw_columns": len(raw.columns),
        "processed_rows": len(processed), "processed_columns": len(processed.columns),
        "analytical_fact_rows": len(analytical["fact_population_state_age_sex"]),
        "power_bi_rows": sum(len(frame) for frame in analytical.values()),
        "memory_bytes": int(processed.memory_usage(deep=True).sum()),
        "full_row_duplicates": int(processed.duplicated().sum()),
        "critical_missing": {column: int(processed[column].isna().sum()) for column in critical},
        "structural_missing": {"age_years_total_rows": int(processed["age_years"].isna().sum())},
        "cardinality": {column: int(processed[column].nunique(dropna=False)) for column in processed.columns},
        "years": sorted(processed["year"].unique().astype(int).tolist()),
        "states": int(processed["state_code"].nunique()), "sex_categories": int(processed["sex_code"].nunique()),
        "age_categories": int(processed["age_code_official"].nunique()),
        "invalid_population_rows": int(processed["population_persons"].lt(0).sum()),
    }


def write_lineage() -> pd.DataFrame:
    rows = [
        ("fact_population_state_age_sex", "population_persons", "destatis_population_hero", "01_raw_data/destatis/hero/12411-0013_de_flat.zip", "value", "Parse official count as integer; exclude official total hierarchy rows from additive fact", "build_processed/build_analytical", "persons", "registered resident population at year end", "official population estimate", "Not GKV insured or clinically eligible population"),
        ("fact_population_state_age_sex", "census_basis", "destatis_population_hero", "01_raw_data/destatis/hero/12411-0013_de_flat.zip", "time", "2021=Census 2011 basis; 2022 onward=Census 2022 basis", "build_processed", "not applicable", "not applicable", "derived metadata", "Do not present 2021-2022 as continuous trend"),
        ("fact_population_state_age_sex", "age_group", "destatis_population_hero", "01_raw_data/destatis/hero/12411-0013_de_flat.zip", "3_variable_attribute_label", "Deterministic age bands from official single-year ages", "build_processed", "category", "registered resident population at year end", "derived category", "90+ is open-ended"),
        ("population_state_summary", "national_share_pct", "destatis_population_hero", "01_raw_data/destatis/hero/12411-0013_de_flat.zip", "value", "State total divided by sum of 16 state totals within date", "build_analytical", "percent", "Germany resident population at year end", "derived calculation", "Not GKV share"),
    ]
    return pd.DataFrame(rows, columns=["output_table", "output_column", "source_dataset", "source_file", "source_column", "transformation_rule", "transformation_code", "unit", "denominator", "observation_class", "limitation"])


def build_hero_dictionary(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for table, frame in tables.items():
        for column, dtype in frame.dtypes.items():
            rows.append((table, column, str(dtype), "DESTATIS-12411-0013", "official or derived population field", "registered resident population at year end", "Not GKV insured or clinically eligible population; preserve census basis"))
    return pd.DataFrame(rows, columns=["table", "column", "type", "source", "description", "denominator", "limitations"])


def run_sql(processed_path: Path, database_path: Path) -> dict[str, pd.DataFrame]:
    connection = duckdb.connect(str(database_path))
    try:
        for filename in ["schema.sql", "quality_checks.sql", "transformations.sql", "analytical_views.sql"]:
            sql = (SQL_DIR / filename).read_text(encoding="utf-8").replace("{{processed_path}}", processed_path.as_posix())
            connection.execute(sql)
        return {
            "sql_quality_checks": connection.execute("SELECT * FROM quality_checks ORDER BY check_name").df(),
            "sql_population_state_summary": connection.execute("SELECT * FROM population_state_summary_sql ORDER BY reference_date, population_rank").df(),
            "sql_population_age_sex_summary": connection.execute("SELECT * FROM population_age_sex_summary_sql ORDER BY reference_date, state_code, sex_code, age_group").df(),
        }
    finally:
        connection.close()


def reconcile(pandas_tables: dict[str, pd.DataFrame], sql_tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    checks = []
    comparisons = [
        ("population_state_summary", "sql_population_state_summary", ["reference_date", "state_code"], ["population_persons", "national_share_pct", "population_rank"]),
        ("population_age_sex_summary", "sql_population_age_sex_summary", ["reference_date", "state_code", "sex_code", "age_group"], ["population_persons"]),
    ]
    for pandas_name, sql_name, keys, metrics in comparisons:
        left, right = pandas_tables[pandas_name].copy(), sql_tables[sql_name].copy()
        left["reference_date"], right["reference_date"] = pd.to_datetime(left["reference_date"]), pd.to_datetime(right["reference_date"])
        joined = left.merge(right, on=keys, suffixes=("_pandas", "_sql"), validate="one_to_one")
        for metric in metrics:
            difference = (joined[f"{metric}_pandas"].astype(float) - joined[f"{metric}_sql"].astype(float)).abs().max()
            checks.append((pandas_name, metric, len(left), len(right), float(difference), "pass" if difference < 1e-9 else "fail"))
    return pd.DataFrame(checks, columns=["table", "metric", "pandas_rows", "sql_rows", "max_absolute_difference", "status"])


def write_hero_outputs() -> dict[str, pd.DataFrame]:
    PROCESSED.mkdir(parents=True, exist_ok=True)
    ANALYTICAL.mkdir(parents=True, exist_ok=True)
    raw = validate_raw()
    processed = build_processed(raw)
    processed_path = PROCESSED / "population_state_age_sex.parquet"
    processed.to_parquet(processed_path, index=False)
    analytical, dimensions = build_analytical(processed), build_dimensions(processed)
    for name, frame in {**analytical, **dimensions}.items():
        frame.to_csv(ANALYTICAL / f"{name}.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    (PROCESSED / "profile.json").write_text(json.dumps(build_profile(raw, processed, analytical), indent=2), encoding="utf-8")
    lineage = write_lineage()
    lineage.to_csv(ANALYTICAL / "data_lineage.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    sql_tables = run_sql(processed_path, PROCESSED / "population_hero.duckdb")
    reconciliation = reconcile(analytical, sql_tables)
    if set(reconciliation["status"]) != {"pass"} or set(sql_tables["sql_quality_checks"]["status"]) != {"pass"}:
        raise ValueError("Pandas/SQL reconciliation or SQL quality check failed")
    reconciliation.to_csv(ANALYTICAL / "population_hero_reconciliation.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    delivered = {**analytical, **dimensions}
    dictionary = build_hero_dictionary(delivered)
    dictionary.to_csv(ANALYTICAL / "population_hero_data_dictionary.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    sql_tables["sql_quality_checks"].to_csv(ANALYTICAL / "population_hero_controls.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    return {**delivered, "data_lineage": lineage, "population_hero_reconciliation": reconciliation, "population_hero_data_dictionary": dictionary, "population_hero_controls": sql_tables["sql_quality_checks"]}


def main() -> None:
    print(json.dumps({name: len(frame) for name, frame in write_hero_outputs().items()}, indent=2))


if __name__ == "__main__":
    main()
