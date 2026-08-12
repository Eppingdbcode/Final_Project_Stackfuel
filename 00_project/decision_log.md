# Decision Log

Este arquivo registra decisões explícitas e aprovadas do projeto. Ele não substitui os relatórios de feasibility nem antecipa a decisão final consolidada da Fase 1.

## Estrutura do registro

Cada decisão preserva, quando disponível:

- ID e data;
- tarefa relacionada;
- decisão e classificação geral;
- decisões específicas por função;
- justificativa resumida;
- limitações e condições;
- arquivos relacionados;
- status de aprovação.

## Decisões registradas

### D-001 — Backlog oficial do projeto

- **Data:** 2026-08-10
- **Tarefa:** F0.4
- **Decisão:** aprovar a estrutura do backlog oficial com status, prioridade, esforço, dependências, entregáveis, pontos de aprovação e Definition of Done.
- **Classificação geral:** não aplicável — decisão de governança.
- **Justificativa:** criar uma sequência incremental, rastreável e orientada aos entregáveis do projeto.
- **Limitações/condições:** executar somente uma etapa por vez e aguardar aprovação antes de avançar quando indicado.
- **Arquivos relacionados:** `00_project/TASKS.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada pelo usuário.

### D-002 — Template do Data Feasibility Map

- **Data:** 2026-08-10
- **Tarefa:** F1.1
- **Decisão:** aprovar um template simples e orientado à decisão de aquisição para avaliar cada fonte antes do download.
- **Classificação geral:** não aplicável — decisão metodológica de estrutura.
- **Justificativa:** preservar somente os campos verificáveis e necessários antes da aquisição.
- **Limitações/condições:** informações desconhecidas devem permanecer não confirmadas; nenhuma métrica dependente da inspeção do arquivo deve ser inventada.
- **Arquivos relacionados:** `00_project/data_feasibility_template.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada pelo usuário.

### D-003 — WIdO / PharMaAnalyst

- **Data:** 2026-08-10
- **Tarefa:** F1.2
- **Decisão:** utilizar o PharMaAnalyst para utilização e despesa ambulatorial reembolsada pelo GKV.
- **Classificação geral:** `CONDITIONAL GO`.
- **Decisões por função:** utilização GKV e despesa GKV permitidas; consumo total alemão, mercado self-pay, pacientes e indicação clínica não são suportados.
- **Justificativa:** a fonte contém prescrições, DDD e custos por medicamento, substância e ATC no universo ambulatorial cobrado do GKV.
- **Limitações/condições:** o formato real do export permanece não confirmado; não inclui receitas privadas/self-pay e não identifica indicação clínica; redistribuição dos exports não foi confirmada.
- **Arquivos relacionados:** `00_project/feasibility/wido.md`, `00_project/data_feasibility_map.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada oficialmente pelo usuário.

### D-004 — RKI Diabetes Surveillance

- **Data:** 2026-08-10
- **Tarefa:** F1.3
- **Decisão:** utilizar a fonte como contexto epidemiológico para prevalência e incidência documentadas de diabetes no GKV.
- **Classificação geral:** `CONTEXTUAL DATASET`.
- **Decisões por função:** adequada para contexto de diabetes documentado e segmentações publicadas; inadequada como base principal exclusiva para diabetes tipo 2.
- **Justificativa:** oferece indicadores oficiais baseados em dados administrativos amplos do GKV.
- **Limitações/condições:** os indicadores adultos principais agregam E10–E14; não há isolamento longitudinal público confiável de T2D; cobertura temporal confirmada é limitada.
- **Arquivos relacionados:** `00_project/feasibility/rki_diabetes.md`, `00_project/data_feasibility_map.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada pelo usuário.

### D-005 — Destatis Disease Costs

- **Data:** 2026-08-10
- **Tarefa:** F1.5
- **Decisão:** utilizar a Krankheitskostenrechnung como baseline econômico oficial nacional dos custos diretos atribuídos a diabetes e obesidade.
- **Classificação geral:** `CONDITIONAL GO`.
- **Decisões por função:** adequada como baseline nacional; não é estimativa direta do GKV, de custos evitáveis ou de economia por GLP-1/GIP.
- **Justificativa:** fonte oficial nacional com custos por diagnóstico, idade, sexo e estabelecimento em anos publicados.
- **Limitações/condições:** E10–E14 não isola T2D; E65–E68 é mais amplo que obesidade isolada; não separa pagador; participação GKV, proporção de T2D e fração evitável dependem de fontes defensáveis ou `modelled assumptions`.
- **Arquivos relacionados:** `00_project/feasibility/destatis_disease_costs.md`, `00_project/data_feasibility_map.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada pelo usuário.

### D-006 — RKI Obesity / GEDA

- **Data:** 2026-08-10
- **Tarefa:** F1.4
- **Decisão:** utilizar RKI/GEDA como baseline epidemiológico oficial da prevalência de obesidade adulta na Alemanha.
- **Classificação geral:** `CONDITIONAL GO`.
- **Decisões por função:** segmentações publicamente verificadas por ano, idade, sexo e educação são permitidas; análises estaduais e classes de obesidade pelo SUF permanecem condicionais.
- **Justificativa:** fonte oficial nacional com estimativas ponderadas de obesidade e documentação metodológica.
- **Limitações/condições:** peso e altura autorrelatados; prevalência não equivale a diagnóstico, GKV ou elegibilidade; classes derivadas exigem dicionário, variáveis, pesos, precisão e acesso formal ao SUF; qualquer atualização para 2026 será `modelled estimate`.
- **Arquivos relacionados:** `00_project/feasibility/rki_obesity_geda.md`, `00_project/data_feasibility_map.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada pelo usuário.

