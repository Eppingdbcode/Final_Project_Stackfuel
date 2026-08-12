# FINAL PROJECT — GLP-1 & PUBLIC HEALTH IN GERMANY

## Current operational handoff — 2026-08-12

- **Official root:** `C:\Users\eppin\Desktop\Final_Project_Stackfuel`.
- **GitHub:** `https://github.com/Eppingdbcode/Final_Project_Stackfuel.git`.
- **Consolidation branch:** `integration/project-consolidation`; `main` was not modified or merged.
- **Temporary backup:** `C:\Users\eppin\GLP1_Germany_Final_Project` remains intact and must not be edited or removed until a later explicit decision.
- **Environment:** UV is the sole active manager; `.python-version`, `pyproject.toml`, `uv.lock` and the UV-managed `.venv` are the sources of truth. The former `environment.yml` remains only in the backup and was not incorporated.
- **Local RAW:** copied byte for byte to the official root only after ignore protection. RAW is not published. `01_raw_data/raw_data_manifest.csv` and `01_raw_data/raw_data_checksums.sha256` are the only public integrity records besides the README.
- **WIdO duplication:** both 556-byte files remain preserved and share SHA-256 `05D1667BFE2197C649F3FC7C37A2A2835FEDEE063A88C3C328DF8CEE4E66CCA5`; the origin of the second path remains `not confirmed` and neither file may be published.
- **Operational memory:** `AGENTS.md`, `PROJECT_STATUS.md`, `00_project/TASKS.md`, `00_project/decision_log.md` and this handoff. Operational detail is in `00_project/WORKFLOW.md`.
- **Last completed task:** F0.11, definitive consolidation and continuity-system deployment.
- **Current substantive state:** F2.2 remains `IN PROGRESS` with partial WIdO acquisition. F2.3–F2.6 and F6.2 have not started.
- **Blocking decisions:** define the systematic WIdO year/substance scope and the approved canonical storage strategy without altering existing RAW; WIdO redistribution remains unconfirmed.
- **Single next eligible task:** resolve and complete the acquisition scope for F2.2; do not start another acquisition automatically.

### Start a new chat

Follow `New chat startup protocol` in `AGENTS.md`: read the five central documents, confirm Git root/branch/status and summarize current state, last task, blockers, the single next task and Definition of Done before editing.

### Environment validation

```powershell
uv sync
uv run python -c "import pandas, matplotlib, seaborn, openpyxl"
uv run pytest
```

`no tests collected` means no tests exist; it is not evidence that analytical code works. Core limitations remain: distinct population universes cannot be conflated; WIdO has no indication or total-market coverage; GEDA is self-reported; Destatis disease costs are not direct GKV/avoidable costs; trial efficacy is not German real-world effectiveness; projections and assumptions require explicit labels and sensitivity analysis.

Validation on 2026-08-12 completed `uv sync`; imports succeeded for pandas 3.0.5, matplotlib 3.11.1, seaborn 0.13.2 and openpyxl 3.1.5. Pytest 9.1.1 collected no tests (`exit 5`), so analytical validation remains pending until code/tests exist.

## Historical project brief



## 1. Project idea



Develop a Data Analytics project investigating the potential public-health and economic impact of broader access to GLP-1/GIP-based obesity treatments within the German statutory healthcare system (GKV).



The project should focus primarily on Germany.



The objective is NOT to prove beforehand that GLP-1 reimbursement saves money. The analysis must test whether broader reimbursement could be economically justified and identify under which population/risk scenarios this might occur.



---



## 2. Main research question



**Could reimbursing GLP-1-based obesity treatment reduce the long-term financial burden of obesity-related Type 2 Diabetes on Germany's statutory healthcare system (GKV)?**



Possible secondary question:



**For which risk groups could GLP-1 reimbursement become economically viable?**



Examples:



* BMI ≥ 30

* BMI ≥ 35

* obesity + prediabetes

* obesity + cardiovascular risk

* different age groups



---



## 3. Analytical principle



The project must clearly separate:



### OBSERVED DATA



What has actually happened in Germany:



* GLP-1 prescriptions

* pharmaceutical expenditure

* diabetes incidence

* diabetes prevalence

* obesity prevalence

* healthcare costs

* demographic development



from:



### MODELLED SCENARIOS



What could happen if Germany changed reimbursement policy:



* eligible population

* adoption rate

* treatment cost

* treatment persistence

* expected risk reduction

* avoided Type 2 Diabetes cases

* avoided healthcare costs

* net cost / saving

* break-even point



No causal conclusion should be made solely from correlations in observational data.



---



# 4. DATASET 1 — German GKV Pharmaceutical Market



## Source



WIdO — Wissenschaftliches Institut der AOK

GKV-Arzneimittelindex / PharMaAnalyst



Official/free source:

https://www.wido.de/publikationen-produkte/analytik/pharmaanalyst/



## Population



