# Destatis demographics quality report

- Source: GENESIS Flat CSV in an unchanged ZIP; UTF-8; semicolon delimiter.
- Coverage: 31 December 2021-2025, Germany, single years of age plus published total.
- Key: `reference_date + age_code`; 435 unique rows; non-negative integer persons; unit `Anzahl`. The blank GENESIS code on each published `Insgesamt` row is deterministically represented as derived code `TOTAL`.
- 2025 published total reconciles to 83,467,117 persons.
- Limitation: resident population is not GKV-insured or clinically eligible population; year-end is not annual average; Census 2022 introduces a break.