### D-007 — Destatis Demographics

- **Data:** 2026-08-10
- **Tarefa:** F1.6
- **Decisão:** utilizar o Destatis Demographics como denominador demográfico oficial.
- **Classificação geral:** `GO`.
- **Decisões por função:** permite converter prevalências em números absolutos e construir segmentações por idade, sexo, ano e, quando compatível, estado federal.
- **Justificativa:** tabelas oficiais recentes, tecnicamente reutilizáveis e com idade individual, sexo e geografia.
- **Limitações/condições:** população residente não equivale a GKV, diagnóstico ou elegibilidade; resultados 12411 são `official population estimate`; projeções 12421 são `official population projection`; variante de 2026 e harmonizações devem ser documentadas; considerar revisões do Censo 2022.
- **Arquivos relacionados:** `00_project/feasibility/destatis_demographics.md`, `00_project/data_feasibility_map.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada pelo usuário.

### D-008 — Fontes públicas IQVIA e mercado autofinanciado

- **Data:** 2026-08-10
- **Tarefa:** F1.7
- **Decisão:** utilizar materiais públicos IQVIA somente como evidência contextual e fonte de valores pontuais rigorosamente rotulados.
- **Classificação geral:** `CONTEXTUAL DATASET`.
- **Decisões por função:** `NO-GO` como dataset quantitativo reproduzível; `GO` para contexto e valores pontuais; `NO-GO` para quantificação defensável do mercado self-pay exclusivamente com fontes públicas.
- **Justificativa:** os materiais públicos documentam métricas, canais e valores pontuais, mas não fornecem série tabular pública reproduzível por pagador e canal.
- **Limitações/condições:** painel projetado não é registro administrativo integral; private prescription não equivale a self-pay; PKV, GKV pagando privadamente e pagamento direto não são separáveis; vendas, embalagens, prescrições, dispensações e pacientes são métricas distintas; valores pontuais não devem preencher séries ou uptake futuro.
- **Arquivos relacionados:** `00_project/feasibility/iqvia_public_sources.md`, `00_project/data_feasibility_map.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada pelo usuário.

### D-009 — EMA e evidências clínicas

- **Data:** 2026-08-10
- **Tarefa:** F1.8
- **Decisão:** utilizar a EMA como fonte normativa e ensaios clínicos como fontes condicionais de parâmetros dentro do escopo estudado.
- **Classificação geral:** `CONDITIONAL GO`.
- **Decisões por função:** elegibilidade regulatória `GO`; perda de peso, controle glicêmico, descontinuação/eventos adversos, eventos cardiovasculares, eventos renais, comparação entre medicamentos, transferibilidade e uso econômico `CONDITIONAL GO`; persistência do efeito no longo prazo `CONTEXTUAL EVIDENCE`.
- **Justificativa:** EPARs/SmPCs definem marca, indicação, população e dose; RCTs fornecem efeitos e incerteza para populações e horizontes específicos.
- **Limitações/condições:** indicação EMA não equivale a cobertura GKV ou apropriação clínica individual; eficácia não equivale a efetividade; SELECT e FLOW não podem ser generalizados; marcas do mesmo princípio ativo não são intercambiáveis; comparações exigem head-to-head randomizado ou método formalmente defensável; extrapolações serão `modelled assumptions`.
- **Arquivos relacionados:** `00_project/feasibility/ema_clinical_evidence.md`, `00_project/data_feasibility_map.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada pelo usuário.

### D-010 — Data Feasibility Map consolidado

- **Data:** 2026-08-10
- **Tarefa:** F1.9
- **Decisão:** aprovar o mapa consolidado como representação rastreável e operacional das avaliações F1.2–F1.8.
- **Classificação geral:** não aplicável — consolidação metodológica; as classificações individuais foram preservadas.
- **Justificativa:** o mapa separa fontes, funções, cobertura, formatos, chaves, compatibilidades, limitações e natureza da evidência.
- **Limitações/condições:** o mapa está completo para as fontes avaliadas, mas não elimina lacunas de self-pay, indicação, comparabilidade populacional, persistência, uptake e transferibilidade clínica.
- **Arquivos relacionados:** `00_project/data_feasibility_map.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada pelo usuário.

## Reserva para F1.10

A seção abaixo registra a decisão da F1.10, formalmente aprovada pelo usuário em 2026-08-10, e o encerramento documental da Fase 1.

## D-011 — Decisão consolidada de feasibility da Fase 1

- **Data:** 2026-08-10
- **Tarefa:** F1.10
- **Decisão final proposta:** `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`.
- **Status:** formalmente aprovada em 2026-08-10; Fase 1 encerrada.
- **Escopo:** decisões operacionais por fonte e função, lista aprovada de datasets/componentes e limites para a fase seguinte.
- **Arquivos relacionados:** `00_project/data_feasibility_map.md`, arquivos aprovados de F1.2–F1.8, `00_project/TASKS.md` e `PROJECT_STATUS.md`.

### 1. Lista operacional aprovada