German statutory health insurance — GKV.



Underlying prescription data represents the overwhelming majority of outpatient prescriptions billed to statutory health insurers.



The current PharMaAnalyst selection of approximately 3,000 relevant pharmaceuticals covers approximately 98% of annual GKV prescriptions according to WIdO methodology.



More than 70 million people are insured through GKV.



## Period



Historical data available from approximately 2016 onward.



## Variables of interest



Potential variables include:



* year

* active ingredient / Wirkstoff

* ATC code

* prescriptions / Verordnungen

* packages

* Defined Daily Doses (DDD)

* net pharmaceutical expenditure / Nettokosten

* cost per prescription

* cost per DDD



## GLP-1/GIP substances to investigate



Do NOT restrict the analysis to Ozempic or Mounjaro.



Search by active ingredient whenever possible.



Main substances:



### Semaglutide



Brands include:



* Ozempic

* Wegovy

* Rybelsus



### Tirzepatide



Brand:



* Mounjaro



### Liraglutide



Brands include:



* Victoza

* Saxenda



### Dulaglutide



* Trulicity



### Exenatide



* Byetta

* Bydureon



### Lixisenatide



* Lyxumia



Other relevant GLP-1 drugs should be added if identified.



## Potential analysis



Build a longitudinal dataframe such as:



year | active_ingredient | prescriptions | DDD | net_cost



Analyse:



* evolution of GLP-1 prescriptions

* evolution of GKV GLP-1 expenditure

* market share by molecule

* transition from older GLP-1s to semaglutide/tirzepatide

* cost per DDD

* cost per prescription

* growth rates



---



# 5. IMPORTANT LIMITATION — PRIVATE / SELF-PAY MARKET



PharMaAnalyst represents prescriptions billed to GKV.



It does NOT represent the entire German consumption of obesity drugs.



This is particularly important because obesity drugs such as Wegovy are generally excluded from GKV reimbursement as Lifestyle-Arzneimittel, while GLP-1 medications prescribed for covered diabetes indications can be reimbursed.



Therefore:



GKV DATA ≠ TOTAL GERMAN GLP-1 CONSUMPTION.



---



# 6. PRIVATE / SELBSTZAHLER MARKET



## IQVIA



IQVIA Germany possesses detailed German pharmaceutical market and prescription data.



The complete database is commercial and should NOT be required for this project.



However, IQVIA publishes free reports, articles and market analyses that can be used as secondary sources.



Public IQVIA information indicates that approximately 100,000 German patients were privately using anti-obesity medications around the end of 2024.



IQVIA has also published public analyses showing development of the self-pay market for products such as:



* Wegovy

* Mounjaro



across Germany and other European countries.



Use these publications as contextual/calibration data rather than as the primary dataset.



Important:



Do NOT interpret all private anti-obesity medication users as "people using Ozempic for weight loss."



Only make claims supported by the original source definition.



---



# 7. DATASET 2 — Diabetes in Germany



## Source



Robert Koch-Institut — RKI

Diabetes Surveillance Germany



https://diabsurv.rki.de/



Datasets of interest:



### Diabetes incidence



"Incidence of documented diabetes"



Potential downloadable XLSX dataset.



### Diabetes prevalence



"Prevalence of documented diabetes"



Potential downloadable XLSX dataset.



Variables may include:



* year

* age

* sex

* Bundesland

* absolute cases

* prevalence/incidence rates



A critical feasibility check is required:



Determine whether Type 2 Diabetes can be separated from other forms of diabetes.



This distinction is important because the economic model should primarily concern preventable Type 2 Diabetes.



---



# 8. DATASET 3 — Obesity / BMI



## Sources



Robert Koch-Institut:



* GEDA

* German Health Monitoring

* Scientific Use Files



Potential variables:



* BMI

* obesity

* overweight

* age

* sex

* Bundesland

* socioeconomic characteristics

* health risk factors



German obesity prevalence has increased substantially over the past two decades.



The project should establish a historical baseline before widespread modern GLP-1 adoption.



---



# 9. DATASET 4 — Disease Costs



## Source



Statistisches Bundesamt — Destatis



Krankheitskostenrechnung / GENESIS database.



Relevant ICD-10 groups include:



### Diabetes mellitus



E10–E14



### Obesity



E65–E68



Variables potentially include:



* year

* ICD-10 disease category

* total costs

* costs per inhabitant



This dataset should provide the economic burden against which GLP-1 treatment costs can be compared.



---



# 10. DATASET 5 — Population & Demographics



## Source



Destatis / GENESIS



Potential variables:



* population

* age

* sex

* Bundesland

* year



These data can be used to standardize prevalence/incidence and calculate eligible populations.



---



# 11. CLINICAL EFFECT DATA



Use high-quality clinical evidence from sources such as:



* EMA

* peer-reviewed randomized clinical trials

* systematic reviews/meta-analyses



Potential parameters:



