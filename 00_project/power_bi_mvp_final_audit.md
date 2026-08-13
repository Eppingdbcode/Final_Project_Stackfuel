# Power BI MVP final technical and analytical audit

Audit date: 2026-08-13. Branch: `analysis/powerbi-mvp`. Baseline audited: `50b792b823a411bc5bba43664166424813154487` plus the corrections documented below.

## Conclusion

The package contains populated, reproducibly generated observed-data tables. It is ready for a descriptive Power BI build with limitations. It is not ready for economic scenario analysis. F6.2 remains `TODO / DEFERRED`; no clinical parameter, avoided cost, break-even value or net budget impact was selected or calculated.

## Deliverable inventory introduced on the branch

- `src/`: `final_project_stackfuel/pipeline.py`; modified package entry point `final_project_stackfuel/__init__.py`.
- `tests/`: `test_pipeline.py` with seven tests.
- `02_processed_data/`: `raw_inventory.csv`; modified `README.md`.
- `03_notebooks/`: no files introduced. Notebooks were not needed because reusable logic is in `src/` and the descriptive findings are documented.
- `04_outputs/tables/`: `dim_date.csv`, `dim_substance.csv`, four populated observed facts, `raw_inventory.csv`, `data_dictionary.csv`, `control_totals.csv`, `scenario_framework.csv`, `validation_summary.json`; modified `README.md`.
- `04_outputs/reports/`: `observed_data_eda.md`.
- `04_outputs/power_bi/`: `README.md`, `measures.dax`, `model_relationships.csv`, `validation_checklist.md`.
- Central/quality documentation: `data_inventory.md`, `data_dictionary.md`, `data_quality_summary.md`, `processing_rules.md`, `processed_data_validation.md`, six reports under `00_project/quality/`, D-024 in `decision_log.md`, and updates to `TASKS.md`, `project_handoff.md` and `PROJECT_STATUS.md`.

## Data-file audit

| File | Format | Rows x columns | Bytes | Content and purpose | Source / input class |
|---|---|---:|---:|---|---|
| `dim_date.csv` | CSV UTF-8 BOM | 13 x 4 | 339 | Derived, populated date/period dimension | Project-derived metadata |
| `dim_substance.csv` | CSV UTF-8 BOM | 4 x 5 | 315 | Derived, populated ATC dimension | WIdO / derived metadata |
| `fact_wido_observed.csv` | CSV UTF-8 BOM | 4 x 14 | 997 | Real processed 2024 observations | WIdO / observed administrative data |
| `fact_population_observed.csv` | CSV UTF-8 BOM | 435 x 11 | 67,279 | Real processed population values | Destatis 12411-0005 / official population estimate |
| `fact_obesity_observed.csv` | CSV UTF-8 BOM | 9 x 15 | 2,471 | Quantitative official estimates transcribed from the acquired PDF | RKI Table 2 / official survey estimate |
| `fact_disease_cost_observed.csv` | CSV UTF-8 BOM | 8 x 14 | 1,659 | Real processed cost estimates | Destatis 23631-0001 / official disease-cost estimate |
| `raw_inventory.csv` | CSV UTF-8 BOM | 7 x 17 | 5,085 | Metadata only; one row per local RAW path | Phase 2 manifest / mixed input classes |
| `data_dictionary.csv` | CSV UTF-8 BOM | 80 x 13 | 24,328 | Documentation metadata, including key, granularity and denominator | Project-derived from delivered schemas |
| `control_totals.csv` | CSV UTF-8 BOM | 8 x 8 | 959 | Reproducible expected-versus-actual controls | Sources named per control / derived validation |
| `scenario_framework.csv` | CSV UTF-8 BOM | 8 x 5 | 904 | Status/documentation only; not scenario results | Mixed framework classes; unavailable parameters explicit |
| `validation_summary.json` | JSON | 1 object | 908 | Machine-readable validation summary; not a Power BI fact | Project-derived validation |

Schemas are recorded completely in `data_dictionary.csv`. No CSV is empty, header-only or a one-row placeholder; no column is entirely null. `scenario_framework.csv` is intentionally a populated gap/status register, not a parameter or results table. The only `pending_verification` values are observational-unit metadata inherited from the two duplicate WIdO manifest records. `unavailable` and `not_calculated` occur only in the scenario framework as safeguards.

Tables proposed but not generated because evidence is unavailable: `scenario_parameters`, `scenario_results`, `scenario_validation`, RKI Diabetes fact and a `.pbix`. These must not be represented as available.

## WIdO 2024

The sole analytical input is the aggregated A10BJ 2024 export. The two byte-identical Semaglutide-only RAW paths are retained in the inventory but never read by `build_wido()`. There is no double counting, no 2012-2023 observation and no permissible WIdO trend chart.

| ATC | Ingredient | Prescriptions (thousand) | DDD (thousand) | Net cost (thousand EUR) | EUR/prescription | EUR/DDD |
|---|---|---:|---:|---:|---:|---:|
| A10BJ01 | Exenatide | 30.3 | 2,086.4 | 8,694.0 | 287.31 | 4.17 |
| A10BJ02 | Liraglutide | 155.9 | 10,419.2 | 56,385.0 | 361.69 | 5.41 |
| A10BJ05 | Dulaglutide | 1,082.9 | 136,078.7 | 244,226.9 | 225.54 | 1.79 |
| A10BJ06 | Semaglutide | 1,404.9 | 129,352.2 | 272,863.2 | 194.22 | 2.11 |