| ID | Fonte ou componente | Instituição | Natureza da evidência | Decisão operacional consolidada | Funções aprovadas | Funções proibidas | Condições, harmonização e necessidades futuras | Limitações principais | Avaliação interna | Aprovação |
|---|---|---|---|---|---|---|---|---|---|---|
| `DESTATIS-DEM` | Destatis Demographics: população atualizada e projeções oficiais | Destatis | `official population estimate`; `official population projection`; `derived calculation` para agregações | `GO` | Denominador demográfico oficial por idade, sexo, ano e estado quando compatível; cenário populacional oficial | Inferir GKV, diagnóstico, BMI ou elegibilidade clínica; chamar projeção de contagem observada | Harmonizar período/população/faixas; registrar base censitária e variante da projeção; agregações serão `derived calculations` | Censo 2022, diferença entre população residente e GKV, data de referência | `00_project/feasibility/destatis_demographics.md` | Aprovada |
| `RKI-GEDA` | RKI/GEDA agregado | RKI | `official survey estimate` baseada em `observed survey data` autorrelatados | `CONDITIONAL GO` | Baseline oficial de prevalência de obesidade adulta; idade, sexo, ano/onda e educação publicados | Contagem direta de elegíveis, diagnóstico, GKV ou classes não verificadas | Harmonizar método, período, população, BMI, idade, sexo e denominador; atualização para 2026 será `modelled estimate` | Peso/altura autorrelatados, comparabilidade entre ondas e precisão por segmento | `00_project/feasibility/rki_obesity_geda.md` | Aprovada |
| `RKI-GEDA-SUF` | GEDA Scientific Use File | RKI/FDZ | Microdados de survey; futuras estimativas ponderadas | `CONDITIONAL GO` | Classes de BMI e segmentações customizadas somente após verificação | Considerar classes/variáveis disponíveis antes da inspeção | Exige acesso formal, dicionário, BMI/peso/altura, pesos, tamanho amostral, IC e estabilidade; cálculos serão `derived calculations` | Acesso condicionado e precisão desconhecida | `00_project/feasibility/rki_obesity_geda.md` | Aprovada com condições |
| `WIDO-PMA` | WIdO/PharMaAnalyst | WIdO | `observed administrative data` do GKV | `CONDITIONAL GO` | Utilização e despesa ambulatorial reembolsada pelo GKV por medicamento/substância/ATC | Mercado total, self-pay, pacientes e indicação clínica | Confirmar export, período e esquema; harmonizar ATC, substância, marca, ano e unidades; qualquer conversão não observada exigirá regra própria | Não inclui consumo privado/hospitalar; indicação ausente; formato do export não confirmado | `00_project/feasibility/wido.md` | Aprovada |
| `GKV-GAMSI` | GKV-Arzneimittel-Schnellinformation | GKV-Spitzenverband | Evidência administrativa/contextual agregada | `CONTEXTUAL ONLY`; sem classificação independente na avaliação original | Validação e triangulação agregada de tendências do GKV | Dataset principal ou substituto silencioso de séries por substância | Alinhar período, métrica e cobertura antes de validar | Cobertura e granularidade detalhadas não foram avaliadas na F1.2 | `00_project/feasibility/wido.md` | Papel contextual aprovado |
| `RKI-DIAB` | RKI Diabetes Surveillance | RKI | `observed administrative data` e indicadores derivados | `CONTEXTUAL ONLY` | Contexto epidemiológico de prevalência e incidência documentadas no GKV | Isolar automaticamente T2D; representar população residente alemã | Harmonizar universo GKV, ano, idade, sexo e geografia; separação de T2D exigiria fonte/método adicional | E10–E14 agregado e série pública confirmada limitada | `00_project/feasibility/rki_diabetes.md` | Aprovada |
| `DESTATIS-KK` | Destatis Disease Costs | Destatis | Estimativa oficial nacional de custos por doença | `CONDITIONAL GO` | Baseline econômico oficial nacional de custos diretos atribuídos a diabetes e obesidade | Custo direto do GKV, custo por paciente tratado ou custo automaticamente evitável | Harmonizar diagnóstico, período, população, pagador, categoria e atribuição; participação GKV, T2D e fração evitável exigem fonte adicional ou `modelled assumptions` | E10–E14, E65–E68, ausência de pagador e abordagem top-down | `00_project/feasibility/destatis_disease_costs.md` | Aprovada |
| `IQVIA-CONTEXT` | Materiais públicos IQVIA e valores pontuais | IQVIA | `projected panel estimate`, `company-reported figure` e contexto metodológico | `CONTEXTUAL ONLY` | Contextualizar demanda/mercado fora do faturamento regular do GKV e citar valores pontuais rotulados | Alimentar estimativa central self-pay, pacientes, indicação ou uptake | Preservar período, métrica, unidade, cobertura, projeção, canal e tipo de preço; não extrapolar séries | Painéis não integrais; private prescription ≠ self-pay; PKV e pagamento direto não separáveis | `00_project/feasibility/iqvia_public_sources.md` | Aprovada |
| `IQVIA-PUBLIC-DATASET` | Dataset quantitativo reproduzível IQVIA a partir das fontes públicas avaliadas | IQVIA | Não disponível publicamente | `NO-GO` | Nenhuma para o uso quantitativo principal | Série pública reproduzível GLP-1/GIP por pagador/canal | Exigiria nova fonte pública adequada ou aquisição/licença avaliada separadamente | Sem CSV/XLSX/API/microdados públicos adequados | `00_project/feasibility/iqvia_public_sources.md` | NO-GO aprovado |
| `SELF-PAY-PUBLIC` | Quantificação defensável do mercado self-pay somente com fontes públicas avaliadas | Não aplicável | Não disponível | `NO-GO` | Nenhuma estimativa central | Inferir self-pay por diferença, PKV, receita privada ou ausência de reembolso | Exigiria fonte adicional ou `modelled assumption` explícita com sensibilidade; não autorizada nesta fase | Pagador final, indicação, pacientes e canais não separáveis | `00_project/feasibility/iqvia_public_sources.md` | NO-GO aprovado |
| `IQVIA-COMMERCIAL` | Produto comercial IQVIA não adquirido | IQVIA | Produto proprietário não avaliado | Não disponível para uso atual; sem decisão de adequação | Nenhuma no estado atual | Presumir adequação ou utilizar sem licença/aquisição e avaliação | Exigiria decisão própria de aquisição, termos de uso e feasibility técnica | Conteúdo, campos, cobertura e validade para self-pay não confirmados | `00_project/feasibility/iqvia_public_sources.md` | Não aplicável |
| `EMA-REG` | EPARs, SmPCs e assessment reports | EMA | `regulatory indication` | `GO` exclusivamente para função regulatória | Marca, indicação autorizada, população, idade, BMI, comorbidades, dose e condições regulatórias | Efetividade real, reembolso GKV, recomendação clínica individual, uptake ou persistência | Preservar produto, versão, indicação e dose; marcas do mesmo princípio ativo não são intercambiáveis | Autorização não equivale a tratamento ou cobertura | `00_project/feasibility/ema_clinical_evidence.md` | Aprovada |
| `CLINICAL-RCT` | Evidências clínicas randomizadas | EMA/documentos regulatórios e publicações primárias | `randomized clinical trial evidence` | `CONDITIONAL GO` | Peso, glicemia, segurança, descontinuação, eventos CV/renais e comparação formal dentro do escopo estudado | Generalizar além da população; converter peso diretamente em eventos/custos; selecionar medicamento-base nesta fase | Preservar marca, dose, população, diabetes, comparador, estimando, horizonte, endpoint, incerteza e fonte; extrapolações serão `modelled assumptions` | Eficácia ≠ efetividade; validade externa; patrocínio e heterogeneidade | `00_project/feasibility/ema_clinical_evidence.md` | Aprovada |
| `CLINICAL-LONG-TERM` | Persistência do efeito no longo prazo | Ensaios/extensões | `CONTEXTUAL EVIDENCE` | `CONTEXTUAL ONLY` | Contextualizar manutenção em tratamento e recuperação após retirada | Definir persistência real ou curva vitalícia | Requer RWE adicional e assumptions para horizontes posteriores | Extensões/withdrawal não equivalem a persistência real | `00_project/feasibility/ema_clinical_evidence.md` | Aprovada |
| `CROSS-TRIAL-RAW` | Comparação bruta STEP × SURMOUNT × SCALE | Não aplicável | Comparação descritiva não causal | `NO-GO` | Nenhuma para superioridade relativa | Ranking ou inferência comparativa por percentuais brutos | Comparação exige head-to-head randomizado ou método formal defensável | População, dose, estimando, missing data e horizonte incompatíveis | `00_project/feasibility/ema_clinical_evidence.md` | NO-GO funcional aprovado |
| `FEASIBILITY-MAP` | Data Feasibility Map consolidado | Projeto | Artefato de governança e integração | Sem classificação empírica independente | Consolidação, rastreabilidade e controle metodológico | Fonte primária de valores ou dataset analítico | Remeter sempre às fontes originais e preservar suas classificações | Não contém observações empíricas próprias | `00_project/data_feasibility_map.md` | Aprovado como artefato |

