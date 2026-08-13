# F3.1 - Acquired data inventory

Generated and validated on 2026-08-13. The machine-readable inventory is `02_processed_data/raw_inventory.csv` and is rebuilt by `src/final_project_stackfuel/pipeline.py`.

| Dataset | Acquired files | Input class | Coverage | Permitted use | Prohibited use |
|---|---:|---|---|---|---|
| WIdO PharMaAnalyst | 3 | observed administrative data | Germany, 2024 | Cross-sectional comparison of four A10BJ ingredients | 2012-2024 trend, clinical indication, total market, duplicate counting |
| RKI/GEDA | 2 | official survey estimate | Germany, 2003-2023 publications | Epidemiological context and published prevalence estimates | Clinical eligibility, measured BMI, invented microdata |
| Destatis population | 1 | official population estimate | Germany, 2021-2025 | Resident-population denominator by age | GKV or eligible population without an assumption |
| Destatis disease costs | 1 | official disease-cost estimate | Germany, 2020 and 2023 | All-payer disease-cost context | GKV or avoidable costs; isolated type 2 diabetes |
| RKI Diabetes | 0 | unavailable contextual data | not acquired | Limitation statement only | Substitute dataset or invented values |

The two 556-byte Semaglutide files share one SHA-256 and are one observation. The 786-byte WIdO group export is the sole analytical WIdO input because it contains all four confirmed ingredient rows in one consistent query.
