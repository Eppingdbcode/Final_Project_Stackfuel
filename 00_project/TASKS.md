# Backlog oficial do projeto

## Recovery gate — GENESIS hero dataset

| ID | Status | Tarefa | Prioridade | Entregável |
|---|---|---|---|---|
| R1 | DONE | Validar e adquirir GENESIS 12411-0013 | HIGH | 22.080 registros oficiais, 2021–2025 |
| R2 | DONE | Implementar Parquet, Pandas, DuckDB/SQL, analytical, lineage e notebook | HIGH | Pipeline e outputs reconciliados |
| R3 | TODO | Montar e reconciliar a página demográfica no Power BI Desktop | HIGH | `.pbix` validado manualmente |

A próxima tarefa única é R3; nenhum cenário econômico está autorizado.

Este arquivo contém o backlog oficial e incremental do projeto de Data Analytics sobre tratamentos GLP-1/GIP, obesidade, diabetes tipo 2 e impacto econômico no sistema GKV da Alemanha.

## Legenda

- **Status:** `TODO`, `IN PROGRESS` ou `DONE`.
- **Prioridade:** `HIGH`, `MEDIUM` ou `LOW`.
- **Esforço:** `XS` (<30 min), `S` (30 min–2 h), `M` (2–6 h), `L` (1–2 dias) ou `XL` (>2 dias).
- **Aprovação:** `SIM` significa que o usuário deve aprovar o entregável antes do início da tarefa dependente ou da continuação para a próxima fase.
- Somente uma tarefa analítica principal deve permanecer como `IN PROGRESS` por vez.
- Uma dependência identificada como `nenhuma` permite execução independente.

## Fase 0 — Preparação e governança do projeto

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F0.1 | DONE | Revisar a estrutura inicial e o handoff | HIGH | S | nenhuma | Resumo de entendimento entregue ao usuário | SIM — concluída |
| F0.2 | DONE | Documentar as regras permanentes | HIGH | XS | F0.1 | `00_project/codex_instructions.md` | SIM — concluída |
| F0.3 | DONE | Criar o registro de progresso | HIGH | XS | F0.2 | `PROJECT_STATUS.md` | NÃO |
| F0.4 | DONE | Criar e revisar o backlog oficial | HIGH | S | F0.2 | `00_project/TASKS.md` | SIM — concluída |
| F0.5 | DONE | Criar o registro formal de decisões | MEDIUM | S | F0.4 | `00_project/decision_log.md` | NÃO |
| F0.6 | DONE | Definir convenções de nomes, versões e datas | MEDIUM | S | F0.4 | `00_project/data_conventions.md` | SIM — concluída |
| F0.7 | DONE | Definir o padrão do manifesto e checksums RAW | HIGH | S | F0.4 | `00_project/raw_data_manifest_template.md` | SIM — concluída |
| F0.8 | DONE | Definir ambientes e dependências | MEDIUM | M | F0.4 | `environment.yml` | SIM — concluída |
| F0.9 | DONE | Preencher a visão geral inicial do projeto | MEDIUM | S | F0.4 | `README.md` | SIM — concluída |
| F0.10 | DONE | Estabelecer instruções permanentes e auditar setup/diretrizes | HIGH | S | F0.4, F0.5, F0.6, F0.8 | `AGENTS.md` e `00_project/setup_guidelines_audit.md` | NÃO — concluída em 2026-08-12 |
| F0.11 | DONE | Consolidar a raiz oficial e implantar continuidade independente de chats | HIGH | M | F0.10 | Estrutura consolidada, UV, memória operacional, manifesto/checksums e branch de integração | NÃO — concluída em 2026-08-12 |

## Fase 1 — Data Feasibility Map

