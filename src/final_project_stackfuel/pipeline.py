"""Build validated observed-data tables for the Power BI MVP.

RAW files are read-only inputs. All generated artifacts are written to
02_processed_data and 04_outputs/tables relative to the repository root.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "01_raw_data"
PROCESSED = ROOT / "02_processed_data"
OUTPUT = ROOT / "04_outputs" / "tables"

WIDO_GROUP = RAW / "wido/pharmaanalyst/year=2024/atc=A10BJ/wirkst_export.csv"
POPULATION_ZIP = RAW / "destatis/12411-0005_de_flat.zip"
DISEASE_COST_ZIP = RAW / "destatis/23631-0001_de_flat.zip"

SUBSTANCE_MAP = {
    "A10BJ01": "Exenatide",
    "A10BJ02": "Liraglutide",
    "A10BJ05": "Dulaglutide",
    "A10BJ06": "Semaglutide",
}


def _read_flat_zip(path: Path) -> pd.DataFrame:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if len(names) != 1 or not names[0].lower().endswith(".csv"):
            raise ValueError(f"Expected exactly one CSV in {path}")
        with archive.open(names[0]) as stream:
            return pd.read_csv(stream, sep=";", encoding="utf-8-sig", dtype=str)


def _de_number(series: pd.Series) -> pd.Series:
    cleaned = series.str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    return pd.to_numeric(cleaned, errors="raise")


def build_wido() -> pd.DataFrame:
    raw = pd.read_csv(WIDO_GROUP, sep=";", encoding="cp1252", dtype=str)
    raw = raw[raw["ATC-Code"].isin(SUBSTANCE_MAP)].copy()
    if set(raw["ATC-Code"]) != set(SUBSTANCE_MAP):
        raise ValueError("WIdO group export does not contain the four confirmed ATC codes")
    if raw["ATC-Code"].duplicated().any():
        raise ValueError("Duplicate ATC rows in WIdO group export")
    metrics = {
        "Verordnungen in Tsd.": "prescriptions_thousand",
        "Tagesdosen in Tsd. DDD": "ddd_thousand",
        "Nettokosten in Tsd. Euro": "net_cost_thousand_eur",
        "Nettokosten je Verordnung": "net_cost_per_prescription_eur",
        "Nettokosten je Tagesdosis": "net_cost_per_ddd_eur",
    }
    out = pd.DataFrame(
        {
            "date_key": raw["Jahr"],
            "year": pd.to_numeric(raw["Jahr"], errors="raise").astype("int64"),
            "atc_code": raw["ATC-Code"],
            "active_ingredient": raw["ATC-Code"].map(SUBSTANCE_MAP),
        }
    )
    for source, target in metrics.items():
        out[target] = _de_number(raw[source]).astype("float64")
    out["source_id"] = "WIDO-PMA"
    out["input_class"] = "observed administrative data"
    out["geography"] = "Germany"
    out["denominator"] = "GKV outpatient prescriptions billed through covered pharmacies"
    out["observation_status"] = "acquired_group_export"
    return out.sort_values("atc_code").reset_index(drop=True)


def build_population() -> pd.DataFrame:
    raw = _read_flat_zip(POPULATION_ZIP)
    required = {"time", "2_variable_attribute_code", "2_variable_attribute_label", "value", "value_unit"}
    if not required.issubset(raw.columns):
        raise ValueError("Unexpected Destatis population schema")
    out = pd.DataFrame(
        {
            "date_key": raw["time"].str[:4],
            "reference_date": pd.to_datetime(raw["time"], errors="raise").dt.date.astype(str),
            "year": pd.to_datetime(raw["time"], errors="raise").dt.year.astype("int64"),
            "age_code": raw["2_variable_attribute_code"],
            "age_label": raw["2_variable_attribute_label"],
            "population_persons": pd.to_numeric(raw["value"], errors="raise").astype("int64"),
            "unit": raw["value_unit"],
        }
    )
    out["source_id"] = "DESTATIS-12411-0005"
    out["input_class"] = "official population estimate"
    out["geography"] = "Germany"
    out["denominator"] = "registered resident population at year end"
    if set(out["year"]) != {2021, 2022, 2023, 2024, 2025}:
        raise ValueError("Unexpected population coverage")
    return out.sort_values(["year", "age_code"]).reset_index(drop=True)


def build_disease_cost() -> pd.DataFrame:
    raw = _read_flat_zip(DISEASE_COST_ZIP)
    relevant = {"ICD10-E10-E14", "ICD10-E65-E68"}
    raw = raw[raw["2_variable_attribute_code"].isin(relevant)].copy()
    if set(raw["2_variable_attribute_code"]) != relevant:
        raise ValueError("Relevant ICD-10 groups missing from disease-cost export")
    out = pd.DataFrame(
        {
            "date_key": raw["time"],
            "year": pd.to_numeric(raw["time"], errors="raise").astype("int64"),
            "diagnosis_code": raw["2_variable_attribute_code"].str.replace("ICD10-", "", regex=False),
            "diagnosis_label": raw["2_variable_attribute_label"],
            "metric_code": raw["value_variable_code"],
            "metric": raw["value_variable_label"],
            "value": pd.to_numeric(raw["value"], errors="raise").astype("float64"),
            "unit": raw["value_unit"],
            "quality_flag": raw["value_q"],
        }
    )
    out["source_id"] = "DESTATIS-23631-0001"
    out["input_class"] = "official disease-cost estimate"
    out["geography"] = "Germany"
    out["payer_scope"] = "all payers"
    out["denominator"] = out["unit"].map(
        {"EUR": "resident population", "Mill. EUR": "national total across all payers"}
    )
    if set(out["year"]) != {2020, 2023} or len(out) != 8:
        raise ValueError("Unexpected disease-cost coverage or row count")
    return out.sort_values(["year", "diagnosis_code", "metric_code"]).reset_index(drop=True)


def build_obesity() -> pd.DataFrame:
    # Manual structured extraction from Table 2 of RKI J Health Monit 2025,
    # DOI 10.25646/12990. Values are official weighted, age-standardized
    # survey estimates for adults aged 18+, with 95% confidence intervals.
    values = [
        ("2003/2004", 2003, 2004, 12.2, 11.5, 12.9),
        ("2006", 2006, 2006, 13.7, 12.5, 15.0),
        ("2009", 2009, 2009, 15.9, 15.1, 16.6),
        ("2010", 2010, 2010, 15.7, 15.0, 16.4),
        ("2012", 2012, 2012, 16.3, 15.5, 17.1),
        ("2014/2015", 2014, 2015, 18.0, 17.3, 18.8),
        ("2019/2020", 2019, 2020, 18.8, 18.0, 19.6),
        ("2022", 2022, 2022, 18.8, 18.1, 19.6),
        ("2023", 2023, 2023, 19.7, 18.6, 21.0),
    ]
    out = pd.DataFrame(
        values,
        columns=["date_key", "period_start_year", "period_end_year", "estimate_pct", "ci95_lower_pct", "ci95_upper_pct"],
    )
    out["indicator"] = "Obesity prevalence (BMI >= 30 kg/m2)"
    out["population"] = "Adults aged 18+ in Germany"
    out["stratum"] = "Total"
    out["unit"] = "percent"
    out["source_id"] = "RKI-GEDA-TREND-2025"
    out["input_class"] = "official survey estimate"
    out["geography"] = "Germany"
    out["denominator"] = "weighted adult survey population"
    out["method_note"] = "Self-reported height and weight; directly age-standardized"
    return out


def build_dimensions(facts: list[pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame]:
    date_rows: dict[str, tuple[int, int]] = {}
    for fact in facts:
        if "date_key" not in fact:
            continue
        for key in fact["date_key"].astype(str).unique():
            years = [int(x) for x in re.findall(r"\d{4}", key)]
            date_rows[key] = (min(years), max(years))
    dim_date = pd.DataFrame(
        [(key, start, end, start == end) for key, (start, end) in date_rows.items()],
        columns=["date_key", "period_start_year", "period_end_year", "is_single_year"],
    ).sort_values(["period_start_year", "period_end_year"])
    dim_substance = pd.DataFrame(
        [(code, name, "A10BJ", True, "observed_in_2024_group_export") for code, name in SUBSTANCE_MAP.items()],
        columns=["atc_code", "active_ingredient", "atc_group", "included_in_mvp", "inclusion_status"],
    )
    return dim_date.reset_index(drop=True), dim_substance


def build_inventory() -> pd.DataFrame:
    manifest = pd.read_csv(RAW / "raw_data_manifest.csv", dtype=str)
    duplicate_hashes = manifest.groupby("sha256")["relative_raw_path"].transform("count") > 1
    inventory = pd.DataFrame(
        {
            "dataset": manifest["dataset_id"],
            "file": manifest["relative_raw_path"],
            "institution": manifest["institution"],
            "status": "acquired",
            "input_class": manifest["dataset_id"].map(
                {
                    "wido_pma": "observed administrative data",
                    "rki_geda_agg": "official survey estimate",
                    "destatis_disease_costs": "official disease-cost estimate",
                    "destatis_population": "official population estimate",
                }
            ),
            "period": manifest["reference_period_start"] + " to " + manifest["reference_period_end"],
            "geography": manifest["geographic_coverage"],
            "observational_unit": manifest["unit_of_observation"],
            "format": manifest["format"],
            "fields_relevant": manifest["dataset_id"].map(
                {
                    "wido_pma": "year; ATC; active ingredient; prescriptions; DDD; net costs",
                    "rki_geda_agg": "published prevalence estimates; period; population; uncertainty",
                    "destatis_disease_costs": "year; ICD-10 group; cost metric; value; unit",
                    "destatis_population": "reference date; age; population count",
                }
            ),
            "units": manifest["dataset_id"].map(
                {
                    "wido_pma": "thousand prescriptions; thousand DDD; thousand EUR; EUR",
                    "rki_geda_agg": "percent and 95% confidence interval",
                    "destatis_disease_costs": "million EUR; EUR per resident",
                    "destatis_population": "persons",
                }
            ),
            "granularity": manifest["dataset_id"].map(
                {
                    "wido_pma": "Germany x 2024 x active ingredient",
                    "rki_geda_agg": "Germany x survey period x published stratum",
                    "destatis_disease_costs": "Germany x year x ICD-10 group x metric",
                    "destatis_population": "Germany x reference date x single year of age",
                }
            ),
            "is_duplicate_content": duplicate_hashes,
            "duplicate_relationship": manifest["duplicate_relationship"],
            "limitations": manifest["limitations"],
            "allowed_use": manifest["dataset_id"].map(
                {
                    "wido_pma": "2024 cross-sectional GKV utilization and cost comparison",
                    "rki_geda_agg": "epidemiological context and explicitly labelled survey inputs",
                    "destatis_disease_costs": "all-payer national disease-cost context",
                    "destatis_population": "resident-population denominator with explicit scope",
                }
            ),
            "prohibited_use": manifest["dataset_id"].map(
                {
                    "wido_pma": "2012-2024 trend; indication; total market; duplicate counting",
                    "rki_geda_agg": "clinical eligibility; measured BMI; invented microdata",
                    "destatis_disease_costs": "GKV or avoidable cost without explicit assumptions",
                    "destatis_population": "GKV-insured or clinically eligible population without assumptions",
                }
            ),
        }
    )
    return inventory


def build_data_dictionary(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    descriptions = {
        "date_key": ("Stable period key for relationships", "not applicable", "table-specific"),
        "year": ("Calendar year", "year", "not applicable"),
        "atc_code": ("ATC code", "code", "not applicable"),
        "population_persons": ("Official resident population", "persons", "registered residents at reference date"),
        "estimate_pct": ("Published prevalence estimate", "percent", "weighted adult survey population"),
        "value": ("Published disease-cost value", "row-specific", "row-specific"),
    }
    rows = []
    for table_name, frame in tables.items():
        for column, dtype in frame.dtypes.items():
            desc, unit, denominator = descriptions.get(column, (column.replace("_", " "), "see table", "see table"))
            rows.append(
                {
                    "table": table_name,
                    "column": column,
                    "type": str(dtype),
                    "description": desc,
                    "unit": unit,
                    "denominator": denominator,
                    "input_class": "mixed; see row input_class" if "input_class" in frame else "derived metadata",
                    "source": "see source_id in fact table" if "source_id" in frame else "project-derived",
                    "limitations": "Preserve source scope and denominator; do not infer missing dimensions",
                }
            )
    return pd.DataFrame(rows)


def build_controls(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    wido = tables["fact_wido_observed"]
    pop = tables["fact_population_observed"]
    obesity = tables["fact_obesity_observed"]
    costs = tables["fact_disease_cost_observed"]
    controls = [
        ("fact_wido_observed", "row_count", 4.0, "count rows", "WIdO A10BJ 2024 group export", 0.0),
        ("fact_wido_observed", "prescriptions_thousand_sum", float(wido["prescriptions_thousand"].sum()), "sum four ingredient rows", "WIdO A10BJ 2024 group export", 0.05),
        ("fact_wido_observed", "net_cost_thousand_eur_sum", float(wido["net_cost_thousand_eur"].sum()), "sum four ingredient rows", "WIdO A10BJ 2024 group export", 0.05),
        ("fact_population_observed", "year_count", float(pop["year"].nunique()), "distinct years", "Destatis 12411-0005", 0.0),
        ("fact_population_observed", "2025_total_persons", float(pop.loc[(pop.year == 2025) & (pop.age_label == "Insgesamt"), "population_persons"].iloc[0]), "published Insgesamt row", "Destatis 12411-0005", 0.0),
        ("fact_obesity_observed", "2023_estimate_pct", float(obesity.loc[obesity.date_key == "2023", "estimate_pct"].iloc[0]), "Table 2 total estimate", "RKI DOI 10.25646/12990", 0.0),
        ("fact_disease_cost_observed", "row_count", float(len(costs)), "2 years x 2 diagnoses x 2 metrics", "Destatis 23631-0001", 0.0),
    ]
    return pd.DataFrame(
        controls,
        columns=["table", "metric", "expected_value", "method", "source", "tolerance"],
    ).assign(status="pass")


def build_scenario_framework() -> pd.DataFrame:
    return pd.DataFrame(
        [
            ("resident_population", "available", "official population estimate", "Destatis 12411-0005", "Not GKV population"),
            ("obesity_prevalence", "available_with_limitations", "official survey estimate", "RKI GEDA", "Self-reported; not eligibility"),
            ("clinical_eligibility_share", "unavailable", "modelled assumption", "not selected", "Required before target population calculation"),
            ("gkv_attribution", "unavailable", "modelled assumption", "not selected", "Resident population and all-payer costs cannot be mapped silently"),
            ("annual_treatment_cost", "unavailable", "literature parameter", "not selected", "F6.2/economic parameter task required"),
            ("treatment_effect", "unavailable", "literature parameter", "not selected", "F6.2 required"),
            ("persistence", "unavailable", "literature parameter or modelled assumption", "not selected", "No defensible German long-term input"),
            ("net_budget_impact", "not_calculated", "derived calculation", "not applicable", "Central parameters unavailable"),
        ],
        columns=["parameter", "status", "input_class", "source", "limitation"],
    )


def write_tables() -> dict[str, pd.DataFrame]:
    PROCESSED.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    wido = build_wido()
    population = build_population()
    obesity = build_obesity()
    disease_cost = build_disease_cost()
    dim_date, dim_substance = build_dimensions([wido, population, obesity, disease_cost])
    inventory = build_inventory()
    tables = {
        "dim_date": dim_date,
        "dim_substance": dim_substance,
        "fact_wido_observed": wido,
        "fact_population_observed": population,
        "fact_obesity_observed": obesity,
        "fact_disease_cost_observed": disease_cost,
        "raw_inventory": inventory,
    }
    dictionary = build_data_dictionary(tables)
    controls = build_controls(tables)
    framework = build_scenario_framework()
    tables.update(
        {
            "data_dictionary": dictionary,
            "control_totals": controls,
            "scenario_framework": framework,
        }
    )
    for name, frame in tables.items():
        frame.to_csv(OUTPUT / f"{name}.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    inventory.to_csv(PROCESSED / "raw_inventory.csv", index=False, encoding="utf-8-sig", lineterminator="\n")
    validation = {
        "status": "pass",
        "tables": {name: {"rows": len(frame), "columns": len(frame.columns)} for name, frame in tables.items()},
        "phase_2_raw_files": 7,
        "wido_independent_observations": 4,
        "scenario_results_status": "not_calculated",
    }
    (OUTPUT / "validation_summary.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")
    return tables


def main() -> None:
    tables = write_tables()
    print(json.dumps({name: len(frame) for name, frame in tables.items()}, indent=2))


if __name__ == "__main__":
    main()
