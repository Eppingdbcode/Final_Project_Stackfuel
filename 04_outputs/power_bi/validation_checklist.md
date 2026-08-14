# Power BI validation checklist

## GENESIS hero checks

- [ ] Hero fact has 14,560 additive detail rows and no official age/sex total rows.
- [ ] Geography has 16 Länder; the fact contains M/F and 91 non-total ages.
- [ ] State totals and shares reconcile to `population_state_summary.csv`.
- [ ] All Pandas–SQL reconciliation rows pass within `1e-9`.
- [ ] Census basis is visible and 2021–2022 is not drawn as a continuous line.
- [ ] No visual labels resident population as GKV-insured, eligible or treatable.

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