As análises F1.2 a F1.8 são independentes entre si. Cada uma pode ser concluída sem que qualquer outra fonte da Fase 1 esteja pronta.

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F1.1 | DONE | Definir o modelo e os campos obrigatórios do Data Feasibility Map | HIGH | S | F0.4 | `00_project/data_feasibility_template.md` | SIM — concluída |
| F1.2 | DONE | Avaliar a viabilidade dos dados WIdO/PharMaAnalyst | HIGH | M | F1.1 | `00_project/feasibility/wido.md` | NÃO |
| F1.3 | DONE | Avaliar a viabilidade dos dados RKI Diabetes, incluindo separação de diabetes tipo 2 | HIGH | M | F1.1 | `00_project/feasibility/rki_diabetes.md` | NÃO |
| F1.4 | DONE | Avaliar a viabilidade dos dados RKI Obesity/GEDA | HIGH | M | F1.1 | `00_project/feasibility/rki_obesity_geda.md` | NÃO |
| F1.5 | DONE | Avaliar a viabilidade dos dados Destatis Disease Costs | HIGH | M | F1.1 | `00_project/feasibility/destatis_disease_costs.md` | NÃO |
| F1.6 | DONE | Avaliar a viabilidade dos dados Destatis Demographics | HIGH | M | F1.1 | `00_project/feasibility/destatis_demographics.md` | NÃO |
| F1.7 | DONE | Avaliar fontes públicas da IQVIA e o mercado autofinanciado | MEDIUM | M | F1.1 | `00_project/feasibility/iqvia_public_sources.md` | NÃO |
| F1.8 | DONE | Avaliar EMA e evidências clínicas aplicáveis ao modelo | HIGH | L | F1.1 | `00_project/feasibility/ema_clinical_evidence.md` | NÃO |
| F1.9 | DONE | Consolidar fontes, cobertura, formatos, chaves, limitações e funções analíticas | HIGH | M | F1.2, F1.3, F1.4, F1.5, F1.6, F1.7, F1.8 | `00_project/data_feasibility_map.md` | SIM — concluída |
| F1.10 | DONE | Registrar a decisão GO/NO-GO por dataset | HIGH | S | F1.9, F0.5 | Entrada em `00_project/decision_log.md` e lista aprovada de datasets | SIM — concluída; Fase 1 encerrada |

## Fase 2 — Aquisição e preservação dos dados

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F2.1 | DONE | Aprovar a lista final de datasets | HIGH | XS | F1.10, F0.7 | Lista aprovada em `00_project/data_feasibility_map.md` | SIM — concluída |
| F2.2 | COMPLETE WITH LIMITATIONS — aquisição parcial encerrada | Adquirir e preservar dados WIdO para 2012–2024 e ATC A10BJ efetivamente disponíveis | HIGH | S | F2.1 | Dois RAW Semaglutid 2024 duplicados e um export agregado A10BJ/2024; 2012–2023 não adquiridos | NÃO — encerrada sob D-023 |
| F2.3 | BLOCKED / NOT ACQUIRED — URLs aprovados redirecionam; XLSX não localizado | Adquirir e preservar dados RKI Diabetes | HIGH | S | F2.1 | Nenhum RAW adquirido; componente contextual e não bloqueante | NÃO — encerrada sob D-023 |
| F2.4 | DONE — duas publicações oficiais preservadas | Adquirir e preservar dados RKI Obesity | HIGH | S | F2.1 | Arquivos originais em `01_raw_data/rki_geda/` | NÃO |
| F2.5 | DONE — escopo nacional mínimo adquirido | Adquirir e preservar dados Destatis | HIGH | M | F2.1 | `12411-0005` população por idade e `23631-0001` custos por diagnóstico | NÃO |
| F2.6 | DONE — registro documental mínimo por URL | Preservar documentação oficial e estudos selecionados | MEDIUM | M | F2.1 | Referências indispensáveis em `05_sources/documentation/README.md`; nenhum parâmetro F6.2 | NÃO |
| F2.7 | DONE — manifesto completo para sete RAW existentes | Registrar metadados, nomes originais, licenças e datas de acesso | HIGH | S | F2.2, F2.3, F2.4, F2.5, F2.6 | `01_raw_data/raw_data_manifest.csv` | NÃO |
| F2.8 | DONE — sete checksums validados; Fase 2 encerrada com limitações | Calcular checksums e validar a imutabilidade RAW | HIGH | S | F2.7 | `01_raw_data/raw_data_checksums.sha256` e validação final | SIM — `COMPLETE WITH LIMITATIONS` |

