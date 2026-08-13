# Minimum economic model and F6.2 assessment

## Intended model before evidence search

- Perspective: German statutory health insurance (GKV).
- Clinical scope: semaglutide (Wegovy) 2.4 mg subcutaneous once weekly for adult weight management, without diabetes, adjunct to reduced-calorie diet and physical activity.
- Target population: German adults meeting the EMA BMI indication; operational clinical appropriateness is not observed.
- Comparator: placebo/no semaglutide plus lifestyle intervention.
- Horizon: one year for a potential budget-impact MVP; the 68-week trial effect would require a documented time conversion and persistence assumption before use.
- Baseline: current reimbursement/utilization, which is not identified by indication in WIdO.
- Intended outputs: potential target population, treated population, gross treatment cost, avoided-cost proxy, net budget impact and break-even threshold.
- Required formula: `resident_population × adult_share × obesity_prevalence × eligibility_share × GKV_share × uptake = treated_population`; `treated_population × annual_treatment_cost = gross_treatment_cost`; avoided cost additionally requires attributable fraction, GKV fraction, applicable clinical effect, benefit realization and horizon.
- Optional parameters: subgroup risk, discontinuation, dose escalation and uncertainty distributions.
- Stop conditions: any missing eligibility, GKV attribution, uptake, annual treatment cost, persistence/realization, attributable avoided-cost or GKV cost fraction prevents net budget impact.

## Evidence selected

The [EMA Wegovy EPAR](https://www.ema.europa.eu/en/medicines/human/EPAR/wegovy) defines adult BMI eligibility boundaries but does not quantify the share operationally eligible in Germany. [STEP 1](https://doi.org/10.1056/NEJMoa2032183) provides one efficacy parameter and one tolerability parameter for the tightly matched non-diabetes scope. Exact fields and limitations are in `05_sources/studies/clinical_evidence_register.csv`. No raw article copy was downloaded or versioned.

## GO/NO-GO matrix

| Required parameter | Available? | Source | Quality | Permitted use | Blocks calculation? | Treatment |
|---|---|---|---|---|---:|---|
| Resident population | With break | Destatis 12411-0005 | High | Contextual denominator | No | Use 2025 only; do not present 2021-2025 as continuous trend |
| Adult share | Derivable | Destatis 12411-0005 | High | Component of a modelled scenario | No | Not calculated while downstream gates fail |
| Obesity prevalence | With limitations | RKI/GEDA | Moderate | Epidemiological context | No | Not clinical eligibility |
| EMA indication | Yes | EMA Wegovy EPAR | High | Define clinical scope | No | Does not quantify German eligibility |
| Eligibility share | No | None selected | None | None | Yes | Missing central parameter |
| GKV share aligned to target denominator | No | None selected | None | None | Yes | Missing central parameter |
| Uptake | No | None selected | None | None | Yes | Missing central parameter |
| Annual treatment cost per patient | No | None selected | None | None | Yes | WIdO aggregate ratios are unsuitable |
| Weight-change effect | With limitations | STEP 1 | High internal validity | Clinical context | No | Not economic benefit or German effectiveness |
| Long-term persistence | No | None selected | None | None | Yes | AE discontinuation is not persistence |
| Avoidable-cost fraction | No | None selected | None | None | Yes | Destatis costs cannot supply it |
| GKV cost fraction | No | None selected | None | None | Yes | All-payer cost cannot be attributed silently |
| Benefit realization | No | None selected | None | None | Yes | Weight change cannot be mapped directly to savings |

## Decision

**B — SCENARIO FRAMEWORK READY, RESULTS NOT CALCULATED.**

F6.2 is `DONE WITH LIMITATIONS`: the minimal regulatory, efficacy and tolerability evidence is selected and traceable. Economic scenarios are not implemented because multiple central parameters fail the prespecified stop conditions. No `scenario_parameters.csv`, `scenario_results.csv`, `scenario_validation.csv`, avoided cost, net budget impact or break-even result is created.

The original economic question remains the motivation for future work, not a quantitatively answered result in the current delivery. The deliverable is a descriptive German evidence dashboard plus a transparent scenario feasibility/gap page.

## Population series break

The acquired file confirms the five published totals. [GENESIS table 12411-0001](https://genesis.destatis.de/datenbank/online/table/12411-0001) explicitly marks results through 2021 as Census 2011-based and results from 2022 as Census 2022-based. The 2022 value of 83,118,501 is a published total, not a processing error. [Destatis documents a time-series break](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Methoden/Erlauterungen/umstellung-bevoelkerungszahlen-zensus-2022.html) from the census-base change; consequently, the dashboard must not draw a continuous 2021-2025 population trend. Use 2025 as the current contextual denominator or show the years with a visible break annotation.