Additive controls: 2,674.0 thousand prescriptions; 277,936.5 thousand DDD; EUR 582,169.1 thousand net cost. Unit-cost ratios are not summed.

## Population

There are 87 rows per year for 2021-2025: `unter 1 Jahr`, single ages 1-84, `85 Jahre und mehr`, and the published `Insgesamt` row. Unit is persons. Disaggregated values range from 448,421 to 3,193,699; including the national total, the maximum is 83,577,140. Published totals are 83,237,124 (2021), 83,118,501 (2022), 83,456,045 (2023), 83,577,140 (2024), and 83,467,117 (2025).

The GENESIS blank code on `Insgesamt` is deterministically represented as derived `TOTAL`; no field is missing after processing. Summing `TOTAL` together with age rows would double count. The DAX population measure filters to `Insgesamt`. These are year-end resident-population counts, not GKV population.

## Disease costs

Eight rows cover 2020 and 2023, ICD groups E10-E14 and E65-E68, with `Mill. EUR` national totals and `EUR` per resident. Monetary totals range from EUR 977 million to EUR 9,685 million; per-resident values range from EUR 10 to EUR 120. There are no missing values.

E10-E14 and E65-E68 are separate selected groupings; no parent and child ICD categories are mixed. Metrics with different units must never be summed. E10-E14 is not isolated type 2 diabetes. All values cover all payers and are contextual disease costs, not avoidable GKV savings.

## RKI/GEDA obesity

Nine quantitative values were extracted from `Adipositas — Gesamt`, Table 2 on PDF page 6 of `JHealthMonit_2025_01_Adipositas_Rauchen.pdf`, DOI `10.25646/12990`. They are weighted, directly age-standardized prevalence estimates for adults aged 18+ in Germany, based on self-reported height and weight: 12.2% (95% CI 11.5-12.9) in 2003/2004; 13.7% (12.5-15.0) in 2006; 15.9% (15.1-16.6) in 2009; 15.7% (15.0-16.4) in 2010; 16.3% (15.5-17.1) in 2012; 18.0% (17.3-18.8) in 2014/2015; 18.8% (18.0-19.6) in 2019/2020; 18.8% (18.1-19.6) in 2022; and 19.7% (18.6-21.0) in 2023.

This series is epidemiological context, not measured BMI, clinical eligibility, causal evidence or a GKV denominator. Survey and mode differences remain relevant.

## Model, DAX and import decision

Relationships are valid one-to-many, single-direction links from unique `dim_date[date_key]` to all four facts and from unique `dim_substance[atc_code]` to WIdO. Facts are never joined directly; there is no many-to-many relationship. `raw_inventory`, `data_dictionary`, `control_totals` and `scenario_framework` are intentionally disconnected documentation/control tables.

All DAX table and column references exist. Additive WIdO measures use `SUM`; weighted cost uses `DIVIDE`. Disease costs filter `Mill. EUR`. The audit added explicit 2025 population, 2023 obesity and 2023 E10-E14 card measures to prevent ambiguous multi-period context. The scenario status measure reads only the `not_calculated` framework status and presents no economic result.

Import the ten CSVs for the documented four-page model. Do not import `validation_summary.json`, Markdown files, DAX text as data, source PDFs/ZIPs/CSVs, or any RAW. `scenario_framework.csv` may be imported only for the `Scenario Framework / Data Gaps` page and must not be treated as scenario results.

## Corrections and validation

Corrections: replaced five null total-row age codes with derived `TOTAL`; added explicit table key, key-column flag, granularity and denominator to the dictionary; changed controls to independently specified expected and computed actual values; added the additive DDD control; made status comparison executable; hardened seven tests; corrected DAX card filter context; documented RKI page/table provenance.

Commands used:

```powershell
C:\Users\eppin\Desktop\Final_Project_Stackfuel\.venv\Scripts\python.exe --version
C:\Users\eppin\Desktop\Final_Project_Stackfuel\.venv\Scripts\python.exe -c "import pandas, matplotlib, seaborn, openpyxl"
C:\Users\eppin\Desktop\Final_Project_Stackfuel\.venv\Scripts\python.exe -m final_project_stackfuel.pipeline
C:\Users\eppin\Desktop\Final_Project_Stackfuel\.venv\Scripts\python.exe -m pytest -p no:cacheprovider --basetemp <writable-audit-temp>
```

Python 3.14.2; pandas 3.0.5; matplotlib 3.11.1; seaborn 0.13.2; openpyxl 3.1.5. Pipeline runtime measured at 0.592 seconds. Pytest collected the expected seven tests and passed all seven in 0.56 seconds on the final run, with no warnings or errors. Regeneration changed only the expected corrected generated artifacts; a second run was stable.

## Component classification

| Component | Classification | Reason |
|---|---|---|
| WIdO 2024 | READY WITH LIMITATIONS | Four real 2024 rows; cross-section only |
| Population | READY WITH LIMITATIONS | Complete acquired national table; resident, not GKV population |
| Disease costs | READY WITH LIMITATIONS | Real national estimates; all payers and mixed units |
| Obesity | READY WITH LIMITATIONS | Verified official total estimates; self-reported survey data |
| Scenarios | NOT READY | Central parameters absent; result explicitly not calculated |
| Data dictionary | READY FOR POWER BI | Complete delivered schema metadata after audit correction |
| Control totals | READY FOR POWER BI | Eight reproducible expected-versus-actual controls pass |
| DAX | READY WITH LIMITATIONS | Descriptive measures validated; scenario measure is status only |
| Power BI guide | READY FOR POWER BI | Import, model, pages, warnings and reconciliation documented |