## Fase 3 — Inspeção e qualidade dos dados

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F3.1 | DONE | Criar inventário dos arquivos adquiridos | HIGH | S | F2.8 | `00_project/data_inventory.md` | NÃO |
| F3.2 | DONE | Inspecionar esquema e qualidade dos dados WIdO | HIGH | M | F3.1 | `00_project/quality/wido_quality_report.md` | NÃO |
| F3.3 | BLOCKED / NOT ACQUIRED | Inspecionar esquema e qualidade dos dados RKI Diabetes | HIGH | M | F3.1 | `00_project/quality/rki_diabetes_quality_report.md` | NÃO |
| F3.4 | DONE | Inspecionar esquema e qualidade dos dados RKI Obesity | HIGH | M | F3.1 | `00_project/quality/rki_obesity_quality_report.md` | NÃO |
| F3.5 | DONE | Inspecionar esquema e qualidade dos dados Destatis Disease Costs | HIGH | M | F3.1 | `00_project/quality/destatis_disease_costs_quality_report.md` | NÃO |
| F3.6 | DONE | Inspecionar esquema e qualidade dos dados Destatis Demographics | HIGH | M | F3.1 | `00_project/quality/destatis_demographics_quality_report.md` | NÃO |
| F3.7 | DONE WITH LIMITATIONS | Validar granularidade, quebras temporais e chaves de integração | HIGH | M | F3.2, F3.3, F3.4, F3.5, F3.6 | `00_project/quality/integration_quality_report.md` | NÃO |
| F3.8 | DONE | Criar o dicionário inicial de dados | HIGH | M | F3.2, F3.3, F3.4, F3.5, F3.6 | `00_project/data_dictionary.md` | NÃO |
| F3.9 | DONE WITH LIMITATIONS | Consolidar e aprovar a avaliação de qualidade | HIGH | S | F3.7, F3.8 | `00_project/data_quality_summary.md` | SIM — autorização integrada do MVP em 2026-08-13 |

## Fase 4 — Processamento e datasets analíticos

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F4.1 | DONE | Definir e aprovar regras de limpeza por dataset | HIGH | M | F3.9 | `00_project/processing_rules.md` | SIM — autorização integrada do MVP em 2026-08-13 |
| F4.2 | DONE — MVP direto | Implementar camada intermediária reproduzível | HIGH | L | F4.1 | Pipeline em `src/`; inventário em `02_processed_data/`; tabelas finais em `04_outputs/tables/` | NÃO |
| F4.3 | DONE | Padronizar colunas, datas, unidades, códigos e categorias | HIGH | L | F4.2 | Tabelas finais padronizadas | NÃO |
| F4.4 | DONE | Tratar ausências e duplicidades conforme regras aprovadas | HIGH | M | F4.3 | Validações automatizadas e controles | NÃO |
| F4.5 | DONE WITH LIMITATIONS — corte 2024 | Construir dataset analítico WIdO GLP-1/GIP | HIGH | L | F4.4 | `04_outputs/tables/fact_wido_observed.csv` | NÃO |
| F4.6 | NOT APPLICABLE — fonte não adquirida | Construir dataset analítico RKI Diabetes | HIGH | L | F4.4 | Ausência documentada; nenhum substituto | NÃO |
| F4.7 | DONE | Construir dataset analítico RKI Obesity | HIGH | L | F4.4 | `04_outputs/tables/fact_obesity_observed.csv` | NÃO |
| F4.8 | DONE | Construir dataset analítico Destatis Disease Costs | HIGH | L | F4.4 | `04_outputs/tables/fact_disease_cost_observed.csv` | NÃO |
| F4.9 | DONE | Construir dataset analítico Destatis Demographics | HIGH | L | F4.4 | `04_outputs/tables/fact_population_observed.csv` | NÃO |
| F4.10 | DONE WITH LIMITATIONS | Validar datasets, linhagem e dicionário de dados | HIGH | M | F4.5, F4.6, F4.7, F4.8, F4.9 | `00_project/processed_data_validation.md` e dicionário atualizado | SIM — encerramento do MVP da Fase 4 |