* weight reduction

* diabetes risk reduction

* cardiovascular outcomes

* treatment discontinuation

* treatment persistence

* adverse-event discontinuation



These should be used as MODEL PARAMETERS, not mixed with observational German datasets.



---



# 12. POTENTIAL ECONOMIC MODEL



Conceptually:



GERMAN POPULATION



↓



OBESE POPULATION



↓



ELIGIBLE HIGH-RISK POPULATION



↓



GLP-1 ADOPTION RATE



↓



TREATMENT PERSISTENCE



↓



ANNUAL TREATMENT COST



↓



EXPECTED REDUCTION IN TYPE 2 DIABETES RISK



↓



AVOIDED DIABETES CASES



↓



AVOIDED HEALTHCARE COSTS



↓



NET ECONOMIC IMPACT



---



# 13. SCENARIOS



Possible adoption scenarios:



* 10%

* 25%

* 50%

* 75%



Possible time horizons:



* 5 years

* 10 years

* 20 years



Possible eligibility scenarios:



A — All patients with obesity



B — BMI ≥ 35



C — Obesity + prediabetes



D — Obesity + high cardiovascular/metabolic risk



Compare:



### Current policy



versus



### Expanded GKV reimbursement



---



# 14. KEY OUTPUT



The desired final answer is NOT predetermined.



Possible conclusions include:



### Scenario 1



GLP-1 reimbursement produces net savings.



### Scenario 2



GLP-1 reimbursement reduces diabetes but costs more than the healthcare costs avoided.



### Scenario 3



Universal reimbursement is economically inefficient, but targeted reimbursement for high-risk patients is cost-effective.



Scenario 3 may potentially be the most policy-relevant result.



---



# 15. POSSIBLE KPIs



* GLP-1 prescriptions/year

* GLP-1 DDD/year

* GKV expenditure on GLP-1

* cost/DDD

* diabetes incidence

* Type 2 Diabetes prevalence

* obesity prevalence

* annual diabetes healthcare cost

* eligible population

* treatment cost/patient/year

* estimated cases prevented

* cost per diabetes case prevented

* avoided healthcare costs

* net budget impact

* ROI

* break-even year



---



# 16. IMPORTANT METHODOLOGICAL LIMITATIONS



The project must explicitly acknowledge:



1. Correlation does not establish causality.

2. Modern GLP-1 obesity treatment is relatively recent in Germany.

3. Long-term diabetes outcomes may not yet be observable.

4. GKV data excludes much of the self-pay obesity market.

5. Private pharmaceutical microdata are generally commercial.

6. Clinical trial populations may differ from the German general population.

7. Treatment discontinuation must be incorporated.

8. Diabetes costs cannot automatically be assumed to disappear when diabetes is prevented.

9. Future costs and savings should ideally be discounted in long-term scenarios.

10. The model should include sensitivity analysis around uncertain assumptions.



---



# 17. PROJECT POSITIONING



This should NOT be presented as:



"GLP-1 drugs save Germany money."



It should be presented as:



**A data-driven investigation of whether, when and for whom expanded GLP-1 reimbursement could reduce the health and economic burden of obesity-related Type 2 Diabetes in Germany.**



---



# 18. CURRENT FEASIBILITY ASSESSMENT



Project status:



**GO**



Current assessment:



* German GKV prescription data: STRONG

* pharmaceutical expenditure: STRONG

* diabetes data: STRONG

* obesity data: STRONG

* disease-cost data: STRONG

* demographic data: STRONG

* clinical evidence: STRONG

* private/self-pay microdata: WEAK

* private/self-pay aggregate evidence: AVAILABLE

* causal inference from German observational data: LIMITED



The project must rely primarily on free/public data.



Paid IQVIA datasets are NOT required for the project.



---



# 19. NEXT STEPS



Do not begin modelling immediately.



First create a DATA FEASIBILITY MAP.



For every dataset document:



* official source

* URL

* file/API

* available years

* number of observations

* columns

* geographic granularity

* demographic granularity

* update frequency

* missing values

* limitations

* join keys

* role in the final analysis



Then:



1. Download raw datasets.

2. Preserve untouched RAW versions.

3. Inspect schemas.

4. Clean datasets separately.

5. Build analytical datasets.

6. Perform EDA.

7. Define model assumptions.

8. Build baseline scenario.

9. Build alternative reimbursement scenarios.

10. Perform sensitivity analysis.

11. Create visualizations.

12. Develop conclusions and policy recommendations.



---



# 20. WORKING PRINCIPLE



Do not force the data to support the original hypothesis.



If the evidence indicates that broad GLP-1 reimbursement would cost the GKV more than it saves, report that.



If only targeted treatment appears economically justified, identify the population where the economics change.



All assumptions must be traceable to a source or explicitly labelled as assumptions.



The final objective is a reproducible, defensible Data Analytics project using primarily official German healthcare data.