### 2. Agrupamento operacional A–E

#### A. Aprovados para uso direto delimitado

- `DESTATIS-DEM`: denominador demográfico oficial, preservando estimativa versus projeção.
- `EMA-REG`: função regulatória exclusivamente.

#### B. Aprovados com condições ou harmonização

- `RKI-GEDA` e `RKI-GEDA-SUF`.
- `WIDO-PMA`.
- `DESTATIS-KK`.
- `CLINICAL-RCT`.

#### C. Contextuais apenas

- `GKV-GAMSI`.
- `RKI-DIAB`.
- `IQVIA-CONTEXT`.
- `CLINICAL-LONG-TERM`.
- `FEASIBILITY-MAP`, exclusivamente como artefato de governança, não como evidência empírica.

#### D. Não aprovados para o uso pretendido

- `IQVIA-PUBLIC-DATASET`: dataset quantitativo reproduzível a partir das fontes públicas avaliadas.
- `SELF-PAY-PUBLIC`: quantificação defensável do mercado self-pay somente com dados públicos avaliados.
- `CROSS-TRIAL-RAW`: inferência de superioridade por comparação bruta entre estudos.

#### E. Não disponíveis ou dependentes de fonte adicional

- `IQVIA-COMMERCIAL`: não adquirido e não avaliado quanto à adequação.
- População clinicamente apropriada e efetivamente coberta para GLP-1/GIP.
- Participação do GKV nos custos por doença, proporção específica de T2D e fração de custos evitável.
- Persistência/adesão real alemã, efetividade real, indicação observada, uptake e pacientes tratados/autofinanciados.

### 3. Decisão final da Fase 1

#### 3.1 É possível construir uma primeira versão defensável?

**Sim, sob condições.** Há base suficiente para preparar e ingerir controladamente denominadores demográficos, prevalência de obesidade, utilização/despesa GKV, custos nacionais por doença, regras regulatórias e parâmetros clínicos delimitados. Isso não autoriza ainda aquisição ou ingestão.

#### 3.2 Módulos com dados observados ou estimativas oficiais

- Denominador demográfico oficial.
- Prevalência oficial de obesidade adulta.
- Utilização e despesa ambulatorial reembolsada pelo GKV.
- Baseline econômico oficial nacional por doença.
- Critérios regulatórios por marca.
- Parâmetros de RCT dentro do escopo estudado.

#### 3.3 Módulos que exigem harmonização

- Prevalência × população.
- Critérios EMA × epidemiologia.
- WIdO × substância/marca/ATC e período.
- Custos por doença × diagnóstico, pagador e horizonte.
- Evidência clínica × segmentos epidemiológicos alemães.