## Fase 5 — Análise exploratória dos dados observados

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F5.1 | DONE WITH LIMITATIONS — descritiva 2024 | Analisar prescrições, DDD, gastos, custos unitários e moléculas | HIGH | L | F4.5 | `04_outputs/reports/observed_data_eda.md` | NÃO |
| F5.2 | NOT APPLICABLE — fonte não adquirida | Analisar incidência e prevalência de diabetes | HIGH | M | F4.6 | Ausência documentada; nenhum substituto | NÃO |
| F5.3 | DONE WITH LIMITATIONS — agregado total | Analisar obesidade e distribuição de BMI | HIGH | M | F4.7 | `04_outputs/reports/observed_data_eda.md` | NÃO |
| F5.4 | DONE WITH LIMITATIONS — todos os pagadores | Analisar custos de diabetes e obesidade | HIGH | M | F4.8 | `04_outputs/reports/observed_data_eda.md` | NÃO |
| F5.5 | DONE — escopo nacional mínimo | Analisar mudanças demográficas relevantes | MEDIUM | M | F4.9 | `04_outputs/reports/observed_data_eda.md` | NÃO |
| F5.6 | DONE WITH LIMITATIONS | Comparar tendências e identificar lacunas sem inferência causal indevida | HIGH | M | F5.1, F5.2, F5.3, F5.4, F5.5 | `04_outputs/reports/observed_data_eda.md` | NÃO |
| F5.7 | DONE WITH LIMITATIONS — MVP descritivo | Consolidar fatos, hipóteses, limitações, tabelas e gráficos da EDA | HIGH | M | F5.6 | `04_outputs/reports/observed_data_eda.md` | SIM — autorização integrada do MVP em 2026-08-13 |

## Fase 6 — Parâmetros clínicos e econômicos

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F6.1 | DONE | Definir critérios de inclusão das evidências | HIGH | S | F1.8 | `00_project/evidence_inclusion_criteria.md` | SIM — concluída |
| F6.2 | DONE WITH LIMITATIONS — STEP 1/EMA, escopo mínimo | Selecionar fontes de eficácia e segurança | HIGH | L | F6.1 | `05_sources/studies/clinical_evidence_register.csv` | NÃO |
| F6.3 | TODO | Extrair redução de peso, risco de diabetes e resultados cardiovasculares | HIGH | L | F6.2 | `02_processed_data/analytical/clinical_effect_parameters.csv` | NÃO |
| F6.4 | TODO | Extrair interrupção e persistência do tratamento | HIGH | M | F6.2 | `02_processed_data/analytical/treatment_persistence_parameters.csv` | NÃO |
| F6.5 | TODO | Definir custos de tratamento e custos potencialmente evitáveis | HIGH | L | F5.7 | `02_processed_data/analytical/economic_parameters.csv` | NÃO |
| F6.6 | TODO | Definir taxas de desconto e tratamento dos custos não evitáveis | HIGH | S | F6.5 | `00_project/economic_assumptions.md` | NÃO |
| F6.7 | TODO | Consolidar valores, unidades, fontes e incertezas | HIGH | M | F6.3, F6.4, F6.5, F6.6 | `00_project/assumptions_registry.md` | SIM — antes da modelagem |

