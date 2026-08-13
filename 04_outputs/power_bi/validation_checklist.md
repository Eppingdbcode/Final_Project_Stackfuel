# Power BI validation checklist

- [ ] All files imported from `04_outputs/tables/`, not RAW.
- [ ] UTF-8 characters and decimal values render correctly.
- [ ] Dimension keys are unique and relationships are one-to-many/single direction.
- [ ] WIdO shows exactly four ingredients and only 2024.
- [ ] No Semaglutide duplicate appears.
- [ ] Population is labelled resident population, not GKV.
- [ ] Disease costs are filtered by unit and labelled all payers.
- [ ] E10-E14 is labelled diabetes mellitus, not isolated type 2 diabetes.
- [ ] Obesity estimates display survey period and IC95%.
- [ ] Scenario status is `not_calculated`; no invented result is displayed.
- [ ] All eight control totals show `pass`, with `expected_value` and `actual_value` reconciled within tolerance.
- [ ] Sources, denominators, units and limitations appear in tooltips/methods.
- [ ] Refresh completes without manual edits to generated CSVs.