#### 3.4 Módulos dependentes de evidência contextual

- Diabetes documentado no GKV.
- Mercado fora do GKV e valores pontuais IQVIA.
- Validação agregada por GKV-GAmSi.
- Persistência do efeito no longo prazo.

#### 3.5 Módulos que permanecem NO-GO com os dados públicos avaliados

- Dataset público IQVIA quantitativo e reproduzível para o mercado pretendido.
- Quantificação defensável do mercado self-pay.
- Inferência de superioridade por comparação bruta entre ensaios.

#### 3.6 Resultados que dependerão de `derived calculations`

- Agregação de idades e construção de faixas compatíveis.
- Conversão de prevalências compatíveis em números absolutos.
- Padronizações e harmonizações reproduzíveis entre códigos, unidades e períodos.
- Segmentações derivadas do SUF, somente após verificação e acesso.

#### 3.7 Resultados que dependerão de `modelled assumptions`

- Atualização/projeção epidemiológica para 2026 quando não publicada.
- População regulatoriamente elegível e clinicamente apropriada quando critérios não forem diretamente observados.
- Participação do GKV nos custos, proporção de T2D e fração evitável.
- Uptake, adesão, persistência, efetividade real, extrapolação clínica/econômica e self-pay sem observação direta.

#### 3.8 Lacunas que impedem afirmações causais ou estimativas diretas

- Ausência de indicação nas fontes de mercado.
- Métricas de vendas/prescrições/DDD/pacotes não equivalentes a pacientes.
- Self-pay, receita privada GKV e PKV não separáveis publicamente.
- T2D não isolado nas principais fontes administrativas/econômicas avaliadas.
- Eficácia de ensaio não equivalente a efetividade alemã.
- Comparabilidade insuficiente para ranking bruto entre ensaios.

#### 3.9 Limitações obrigatórias em resultados futuros

- População residente, survey, GKV, diagnosticada, regulatoriamente elegível, clinicamente apropriada e tratada são universos distintos.
- Projeções não são contagens observadas.
- Peso/altura do GEDA são autorrelatados.
- WIdO não mede mercado total nem indicação.
- Destatis Disease Costs não mede automaticamente GKV ou custos evitáveis.
- Parâmetros clínicos valem somente no escopo estudado; extrapolações devem ser rotuladas e testadas.

#### 3.10 Escopo autorizado para a fase seguinte

Com a aprovação formal desta decisão, fica autorizada apenas a preparação da governança de aquisição e, mediante autorização específica posterior, a ingestão controlada das fontes aprovadas. Continuam não autorizados downloads automáticos, cálculos, joins, população elegível, pacientes, self-pay, uptake, medicamento-base, extrapolações e modelo econômico.

### 4. Condições para prosseguir

1. Aprovação formal do usuário obtida em 2026-08-10; Fase 1 encerrada.
2. Concluir os pré-requisitos de governança da aquisição, especialmente o padrão de manifesto/checksums RAW previsto em F0.7.
3. Aprovar a lista final de datasets em F2.1 antes de qualquer download.
4. Preservar RAW, registrar origem/versão/data/licença e manter processamento separado.
5. Validar esquema, chaves, unidades e compatibilidade antes de qualquer integração.
6. Rotular separadamente dados observados, estimativas oficiais, projeções, `derived calculations` e `modelled assumptions`.
7. Documentar e testar assumptions em análise de sensibilidade nas fases correspondentes.

### 5. Limite de autorização

A decisão aprovada não inicia a Fase 2 e não autoriza download, ingestão, transformação, análise, cálculo ou modelagem. A Fase 1 foi formalmente encerrada em 2026-08-10.

## D-012 — Padrão do manifesto e checksums RAW

- **Data:** 2026-08-10
- **Tarefa:** F0.7
- **Decisão:** aprovar o template obrigatório de manifesto RAW, SHA-256, imutabilidade, quarentena lógica, cadeia de custódia, preservação de versões e separação entre RAW e derivados.
- **Classificação geral:** não aplicável — decisão de governança.
- **Justificativa:** garantir rastreabilidade, integridade, versionamento e preservação antes de qualquer aquisição.
- **Limitações/condições:** não autoriza download, checksum real, criação de diretório RAW, automação ou processamento; formas técnicas de feasibility são representações dos mesmos conceitos documentais aprovados.
- **Arquivos relacionados:** `00_project/raw_data_manifest_template.md`, `00_project/TASKS.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada formalmente pelo usuário em 2026-08-10.

## D-013 — Convenções de nomes, versões e datas

- **Data:** 2026-08-10
- **Tarefa:** F0.6
- **Decisão:** definir convenções técnicas em inglês, IDs e nomes em `snake_case`, datas/timestamps ISO 8601, versionamento sem sobrescrita e mapeamento explícito entre rótulos documentais e valores técnicos.
- **Classificação geral:** não aplicável — decisão de governança.
- **Justificativa:** manter artefatos estáveis, legíveis, auditáveis e compatíveis com o manifesto RAW aprovado.
- **Limitações/condições:** nenhuma camada, arquivo de dados, código ou checksum foi criado.
- **Arquivos relacionados:** `00_project/data_conventions.md`, `00_project/raw_data_manifest_template.md`, `00_project/TASKS.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada formalmente pelo usuário em 2026-08-10.

## D-014 — Formato e versões do ambiente técnico