## Fase 7 — Desenvolvimento do modelo econômico

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F7.1 | TODO | Definir perspectiva, política atual e estrutura conceitual | HIGH | M | F6.7 | `00_project/model_specification.md` | SIM — antes da implementação |
| F7.2 | TODO | Definir elegibilidade, adoção e horizontes temporais | HIGH | M | F7.1 | Seção de cenários em `00_project/model_specification.md` | SIM |
| F7.3 | TODO | Implementar população tratada, persistência e custos | HIGH | L | F7.2 | Módulo reproduzível do modelo econômico | NÃO |
| F7.4 | TODO | Implementar casos evitados e custos de saúde evitados | HIGH | L | F7.3 | Módulo reproduzível de resultados clínicos e custos evitados | NÃO |
| F7.5 | TODO | Implementar impacto líquido, custo por caso, ROI e break-even | HIGH | L | F7.4 | Dataset-base em `04_outputs/model_results/baseline_results.csv` | NÃO |
| F7.6 | TODO | Validar fórmulas, unidades e coerência interna | HIGH | M | F7.5 | `00_project/model_validation.md` | NÃO |
| F7.7 | TODO | Documentar premissas, equações e validação | HIGH | M | F7.6 | Especificação e registro de premissas atualizados | SIM — encerramento da Fase 7 |

## Fase 8 — Cenários e análise de sensibilidade

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F8.1 | TODO | Executar e verificar o cenário-base | HIGH | M | F7.7 | `04_outputs/model_results/baseline_results.csv` | NÃO |
| F8.2 | TODO | Executar cenários de elegibilidade, adoção e persistência | HIGH | L | F8.1 | `04_outputs/model_results/scenario_results.csv` | NÃO |
| F8.3 | TODO | Executar cenários de eficácia, custos e desconto | HIGH | L | F8.1 | `04_outputs/model_results/parameter_scenarios.csv` | NÃO |
| F8.4 | TODO | Realizar análise de sensibilidade determinística | HIGH | L | F8.2, F8.3 | `04_outputs/model_results/deterministic_sensitivity.csv` | NÃO |
| F8.5 | TODO | Avaliar viabilidade da análise probabilística | MEDIUM | M | F8.4 | `00_project/probabilistic_sensitivity_decision.md` | SIM — antes de executar, se recomendada |
| F8.6 | TODO | Executar análise probabilística, se aprovada e viável | LOW | XL | F8.5 | `04_outputs/model_results/probabilistic_sensitivity.csv` | NÃO |
| F8.7 | TODO | Identificar parâmetros críticos e condições de break-even | HIGH | M | F8.4 e F8.6, se aplicável | `04_outputs/reports/sensitivity_summary.md` | NÃO |
| F8.8 | TODO | Consolidar e aprovar resultados e incertezas | HIGH | M | F8.7 | `04_outputs/reports/model_results_summary.md` | SIM — encerramento da Fase 8 |

## Fase 9 — Resultados, visualizações e interpretação

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F9.1 | TODO | Definir KPIs e plano de visualizações | HIGH | S | F8.8 | `00_project/output_specification.md` | SIM — antes da produção final |
| F9.2 | TODO | Criar tabelas finais observadas e modeladas | HIGH | M | F9.1 | Arquivos verificados em `04_outputs/tables/` | NÃO |
| F9.3 | TODO | Criar gráficos de tendências observadas | HIGH | M | F9.1 | Arquivos verificados em `04_outputs/charts/` | NÃO |
| F9.4 | TODO | Criar gráficos de impacto, sensibilidade e break-even | HIGH | L | F9.1 | Arquivos verificados em `04_outputs/charts/` | NÃO |
| F9.5 | TODO | Validar distinção observado/modelado, títulos, unidades e fontes | HIGH | M | F9.2, F9.3, F9.4 | `00_project/output_validation.md` | NÃO |
| F9.6 | TODO | Interpretar resultados, grupos de risco e limitações | HIGH | M | F9.5 | `04_outputs/reports/results_interpretation.md` | SIM — encerramento da Fase 9 |

