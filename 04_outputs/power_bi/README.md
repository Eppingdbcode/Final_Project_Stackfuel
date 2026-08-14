# Power BI MVP build guide

## Hero population extension

Import the hero fact, four hero dimensions, two summaries, controls and reconciliation CSVs. Create the relationships appended to `model_relationships.csv` and add the hero measures from `measures.dax`.

Add a **Population composition** page with Bundesland ranking, age-group × sex matrix, state/year slicers and tooltips for persons, national share, census basis and observation class. Display permanently: **2021 uses Census 2011 basis; 2022 onward uses Census 2022 basis. Do not interpret the boundary as a continuous trend. Resident population is not GKV coverage or clinical eligibility.**

## Import

1. Open Power BI Desktop and choose **Get data > Text/CSV**.
2. Import the ten CSV files from `04_outputs/tables/` using UTF-8 and comma delimiter. Do not import `validation_summary.json` as a fact.
3. Set numeric types from `data_dictionary.csv`; keep `date_key`, ATC and diagnosis codes as text.
4. Create relationships exactly as listed in `model_relationships.csv`. Use one-to-many, single-direction filters from dimensions to facts.
5. Add measures from `measures.dax`. Do not create implicit sums for mixed-unit disease-cost rows.

## Page 1 - Executive Overview

- KPI cards: WIdO prescriptions (thousands), WIdO net cost (EUR), `Obesity Prevalence 2023 (%)`, and `Disease Cost - Diabetes 2023 (Million EUR)`.
- Clustered bar: active ingredient by prescriptions and net costs; title **GKV-reimbursed A10BJ utilization, 2024**.
- Line: published obesity prevalence by period with lower/upper CI in tooltip.
- Required banner: **Observed and official estimates only; no net budget impact calculated.**

## Page 2 - Observed Data

- WIdO matrix: ingredient, ATC, prescriptions, DDD, net cost, unit costs. Do not use a trend visual.
- Population cards/table: published total resident population by year; optional age slicer. Do not connect 2021 to 2022 as a continuous trend because the census basis changes.
- Disease-cost clustered columns: diagnosis and year, filtered to `Mill. EUR`; label **all payers**.
- Slicers: period, ingredient, diagnosis, metric/unit. Keep fact-specific slicers visually grouped.

## Page 3 - Scenario Framework / Data Gaps

- Table from `scenario_framework.csv`: parameter, status, input class, source, quality, permitted use, blocking flag and treatment.
- KPI: `Scenario Result Status`.
- No treated-population, savings, ROI or break-even numbers. Explain that STEP 1 efficacy/tolerability evidence is available but eligibility, GKV attribution, uptake, annual treatment cost, long-term persistence and avoided-cost mapping remain unavailable.

## Page 4 - Methods and Limitations

- Inventory table with dataset, status, input class, coverage and prohibited use.
- Control-total table filtered to status `pass`.
- Text boxes: WIdO cross-section only; self-reported GEDA; resident population not GKV; disease costs all-payer; RKI Diabetes absent.
- Source links and last refresh date.

## Visual language

- Observed administrative data: dark blue.
- Official estimates: teal.
- Derived controls: grey.
- Literature parameters: amber (STEP 1 context only; not used in an economic calculation).
- Modelled assumptions/scenarios: purple (framework only, no results).
- Use the input-class label in every tooltip and never combine universes in a single unlabeled KPI.

## Reconciliation

After refresh, compare every KPI with `control_totals.csv`. Confirm four WIdO rows, five population years, 2025 total 83,467,117, 2023 obesity prevalence 19.7%, and eight selected disease-cost rows. Confirm `expected_value` equals `actual_value` within `tolerance`; all eight control statuses must remain `pass`.