- **Data:** 2026-08-10
- **Tarefa:** F0.8
- **Decisão:** usar Conda/Mamba com `environment.yml`, ambiente `glp1_germany`, canal exclusivo `conda-forge` seguido de `nodefaults`, Python 3.14 e somente as dependências diretas aprovadas.
- **Classificação geral:** não aplicável — decisão arquitetural.
- **Requisito externo:** Python 3.14 é exigência documental do curso. A instalação local do Python 3.14.2 não é a justificativa da escolha.
- **Versão do Python:** especificar `python=3.14`, sem fixar automaticamente o patch 3.14.2.
- **Dependências diretas:** `pandas` para manipulação tabular; `openpyxl` para XLSX; `matplotlib` e `seaborn` para visualizações; `jupyterlab` para notebooks; `pytest` para testes.
- **Dependências transitivas:** serão determinadas futuramente pelo gerenciador durante resolução autorizada; não foram escolhidas manualmente.
- **Dependências opcionais ou pendentes:** nenhuma incluída. Pacotes para formatos ou funções condicionais futuras exigirão decisão própria.
- **Reprodutibilidade:** `environment.yml` é a especificação declarativa. Compatibilidade, versões resolvidas e reprodutibilidade efetiva somente poderão ser confirmadas após resolução, instalação e validação futuras autorizadas.
- **Lockfile:** não criado; eventual arquivo resolvido será gerado somente em tarefa autorizada após resolução bem-sucedida.
- **Segurança:** credenciais, tokens, senhas, chaves e URLs privadas com credenciais são proibidos no ambiente e no versionamento.
- **Sistemas operacionais:** Windows é o ambiente local documentado; portabilidade para outros sistemas permanece não testada.
- **Limitações/condições:** nenhum gerenciador foi executado, nenhum pacote foi instalado, atualizado ou removido, nenhum ambiente foi criado/ativado, nenhum import foi testado e nenhum lockfile foi gerado.
- **Arquivos relacionados:** `environment.yml`, `00_project/TASKS.md`, `PROJECT_STATUS.md`, `00_project/data_conventions.md`, `00_project/raw_data_manifest_template.md`.
- **Aprovação:** aprovada formalmente pelo usuário em 2026-08-10.

## D-015 — Visão geral inicial do projeto

- **Data da execução técnica:** 2026-08-10
- **Data da aprovação formal:** 2026-08-11
- **Tarefa:** F0.9
- **Status final:** `DONE`.
- **Decisão:** preencher o `README.md` como ponto de entrada factual, conciso e navegável do repositório, sem substituir os documentos de governança, feasibility ou metodologia.
- **Classificação geral:** não aplicável — decisão de documentação e governança.
- **Justificativa:** apresentar problema, objetivos, escopo, princípios metodológicos, status real, estrutura, ambiente técnico, documentos de controle, fluxo planejado e próximos passos em um único documento inicial.
- **Escopo da aprovação:** aprovação limitada ao conteúdo documental atual do `README.md` como visão geral inicial do projeto.
- **Limitações/condições:** a Fase 2 não foi iniciada; nenhum dataset foi adquirido; não existem resultados analíticos; o ambiente permanece apenas declarativo, não resolvido nem validado; esta aprovação não autoriza implicitamente F2.1, F6.1 ou qualquer outra tarefa.
- **Arquivos relacionados:** `README.md`, `00_project/TASKS.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada formalmente pelo usuário em 2026-08-11.

## D-016 — Critérios de inclusão das evidências clínicas e econômicas

- **Data da execução técnica:** 2026-08-11
- **Data da aprovação formal:** 2026-08-11
- **Tarefa:** F6.1
- **Status final:** `DONE`.
- **Decisão:** adotar uma estrutura de evidência por finalidade do parâmetro, com critérios prévios e verificáveis para elegibilidade, exclusão, hierarquia de fontes, transferibilidade, qualidade, rastreabilidade e controle de mudanças.
- **Classificação geral:** não aplicável — decisão metodológica aprovada.
- **Justificativa:** evitar seleção oportunista sem impor ao projeto a alegação de revisão sistemática formal, mantendo fontes oficiais alemãs prioritárias, mas não exclusivas, e preservando a diferença entre evidência observada, cálculo derivado e pressuposto modelado.
- **Escopo da aprovação:** aprovação limitada à versão atual do protocolo documental `00_project/evidence_inclusion_criteria.md`.
- **Decisões pendentes preservadas:** estratégia e bases da busca, strings, idioma, período, número de revisores, resolução de discordâncias, ferramentas de qualidade/risco de viés, perspectiva econômica, horizonte, ano-base, desconto, população/intervenção/comparador-base, comparação indireta, extrapolação e conversão para parâmetros econômicos permanecem não aprovados.
- **Condições:** nenhuma busca, triagem, seleção, deduplicação, extração, avaliação de evidência ou modelagem foi autorizada ou executada; nenhum estudo, fonte ou valor de parâmetro foi aprovado; F6.2 e F2.1 não foram iniciadas; qualquer alteração posterior nos critérios deverá ser justificada, datada e versionada.
- **Arquivos relacionados:** `00_project/evidence_inclusion_criteria.md`, `00_project/feasibility/ema_clinical_evidence.md`, `00_project/TASKS.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada formalmente pelo usuário em 2026-08-11; não autoriza qualquer etapa posterior.

## D-017 — Lista final de datasets para futura aquisição

