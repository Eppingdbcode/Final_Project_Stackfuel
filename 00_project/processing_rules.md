# Processing rules for the Power BI MVP

1. Read RAW only; never extract, edit or overwrite source files in place.
2. Decode WIdO as Windows-1252 and German decimal notation explicitly.
3. Use only the 2024 A10BJ group export for WIdO facts; exclude aggregate rows and duplicate Semaglutide copies.
4. Read Destatis Flat CSV directly from ZIP, preserving original units and quality flags.
5. Filter disease costs only to approved ICD groups without reclassifying E10-E14 as type 2 diabetes.
6. Structure only the published total obesity series with exact estimates and IC95% from RKI Table 2.
7. Preserve source classes, universes, units and denominators in output columns.
8. Do not impute missing values, manufacture years or calculate scenarios without approved central parameters.