## Fase 10 — Relatório final e entrega reproduzível

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F10.1 | TODO | Definir a estrutura do relatório final | HIGH | S | F9.6 | `00_project/final_report_outline.md` | SIM — antes da redação |
| F10.2 | TODO | Redigir contexto, objetivo, metodologia e fontes | HIGH | L | F10.1 | Seções iniciais do relatório final | NÃO |
| F10.3 | TODO | Redigir resultados observados, modelados e sensibilidade | HIGH | L | F10.2 | Seções de resultados do relatório final | NÃO |
| F10.4 | TODO | Redigir limitações, conclusões e recomendações | HIGH | L | F10.3 | Relatório final completo em `04_outputs/reports/final_report.md` | NÃO |
| F10.5 | TODO | Revisar suporte das afirmações e classificação analítica | HIGH | M | F10.4 | `00_project/final_claims_review.md` | NÃO |
| F10.6 | TODO | Validar reprodução completa em ambiente limpo | HIGH | L | F10.5 | `00_project/reproducibility_report.md` | NÃO |
| F10.7 | TODO | Finalizar documentação de execução | HIGH | M | F10.6 | `README.md` atualizado | NÃO |
| F10.8 | TODO | Atualizar o status e realizar revisão final dos arquivos | HIGH | M | F10.7 | `PROJECT_STATUS.md` atualizado e checklist final | SIM — encerramento do projeto |

## Próxima execução operacional autorizada

Bloco F2.2–F2.8 encerrado em 2026-08-13 como `COMPLETE WITH LIMITATIONS`, conforme D-023. Não reabrir buscas WIdO 2012–2023, RKI Diabetes ou documentação ampla antes da entrega, salvo se uma lacuna indispensável da análise exigir decisão explícita.

| ID | Status | Tarefa | Prioridade | Esforço | Dependências | Entregável | Aprovação |
|---|---|---|---|---|---|---|---|
| F2.2–F2.8 | COMPLETE WITH LIMITATIONS | Aquisição mínima nacional encerrada; limitações WIdO/RKI documentadas; manifesto e checksums completos | HIGH | L | F2.1 | Sete RAW preservados localmente e validação de encerramento | SIM — encerrada sob D-023 |
| F2.3 | BLOCKED / NOT ACQUIRED | Adquirir e preservar dados RKI Diabetes | HIGH | S | F2.1 | Nenhum arquivo; uso contextual removido do caminho crítico | NÃO |
| F2.4 | DONE — duas publicações oficiais preservadas | Adquirir e preservar dados RKI Obesity | HIGH | S | F2.1 | Arquivos originais em `01_raw_data/rki_geda/` | NÃO |
| F2.5 | DONE | Adquirir e preservar dados Destatis | HIGH | M | F2.1 | Dois exports nacionais em `01_raw_data/destatis/` | NÃO |
| F2.6 | DONE | Preservar documentação oficial e estudos selecionados | MEDIUM | M | F2.1 | Registro mínimo de URLs oficiais | NÃO |
| F6.2 | DONE WITH LIMITATIONS — STEP 1/EMA, escopo mínimo | Selecionar fontes de eficácia e segurança | HIGH | L | F6.1 | `05_sources/studies/clinical_evidence_register.csv` | NÃO |

## Definition of Done

Uma tarefa somente poderá ser marcada como `DONE` quando todos os critérios abaixo forem atendidos:

- Todas as informações tiverem sido verificadas em fontes oficiais aplicáveis à tarefa.
- Todas as fontes utilizadas estiverem documentadas.
- Todas as limitações identificadas estiverem registradas.
- O entregável correspondente estiver criado e verificado.
- O `PROJECT_STATUS.md` tiver sido atualizado.

Para tarefas administrativas que não utilizam fontes externas, o primeiro e o segundo critérios são atendidos pela verificação direta dos arquivos e das instruções oficiais do próprio projeto.