- **Data da execução técnica:** 2026-08-11
- **Data da aprovação formal:** 2026-08-11
- **Tarefa:** F2.1
- **Status final:** `DONE`.
- **Decisão:** consolidar no `data_feasibility_map.md` a lista final de datasets, documentos e componentes para futura aquisição, usando `APPROVED`, `CONDITIONALLY APPROVED`, `NOT APPROVED` e `PENDING DECISION`.
- **Classificação geral:** `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`, sem alteração.
- **Escopo da aprovação:** aprovação limitada à lista documental e às finalidades definidas na seção 13 do `data_feasibility_map.md`; não representa aquisição, presença local, acesso operacional validado, licença definitiva, reutilização irrestrita ou adequação analítica.
- **Resumo das classificações:** `APPROVED`: `DESTATIS-POP`, `DESTATIS-PROJ`, `EMA-REG`; `CONDITIONALLY APPROVED`: `WIDO-PMA`, `RKI-DIAB-PREV`, `RKI-DIAB-INC`, `RKI-GEDA-AGG`, `RKI-GEDA-SUF`, `DESTATIS-KK`, `DE-REG-CONTEXT`, `IQVIA-CONTEXT`; `PENDING DECISION`: `GKV-GAMSI`, `CLINICAL-STUDIES`; `NOT APPROVED`: `IQVIA-PUBLIC-DATASET`, `SELF-PAY-PUBLIC`, `IQVIA-COMMERCIAL`, `CROSS-TRIAL-RAW`, `FEASIBILITY-MAP-AS-DATA`.
- **Condições:** confirmar identidade, arquivo, formato, período, esquema, licença/termos, versão e método de acesso antes da aquisição; preservar RAW e manifesto; não adquirir componentes pendentes ou não aprovados.
- **Limitações e pendências preservadas:** nenhum linkage foi confirmado; variáveis deriváveis não são observadas; acesso público não equivale a reutilização; os universos demográficos, survey, GKV, clínicos e regulatórios permanecem distintos; formatos, esquemas, períodos, licenças, versões e métodos de acesso ainda pendentes continuam não confirmados.
- **Restrições:** componentes `PENDING DECISION` permanecem não autorizados para aquisição; componentes `NOT APPROVED` permanecem rejeitados; nenhuma tarefa de aquisição e nenhuma F6.2 foi iniciada; qualquer alteração posterior na lista ou classificação deverá ser justificada, datada e versionada.
- **Arquivos relacionados:** `00_project/data_feasibility_map.md`, `00_project/raw_data_manifest_template.md`, `00_project/decision_log.md`, `00_project/TASKS.md`, `PROJECT_STATUS.md`.
- **Aprovação:** aprovada formalmente pelo usuário em 2026-08-11; não autoriza automaticamente F2.2–F2.6, F6.2 ou qualquer outra tarefa.

## D-018 — Aquisição parcial dos dados WIdO

> **Superação:** os bloqueios decisionais sobre anos, escopo ATC e armazenamento registrados nesta decisão foram resolvidos pela D-022. A D-018 permanece preservada como histórico.

- **Data da execução técnica:** 2026-08-11
- **Tarefa:** F2.2
- **Status:** `IN PROGRESS — aquisição parcial; seleção sistemática de anos/substâncias aguarda decisão do usuário`.
- **Decisão:** preservar como RAW a exportação oficial de teste do PharMaAnalyst para `Semaglutid (A10BJ06)`, ano de referência 2024, com todas as cinco métricas disponíveis selecionadas, e interromper a aquisição sistemática antes de escolher silenciosamente combinações adicionais de anos e substâncias.
- **Identidade e origem:** `WIDO-PMA`, PharMaAnalyst / GKV-Arzneimittelindex, Wissenschaftliches Institut der AOK (WIdO); página documental `https://www.wido.de/publikationen-produkte/analytik/pharmaanalyst/`; portal operacional `https://arzneimittel.wido.de/PharMaAnalyst/`; acesso em 2026-08-11, sem login.
- **Arquivo preservado:** `01_raw_data/wido/wirkst_export.csv`; nome original `wirkst_export.csv`; CSV delimitado por ponto e vírgula; 556 bytes; conteúdo preservado sem edição, conversão, renomeação, descompactação ou sobrescrita.
- **Versão e período:** dados de 2024; portal identificado como atualizado em 07.10.2025 com dados de prescrições de 2024.
- **Validação mínima:** existência, caminho, nome, extensão, tamanho em bytes e assinatura textual compatível com CSV confirmados; o início do arquivo não corresponde a página HTML de erro. Nenhuma inspeção analítica, contagem de linhas, leitura de esquema ou validação de valores foi realizada.
- **Condições de uso:** acesso público e exportação confirmados; o portal exibe `Alle Rechte vorbehalten`. Licença específica e autorização de redistribuição do export permanecem não confirmadas; disponibilidade pública não foi interpretada como licença aberta.
- **Bloqueio:** o portal gera uma exportação separada por ano/consulta e reutiliza o nome `wirkst_export.csv`. A documentação aprovada registra 2012–2024 e substâncias relevantes, mas não define quais combinações de anos/substâncias devem compor a aquisição sistemática nem a regra para armazenar múltiplos arquivos de mesmo nome. Essa seleção material e a estratégia de nomes/caminhos exigem decisão explícita do usuário.
- **Limitações preservadas:** dados restritos a prescrições ambulatoriais cobradas do GKV; não incluem privado, self-pay ou uso hospitalar; não informam indicação clínica; ATC e disponibilidade entre anos podem variar; o painel anual pode ser desequilibrado.
- **Restrições:** nenhum manifesto ou checksum foi criado; nenhuma transformação, análise, código, notebook, teste, instalação, resolução de ambiente ou tarefa F2.3–F2.8/F6.2 foi executada.
- **Arquivos relacionados:** `01_raw_data/wido/wirkst_export.csv`, `00_project/TASKS.md`, `PROJECT_STATUS.md`.
- **Aprovação:** execução parcial registrada; F2.2 não está tecnicamente concluída e aguarda decisão do usuário sobre o escopo sistemático.

## D-019 — Raiz oficial, consolidação e ambiente UV

