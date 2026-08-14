# GENESIS 12411-0013 gate

- Decision: `GO`, 2026-08-14.
- Table: `Bevölkerung: Bundesländer, Stichtag, Geschlecht, Altersjahre`.
- URL: https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0013/table-toolbar
- API: POST `https://genesis.destatis.de/genesisWS/rest/2020/data/tablefile`; API token required, public UI anonymous.
- Format: ZIP containing UTF-8 semicolon-delimited Flat CSV.
- Codes: `STAG` date; `DLAND` Land; `GES` sex; `ALT103` age.
- Period: 2021-12-31 through 2025-12-31.
- Volume: 22,080 × 22; ZIP 230,420 bytes; CSV 4,919,022 bytes.
- Formula: 5 dates × 16 Länder × 3 sex categories × 92 age categories.
- API limit: direct requests above 40,000 values require a queued authenticated job or legitimate splitting; this recut is below the limit.
- License: Datenlizenz Deutschland – Namensnennung – Version 2.0 (`dl-de/by-2-0`).
- Method: population estimates; through 2021 Census 2011-based, from 2022 Census 2022-based.
- Reproducibility: public UI and token-based download script; overwrite and non-ZIP responses are rejected.