- **Data:** 2026-08-12
- **Tarefa:** F0.11
- **Decisão:** adotar `C:\Users\eppin\Desktop\Final_Project_Stackfuel` como única raiz oficial, preservar seu histórico Git/remoto e usar UV como único gerenciador ativo.
- **Substituição formal:** esta decisão substitui D-014 para o ambiente executável do repositório oficial. D-014 permanece preservada como decisão histórica da pasta anterior.
- **Fontes de verdade do ambiente:** `.python-version`, `pyproject.toml`, `uv.lock` e `.venv` gerenciada por UV; Python 3.14 permanece requisito do curso.
- **Conda:** `environment.yml` não foi incorporado; é artefato histórico existente apenas no backup temporário. Conda e UV não podem coexistir como fontes concorrentes.
- **Dependências:** removido `seeborn`; mantidos `pandas`, `matplotlib`, `seaborn` e `ipykernel`; adicionado `openpyxl`; `pytest` adicionado ao grupo de desenvolvimento; JupyterLab não foi adicionado.
- **Continuidade:** memória operacional definida por `AGENTS.md`, `PROJECT_STATUS.md`, `00_project/TASKS.md`, `00_project/decision_log.md` e `00_project/project_handoff.md`, com detalhes em `00_project/WORKFLOW.md`.
- **Branch:** implementação exclusiva em `integration/project-consolidation`; nenhuma alteração ou merge em `main`.
- **Backup:** `C:\Users\eppin\GLP1_Germany_Final_Project` permanece intacta como backup temporário.
- **Aprovação:** implementação, commit e push da branch explicitamente autorizados pelo usuário.
- **Validação do ambiente:** `uv sync` concluído; imports de pandas 3.0.5, matplotlib 3.11.1, seaborn 0.13.2 e openpyxl 3.1.5 concluídos; Pytest 9.1.1 executado sem testes coletados, sem alegação de validação analítica.

## D-020 — Consolidação RAW local e proteção de publicação

- **Data:** 2026-08-12
- **Tarefa:** F0.11; artefatos parciais relacionados a F2.7/F2.8, sem concluir essas tarefas.
- **Decisão:** copiar RAW byte por byte apenas localmente para a raiz oficial, depois de proteger `01_raw_data/**` no `.gitignore`, e versionar somente README, manifesto e checksums.
- **Integridade:** os dois exports WIdO possuem 556 bytes e o mesmo SHA-256 `05D1667BFE2197C649F3FC7C37A2A2835FEDEE063A88C3C328DF8CEE4E66CCA5`.
- **Duplicação:** ambos permanecem preservados; nenhuma deduplicação, renomeação, transformação ou correção foi realizada. A origem do segundo caminho permanece `not confirmed`.
- **Publicação:** licença e redistribuição WIdO permanecem não confirmadas; ambos os CSVs estão classificados `do_not_publish` e não podem entrar no Git.
- **Limite:** manifesto/checksums cobrem somente os RAW existentes nesta data. F2.7 e F2.8 continuam abertas até cobrir e validar todas as aquisições previstas.
- **Aprovação:** consolidação local e registros públicos de integridade explicitamente autorizados pelo usuário.

## D-021 — Deadline e apresentação final em Power BI

- **Data:** 2026-08-12
- **Tarefa:** governança da entrega final.
- **Decisão:** fixar o deadline final em 2026-08-26 e usar um dashboard interativo em Microsoft Power BI como apresentação final.
- **Processamento:** Python/Pandas permanece responsável pela preparação e validação dos dados analíticos; Power BI deve consumir somente tabelas processadas e validadas.
- **Reconciliação:** métricas, filtros, unidades, denominadores e resultados devem ser reconciliados entre controles Python e Power BI.
- **Transparência:** dados observados e premissas/modelagem devem ser visualmente distinguíveis.
- **Proposta mínima:** visão executiva, tendências observadas, análise de cenários e métodos/limitações, sujeita à disponibilidade dos dados e ao prazo; não se fixa número obrigatório de páginas.
- **Condição:** o planejamento deve preservar tempo suficiente para construção e validação do dashboard.
- **Aprovação:** decisão explicitamente fornecida pelo usuário em 2026-08-12.

## D-022 — Execução integrada F2.2–F2.8 e escopo sistemático WIdO

- **Data:** 2026-08-12
- **Tarefa:** F2.2–F2.8.
- **Decisão:** autorizar a execução operacional integrada de F2.2–F2.8 sem aprovação intermediária; a Fase 3 não pode ser iniciada durante esse bloco.
- **WIdO — período:** 2012–2024.
- **WIdO — escopo:** princípios ativos da classe ATC A10BJ efetivamente disponíveis no PharMaAnalyst; adquirir somente combinações de ano/substância disponibilizadas pelo portal e documentar as indisponíveis.
- **Caminho canônico:** `01_raw_data/wido/pharmaanalyst/year=AAAA/atc=CODIGO_ATC/wirkst_export.csv`.
- **Preservação:** manter os dois arquivos WIdO existentes sem alteração, remoção ou deduplicação.
- **Tirzepatida:** incluir somente como comparador separado se sua inclusão/disponibilidade estiver confirmada; não promover silenciosamente a A10BJ.
- **Publicação:** licença e redistribuição WIdO permanecem não confirmadas; status `do_not_publish`; nenhum RAW pode ser publicado.
- **Próxima ação:** iniciar a execução operacional F2.2, não uma nova rodada decisória, e prosseguir sequencialmente até F2.8 dentro da autorização.
- **Aprovação:** decisão e execução integrada explicitamente autorizadas pelo usuário em 2026-08-12.
