# Status do projeto

Este arquivo registra o progresso do projeto e deve ser atualizado sempre que uma tarefa importante for concluída.

## Última atualização

- Data: 2026-08-13
- Deadline final: 2026-08-26.
- Entrega de apresentação: dashboard interativo em Microsoft Power BI, alimentado por tabelas processadas e validadas em Python/Pandas.
- Status geral: Fases 3 e 4 e a EDA mínima da Fase 5 concluídas `WITH LIMITATIONS` na branch `analysis/powerbi-mvp`. O pacote Power BI descritivo está preparado para montagem manual. F6.2 permanece `TODO / DEFERRED`; cenários econômicos estão `not_calculated` e nenhuma Fase 6–8 foi iniciada.

## Tarefas concluídas

### 35. Auditoria final do pacote Power BI MVP

- Auditoria técnica e analítica confirmou tabelas observadas populadas e reproduzíveis, ausência de tabelas vazias enganosas, sete testes aprovados e oito controles reconciliados.
- Foram corrigidos o código nulo das linhas populacionais `Insgesamt`, metadados insuficientes do dicionário, controles antes auto-referenciais e riscos de contexto em cards DAX.
- A origem RKI foi validada visual e textualmente na Tabela 2, página 6 do PDF oficial.
- Classificação geral: pacote descritivo `READY WITH LIMITATIONS`; cenários `NOT READY` e `not_calculated`; F6.2 continua `TODO / DEFERRED`.
- Relatório completo: `00_project/power_bi_mvp_final_audit.md`.

### 34. Pacote analítico mínimo para Power BI — `READY FOR MANUAL BUILD`

- Os sete RAW locais foram inventariados e tiveram caminho, tamanho e SHA-256 reconciliados com manifesto e checksums; nenhum RAW foi alterado ou adicionado ao Git.
- Um pipeline Python/Pandas reutilizável em `src/final_project_stackfuel/pipeline.py` processa diretamente os dados observados sustentados pelas fontes e produz tabelas finais em `04_outputs/tables/`.
- WIdO contém somente quatro observações transversais de 2024; os dois exports Semaglutida byte-idênticos não foram contados como observações adicionais.
- Foram produzidas dimensões, fatos observados de WIdO, população, obesidade e custos de doença, dicionário, totais de controle, inventário e contrato de cenários. As classes, unidades, denominadores e limitações permanecem explícitas.
- RKI Diabetes continua ausente e sem substituto. População residente não foi rotulada como GKV; custos de doença permanecem todos os pagadores; obesidade não foi tratada como elegibilidade clínica.
- Sete testes automatizados cobrem integridade do inventário, duplicação WIdO, esquemas, chaves, cobertura, intervalos e proibição de resultados de cenário sem parâmetros.
- O pacote `04_outputs/power_bi/` documenta modelo estrela, relacionamentos, cardinalidades, medidas DAX, páginas, KPIs, slicers, avisos, importação e reconciliação. Um `.pbix` não foi criado porque sua montagem e validação exigem ação manual no Power BI Desktop.
- F6.2 permanece adiada. Não há parâmetros clínicos/econômicos aprovados nem net budget impact calculado; a quarta página proposta é `Scenario Framework / Data Gaps`.
- Próxima tarefa única: montar o dashboard no Power BI Desktop a partir do pacote validado e executar o checklist de reconciliação, sem iniciar cenários até decisão específica sobre F6.2.

### 33. Encerramento da Fase 2 — `COMPLETE WITH LIMITATIONS`

- F2.2 foi encerrada com aquisição parcial: dois caminhos byte-idênticos do export Semaglutid/A10BJ06 de 2024 e um export agregado da consulta A10BJ de 2024. O agregado contém linhas para os quatro ingredientes confirmados, mas não equivale a quatro exports individuais. Nenhum ano de 2012 a 2023 foi adquirido; tirzepatida não foi adquirida.
- F2.3 foi encerrada como `BLOCKED / NOT ACQUIRED`: os URLs aprovados redirecionam para a nova área GBE e a tentativa final limitada não localizou os XLSX. O componente permanece contextual e sua ausência não impede a análise nacional central.
- F2.4 permanece concluída com duas publicações oficiais RKI/GEDA.
- F2.5 foi concluída no escopo mínimo nacional com os exports GENESIS `12411-0005` (população por idade, 2021–2025) e `23631-0001` (custos por diagnóstico, 2020 e 2023).
- F2.6 foi concluída com registro mínimo de referências oficiais por URL; nenhum levantamento amplo ou seleção quantitativa de parâmetros clínicos foi realizado.
- F2.7 e F2.8 foram concluídas para o inventário final de sete RAW, com caminhos, tamanhos, SHA-256, duplicata WIdO, licenças e limitações validados.
- Não reabrir WIdO 2012–2023, RKI Diabetes ou busca documental ampla antes da entrega, salvo lacuna indispensável identificada na análise. Próxima tarefa única elegível: F3.1, sem iniciá-la nesta execução.

### 32. Execução parcial do bloco F2.2–F2.8

- O PharMaAnalyst confirmou em 2024 `Exenatid (A10BJ01)`, `Liraglutid (A10BJ02)`, `Dulaglutid (A10BJ05)` e `Semaglutid (A10BJ06)`; tirzepatida não apareceu em A10BJ.
- A exportação sistemática individual WIdO não foi concluída porque a sessão do portal reinicia após cada download e a seleção automatizada individual mostrou-se instável. Nenhum RAW existente foi sobrescrito.
- Os URLs aprovados do RKI Diabetes redirecionam para a nova área GBE; os XLSX legados não foram localizados e nenhuma substituição não aprovada foi feita.
- Duas publicações oficiais RKI/GEDA foram preservadas em `01_raw_data/rki_geda/`, validadas por assinatura PDF, tamanho e SHA-256, e registradas no manifesto e nos checksums.
- Fase 3, F6.2, Power BI, processamento e análise não foram iniciados.

### 31. Atualização da memória operacional com o handoff histórico validado

#### O que foi feito

- Registro do deadline final em 2026-08-26 e do dashboard interativo Power BI como apresentação final.
- Formalização de Python/Pandas como camada de processamento e validação dos dados consumidos pelo Power BI, com reconciliação obrigatória entre as duas ferramentas.
- Autorização do bloco operacional integrado F2.2–F2.8 sem aprovação intermediária e proibição explícita de iniciar a Fase 3 durante sua execução.
- Formalização do escopo WIdO 2012–2024 para princípios ativos ATC A10BJ efetivamente disponíveis e do caminho canônico por ano/código.
- Preservação dos dois RAW WIdO existentes, da classificação `do_not_publish` e da proibição de publicar RAW.
- Atualização exclusivamente documental; nenhuma aquisição, análise, alteração RAW, dependência ou artefato Power BI foi criado.

#### Próxima tarefa operacional

- Executar o bloco integrado F2.2–F2.8 conforme D-022, começando pela aquisição sistemática WIdO já autorizada; documentar combinações indisponíveis e não iniciar Fase 3.
- As referências históricas a decisões ainda pendentes sobre anos, escopo ATC e armazenamento WIdO ficam superadas pela D-022; permanecem preservadas apenas como histórico.

### 30. F0.11 — consolidação definitiva e sistema de continuidade

#### O que foi feito

- Confirmação da raiz Git oficial, remoto, branch `main` limpa e sincronizada com `origin/main` antes da implementação.
- Criação e uso exclusivo da branch `integration/project-consolidation`.
- Cópia da governança e do status da pasta anterior, que permaneceu intacta como backup temporário.
- Proteção de RAW, estudos, documentação restrita, segredos, caches e temporários no `.gitignore`.
- Cópia local byte por byte dos RAW somente após validação do ignore; preservação dos dois arquivos WIdO duplicados.
- Criação de `raw_data_manifest.csv` e `raw_data_checksums.sha256` sem conteúdo dos datasets e com publicação proibida para os CSVs.
- Consolidação do ambiente oficial em UV; remoção de `seeborn`, adição de `openpyxl` e de `pytest` como dependência de desenvolvimento, sem JupyterLab e sem `environment.yml`.
- Criação de `00_project/WORKFLOW.md`, protocolos de novo chat/conclusão e READMEs estruturais.
- Mesclagem do README principal e correção da renderização Markdown do handoff.

#### O que ficou pendente

- F2.2 continua aberta: anos/substâncias da aquisição sistemática e estratégia canônica de armazenamento exigem decisão do usuário.
- Licença e redistribuição dos exports WIdO permanecem não confirmadas; RAW não pode ser publicado.
- F2.7/F2.8 permanecem abertas porque os registros atuais cobrem apenas os RAW existentes, não toda a futura Fase 2.
- Ainda não existem testes ou código analítico substantivo.

#### Validações executadas

- `uv sync`: concluído; 50 pacotes resolvidos e 45 pacotes verificados.
- Imports: `pandas 3.0.5`, `matplotlib 3.11.1`, `seaborn 0.13.2` e `openpyxl 3.1.5` importados com sucesso.
- `uv run pytest`: executado com Python 3.14.2 e Pytest 9.1.1; nenhum teste coletado (`exit 5`), registrado como ausência de testes e não como validação de código analítico.
- Hashes RAW na raiz oficial iguais aos hashes do backup; checksums verificados e manifesto com dois registros `do_not_publish`.
- Links Markdown relativos dos documentos centrais verificados; referências do `AGENTS.md` existem.
- `environment.yml` ausente da raiz oficial; `.venv` e os dois CSVs RAW ignorados e não versionados.

#### Arquivos criados

- `00_project/WORKFLOW.md`
- READMEs das camadas analíticas e protegidas
- `01_raw_data/raw_data_manifest.csv`
- `01_raw_data/raw_data_checksums.sha256`

#### Arquivos modificados

- `.gitignore`, `pyproject.toml`, `uv.lock`, `README.md`, `AGENTS.md`
- `PROJECT_STATUS.md`, `00_project/TASKS.md`, `00_project/decision_log.md`, `00_project/project_handoff.md`, `00_project/setup_guidelines_audit.md`

#### Decisões tomadas

- PASTA A é a única raiz oficial; PASTA B permanece backup temporário intacto.
- UV substitui formalmente Conda/Mamba como única fonte de verdade do ambiente.
- RAW permanece local, ignorado e não publicável; somente README, manifesto e checksums podem ser versionados.
- `main` não foi alterada; a consolidação pertence exclusivamente à branch de integração.

#### Próxima tarefa recomendada

- Executar somente a decisão e conclusão da F2.2: definir o escopo WIdO por anos/substâncias e a estratégia canônica de armazenamento, sem alterar os RAW já preservados.

### 29. F0.10 — instruções permanentes e auditoria de setup/diretrizes

#### O que foi feito

- Leitura integral do guia oficial StackFuel, dos documentos de governança solicitados, das configurações existentes e da estrutura completa disponível.
- Criação de `AGENTS.md` como entrada concisa para regras permanentes, com referências aos documentos detalhados.
- Criação de `00_project/setup_guidelines_audit.md`, classificando divergências de `CRITICAL` a `LOW`.
- Tratamento explícito do conflito entre UV/`pyproject.toml` e Conda/Mamba/`environment.yml`, sem escolher, migrar ou manter silenciosamente dois sistemas concorrentes.
- Verificação read-only da estrutura e dos dois arquivos RAW WIdO; nenhum conteúdo RAW foi alterado.

#### O que ficou pendente

- Resolver as divergências somente em tarefas futuras autorizadas, começando pela confirmação da raiz Git e pela decisão única sobre o sistema de ambiente.
- O diretório atual não foi reconhecido como repositório Git; por isso não foi possível comparar as alterações com um baseline Git.
- F2.2 permanece `IN PROGRESS`; nenhuma tarefa analítica ou aquisição adicional foi iniciada.

#### Arquivos criados

- `AGENTS.md`
- `00_project/setup_guidelines_audit.md`

#### Arquivos modificados

- `00_project/TASKS.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Não implementar nenhuma correção da auditoria nesta tarefa.
- Não criar `pyproject.toml`, `.gitignore`, lockfile, diretórios de código/testes ou manifesto/checksums.
- Não mover, renomear, remover ou reconciliar as duas cópias RAW detectadas.

#### Próxima tarefa recomendada

- Confirmar a raiz e o histórico Git do projeto. Depois, em tarefa separada e única, decidir formalmente entre o padrão StackFuel com UV e a exceção Conda/Mamba já aprovada; não executar a migração durante a decisão.

### 28. Execução parcial da F2.2 — aquisição e preservação dos dados WIdO

#### O que foi feito

- Leitura dos documentos internos obrigatórios diretamente aplicáveis à aquisição WIdO.
- Verificação da identidade institucional do PharMaAnalyst / GKV-Arzneimittelindex no portal e na página documental oficial do WIdO.
- Confirmação de acesso público sem login, cobertura selecionável de 2012 a 2024 e atualização do portal em 07.10.2025 com dados de 2024.
- Confirmação operacional de que o portal gera exportação CSV por ano e consulta, com nome original `wirkst_export.csv`.
- Aquisição controlada de uma exportação oficial para `Semaglutid (A10BJ06)`, ano 2024, com prescrições, DDD, custos líquidos, custos líquidos por prescrição e custos líquidos por DDD.
- Preservação do arquivo original, sem alteração, em `01_raw_data/wido/wirkst_export.csv`.
- Validação mínima de existência, caminho, nome, extensão, tamanho de 556 bytes, assinatura textual compatível com CSV delimitado por ponto e vírgula e ausência de início HTML de erro.
- Registro da execução parcial na decisão D-018.
- Nenhum dado foi analisado e nenhuma contagem de linhas, inspeção de esquema ou validação de valores foi realizada.

#### O que ficou pendente

- Definir explicitamente quais combinações de anos e substâncias devem integrar a aquisição sistemática do WIdO.
- Definir uma estratégia aprovada para preservar múltiplos exports que reutilizam o mesmo nome original `wirkst_export.csv`, sem sobrescrita e com rastreabilidade.
- Confirmar licença específica e condições de redistribuição do arquivo exportado; o portal informa `Alle Rechte vorbehalten`, e acesso público não foi tratado como licença aberta.
- Concluir a aquisição somente após decisão do usuário; a F2.2 permanece `IN PROGRESS` e não foi marcada como tecnicamente concluída.
- Manifesto e checksums permanecem reservados para tarefa posterior autorizada.

#### Arquivos criados

- `01_raw_data/wido/wirkst_export.csv`

#### Arquivos modificados

- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Preservar a exportação oficial de teste como RAW por corresponder documentalmente ao componente `WIDO-PMA` aprovado condicionalmente.
- Interromper a aquisição antes de escolher silenciosamente anos, substâncias ou uma convenção de armazenamento para arquivos homônimos.
- Manter a decisão geral `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`, sem promoção para `GO`.
- Manter todas as limitações do WIdO: universo ambulatorial GKV, ausência de privado/self-pay/hospitalar, ausência de indicação clínica e potencial variação anual de ATC e cobertura.

#### Próxima tarefa recomendada

- Obter decisão do usuário sobre o escopo sistemático da F2.2 e a estratégia de preservação de múltiplos exports homônimos. Nenhuma outra tarefa deve ser iniciada automaticamente.

### 27. Aprovação formal da F2.1 — lista final de datasets

#### O que foi feito

- Registro da aprovação formal, em 2026-08-11, da seção 13 do `00_project/data_feasibility_map.md` como lista documental final para futura aquisição.
- Preservação da data da execução técnica em 2026-08-11 e atualização do status final da F2.1 para `DONE`.
- Atualização mínima dos trechos de status da seção 13, sem alterar tabelas, componentes ou classificações.
- Atualização da decisão D-017 sem criação de decisão duplicada.
- Preservação integral das categorias `APPROVED`, `CONDITIONALLY APPROVED`, `PENDING DECISION` e `NOT APPROVED`, bem como de suas condições, limitações, riscos e informações pendentes.
- Confirmação de que a Fase 1 permanece encerrada e a decisão geral permanece `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`.
- Confirmação de que a etapa operacional da Fase 2 permanece não iniciada, sem datasets na camada RAW.
- Confirmação de que F2.2–F2.6 e F6.2 permanecem `TODO` e não foram iniciadas.
- Nenhum download, aquisição, acesso operacional, dado, diretório RAW, manifesto, checksum, instalação, código, teste, análise, seleção de evidência ou modelagem foi executado.

#### O que ficou pendente

- Cada tarefa F2.2–F2.6 exige autorização específica antes de qualquer aquisição.
- Componentes `PENDING DECISION` permanecem não autorizados e componentes `NOT APPROVED` permanecem rejeitados.
- Formatos, esquemas, períodos, licenças, versões e métodos de acesso identificados como pendentes continuam não confirmados.
- F6.2 permanece `TODO` e exige autorização específica.
- O ambiente permanece não instalado, não resolvido e não validado; nenhum lockfile foi criado.
- O `README.md` contém referências históricas desatualizadas sobre F0.9 e F6.1; essa dívida documental não foi corrigida por estar fora do escopo desta formalização.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- `00_project/data_feasibility_map.md`
- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Considerar a F2.1 formalmente concluída em 2026-08-11.
- Limitar a aprovação à lista documental e às finalidades registradas.
- Não interpretar a aprovação como autorização automática para aquisição ou uso analítico.
- Exigir justificativa, data e versionamento para qualquer alteração posterior da lista ou classificação.
- Manter a decisão geral `CONDITIONAL GO`, sem promoção para `GO`.

#### Próxima tarefa recomendada

- Aguardar autorização específica do usuário para uma das tarefas elegíveis, sem selecionar ou iniciar automaticamente qualquer delas.

### 26. Conclusão técnica da F2.1 — lista final de datasets

#### O que foi feito

- Identificação da D-011 e de sua lista operacional aprovada como entregável da F1.10.
- Identificação de `00_project/raw_data_manifest_template.md` como entregável da F0.7.
- Revisão exclusivamente documental das avaliações e decisões existentes, sem consulta externa.
- Inclusão da seção 13 no `00_project/data_feasibility_map.md`, com a lista final de aquisição e as categorias `APPROVED`, `CONDITIONALLY APPROVED`, `NOT APPROVED` e `PENDING DECISION`.
- Registro de finalidade, cobertura, acesso, condições, limitações e riscos documentados para cada componente.
- Normalização das decisões funcionais da Fase 1 para categorias de aquisição, sem promover usos proibidos.
- Atualização da F2.1 para `IN PROGRESS — execução técnica concluída, aguardando aprovação formal`.
- Registro da execução técnica na decisão D-017.
- Nenhum download, acesso operacional, aquisição, dado, diretório RAW, checksum, código, instalação, teste, análise, integração ou modelagem foi executado.

#### O que ficou pendente

- Obter aprovação formal da F2.1 antes de qualquer download.
- Confirmar, em cada tarefa futura autorizada, arquivo, formato, período, esquema, licença/termos, versão e método de acesso.
- F2.2 e todas as tarefas operacionais de aquisição permanecem bloqueadas.
- F6.2 permanece `TODO` e não foi iniciada.
- O ambiente permanece não instalado, não resolvido e não validado.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- `00_project/data_feasibility_map.md`
- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Aprovar tecnicamente apenas a lista documental candidata, sem autorizar aquisição.
- Manter a decisão geral `CONDITIONAL GO`, sem promoção para `GO`.
- Tratar acesso público, acesso operacional e autorização de reutilização como conceitos distintos.
- Manter componentes clínicos específicos pendentes até F6.2 e GKV-GAmSi pendente de feasibility própria.
- Não adquirir componentes `PENDING DECISION` ou `NOT APPROVED` sem nova decisão.

#### Próxima tarefa recomendada

- Aguardar aprovação formal da F2.1. Não iniciar F2.2, F6.2 ou qualquer outra tarefa sem autorização específica.

### 25. Aprovação formal da F6.1 — critérios de inclusão das evidências

#### O que foi feito

- Registro da aprovação formal de `00_project/evidence_inclusion_criteria.md` como protocolo para futura seleção de evidências clínicas e econômicas.
- Preservação da data da execução técnica em 2026-08-11 e registro da aprovação formal em 2026-08-11.
- Atualização da F6.1 de `IN PROGRESS` para `DONE` no backlog.
- Atualização da decisão D-016, sem criação de decisão duplicada.
- Confirmação de que a aprovação está limitada à versão atual do protocolo documental.
- Preservação explícita das decisões metodológicas ainda pendentes.
- Confirmação de que a Fase 1 permanece formalmente encerrada com decisão `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE` e de que a Fase 2 permanece não iniciada.
- Confirmação de que F2.1 e F6.2 permanecem `TODO` e não foram iniciadas.
- Nenhuma busca, triagem, seleção, deduplicação, extração, avaliação de evidência, download, instalação, resolução, validação, checksum, código, notebook, teste, análise ou modelagem foi executada.

#### O que ficou pendente

- F2.1 permanece `TODO` e exige autorização específica antes de qualquer download.
- F6.2 permanece `TODO` e exige autorização específica antes da seleção de fontes.
- F6.3, F6.4 e F6.7 permanecem bloqueadas pelas dependências registradas no backlog.
- Estratégia de busca, bases, strings, idioma, período, revisores, ferramentas metodológicas e elementos do futuro modelo econômico permanecem pendentes.
- O ambiente técnico permanece não instalado, não resolvido e não validado; nenhum lockfile foi criado.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Considerar a F6.1 formalmente concluída em 2026-08-11.
- Limitar a aprovação à versão atual do protocolo documental.
- Exigir justificativa, data e versionamento para qualquer alteração posterior dos critérios.
- Não interpretar a aprovação como autorização para F6.2, F2.1 ou qualquer outra atividade.
- Manter a decisão consolidada como `CONDITIONAL GO`, sem promoção para `GO`.

#### Próxima tarefa recomendada

- Aguardar autorização específica do usuário para F2.1 ou F6.2, sem selecionar automaticamente entre as duas tarefas elegíveis.

### 24. Conclusão técnica da F6.1 — critérios de inclusão das evidências

#### O que foi feito

- Identificação de `00_project/feasibility/ema_clinical_evidence.md` como entregável aprovado da F1.8.
- Criação de `00_project/evidence_inclusion_criteria.md` como protocolo proporcional para futura seleção de evidências clínicas e econômicas.
- Definição de estrutura por finalidade do parâmetro, tipos de evidência, critérios de inclusão e exclusão, hierarquia de fontes, transferibilidade, avaliação futura de qualidade, duplicatas, processo de seleção, rastreabilidade, casos incertos e controle de mudanças.
- Separação explícita entre busca estruturada, revisão sistemática formal, seleção de parâmetros e uso contextual de fontes secundárias.
- Preservação da prioridade das fontes oficiais alemãs sem transformar prioridade em exclusividade para evidência clínica.
- Registro de decisões ainda pendentes, incluindo estratégia de busca, período, idioma, revisores, ferramentas metodológicas e elementos do modelo econômico.
- Atualização da F6.1 para `IN PROGRESS — execução técnica concluída, aguardando aprovação formal`.
- Registro da execução técnica na decisão D-016.
- Nenhuma busca, triagem, seleção, extração, avaliação de estudo, download, instalação, resolução, validação, checksum, código, notebook, teste, análise ou modelagem foi executada.

#### O que ficou pendente

- Obter aprovação formal dos critérios antes de qualquer extração.
- F6.2 e todas as tarefas dependentes da F6.1 permanecem bloqueadas.
- F2.1 permanece `TODO` e não foi iniciada.
- Instalação, resolução, lockfile e validação do ambiente permanecem pendentes.

#### Arquivos criados

- `00_project/evidence_inclusion_criteria.md`

#### Arquivos modificados

- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Usar estrutura de evidência por finalidade do parâmetro, sem declarar PICO único ou revisão sistemática formal.
- Exigir correspondência e rastreabilidade de população, intervenção, comparador, outcome, desenho, horizonte e finalidade.
- Priorizar fontes alemãs para custos e contexto, admitindo evidência clínica internacional com avaliação explícita de transferibilidade.
- Manter elegibilidade, qualidade, risco de viés, aplicabilidade, transferibilidade e força da evidência como avaliações distintas.
- Não adotar nesta etapa ferramentas específicas de avaliação metodológica.
- Classificar casos insuficientes como incertos, sem forçar decisão binária.

#### Próxima tarefa recomendada

- Aguardar aprovação formal da F6.1. Não iniciar F6.2, F2.1 ou qualquer outra tarefa sem autorização específica.

### 23. Aprovação formal da F0.9 — visão geral inicial do projeto

#### O que foi feito

- Registro da aprovação formal do conteúdo atual do `README.md` como visão geral inicial do projeto.
- Preservação da data da execução técnica da F0.9 em 2026-08-10.
- Registro da aprovação formal em 2026-08-11.
- Atualização da F0.9 de `IN PROGRESS` para `DONE` no backlog.
- Atualização da decisão D-015 sem criação de decisão duplicada.
- Confirmação de que a Fase 1 permanece formalmente encerrada com decisão `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`.
- Confirmação de que a Fase 2 permanece não iniciada e de que F2.1 e F6.1 permanecem `TODO`.
- Nenhuma tarefa seguinte, instalação, resolução, lockfile, validação, download, aquisição, alteração de dados, checksum, código, notebook, importação, teste ou análise foi executada.

#### O que ficou pendente

- F2.1 permanece `TODO` e exige autorização específica antes de qualquer download.
- F6.1 permanece `TODO` e exige autorização específica antes da extração de evidências.
- Instalação, resolução, criação de lockfile e validação do ambiente permanecem pendentes e exigem autorização própria.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Considerar a F0.9 formalmente concluída em 2026-08-11.
- Limitar a aprovação ao conteúdo documental atual do `README.md`.
- Não interpretar a aprovação como autorização implícita para F2.1, F6.1 ou qualquer outra tarefa.
- Manter a decisão consolidada da Fase 1 como `CONDITIONAL GO`, sem promoção para `GO`.

#### Próxima tarefa recomendada

- Aguardar autorização específica do usuário para F2.1 ou F6.1, sem selecionar automaticamente entre as duas tarefas elegíveis.

### 22. Conclusão técnica da F0.9 — visão geral inicial do projeto

#### O que foi feito

- Preenchimento do `README.md`, que existia vazio, como ponto de entrada factual e navegável do repositório.
- Documentação do problema, objetivos, escopo, perguntas de pesquisa, princípios metodológicos, status real, estrutura, ambiente técnico, governança, fluxo planejado e próximos passos.
- Inclusão de links relativos para os principais documentos de controle do projeto.
- Preservação da decisão consolidada `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE` e da distinção entre dados observados e elementos modelados.
- Atualização da F0.9 para `IN PROGRESS — execução técnica concluída, aguardando aprovação formal`.
- Registro da execução técnica na decisão D-015.
- Nenhuma pesquisa, instalação, resolução, validação, importação, teste, download, código, notebook, dataset, checksum ou tarefa da Fase 2 foi executada.

#### O que ficou pendente

- Obter aprovação formal do usuário para marcar a F0.9 como `DONE`.
- Instalação, resolução, lockfile e validação do ambiente permanecem pendentes e exigem autorização própria.
- F2.1 e F6.1 permanecem `TODO`, embora suas dependências documentais estejam satisfeitas.
- A Fase 2 permanece não iniciada e nenhum dataset foi baixado.

#### Arquivos criados

- Nenhum. O `README.md` já existia vazio.

#### Arquivos modificados

- `README.md`
- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Usar o README como visão geral inicial, sem duplicar ou substituir os documentos de governança e metodologia.
- Não apresentar pastas reservadas como evidência de entregáveis já produzidos.
- Não apresentar resultados, conclusões econômicas, aquisições ou reprodutibilidade como concluídos.
- Manter F0.9 em `IN PROGRESS` até aprovação formal.
- Não escolher nem iniciar F2.1 ou F6.1 sem autorização específica.

#### Próxima tarefa recomendada

- Aguardar a aprovação formal da F0.9. Após a formalização, F2.1 e F6.1 continuarão documentalmente elegíveis, sem escolha automática entre elas.

### 21. Aprovação formal da F0.8 e identificação das tarefas elegíveis

#### O que foi feito

- Confirmação de que `environment.yml` corresponde exatamente à especificação formalmente aprovada.
- Registro da aprovação formal da F0.8 em 2026-08-10 na decisão D-014.
- Atualização da F0.8 de `IN PROGRESS` para `DONE`.
- Confirmação de que F0.6 e F0.7 permanecem `DONE`.
- Confirmação de que a Fase 1 permanece formalmente encerrada com decisão `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`.
- Verificação das dependências do backlog após a conclusão da F0.8.
- Identificação de F0.9, F2.1 e F6.1 como tarefas documentalmente elegíveis.
- Manutenção das três tarefas como `TODO`, sem escolha ou início.
- Nenhuma instalação, resolução, ativação de ambiente, lockfile, importação, teste, código, notebook, dataset ou RAW foi executado/criado. Durante a validação documental, foi calculado inadvertidamente um SHA-256 transitório de `environment.yml`; o valor não foi persistido e nenhum arquivo de checksum ou checksum RAW foi criado.

#### O que ficou pendente

- Instalação, resolução e validação do ambiente permanecem pendentes e exigem autorização própria.
- Eventual lockfile somente poderá ser criado após resolução e validação autorizadas.
- O usuário deverá escolher e autorizar especificamente uma das tarefas elegíveis antes de qualquer execução.
- Fase 2 permanece não iniciada.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Considerar F0.8 formalmente concluída em 2026-08-10.
- Manter `environment.yml` como especificação declarativa ainda não resolvida nem testada.
- Não escolher arbitrariamente entre F0.9, F2.1 e F6.1, pois todas possuem dependências satisfeitas segundo o backlog.
- Não iniciar a Fase 2 nem qualquer outra tarefa sem autorização específica.
- Registrar como desvio de validação o cálculo transitório e não persistido de SHA-256 de `environment.yml`, sem impacto no conteúdo do arquivo.

#### Próxima tarefa recomendada

- Aguardar o usuário selecionar e autorizar uma das tarefas elegíveis: F0.9, F2.1 ou F6.1.

### 20. Conclusão técnica da F0.8 com Python 3.14

#### O que foi feito

- Criação de uma única especificação declarativa em `environment.yml`.
- Definição do ambiente Conda/Mamba com nome `glp1_germany`.
- Definição de `conda-forge` como canal exclusivo, seguida de `nodefaults`.
- Definição de `python=3.14` como requisito externo do curso, sem fixar o patch 3.14.2.
- Inclusão somente das dependências diretas autorizadas: Pandas, OpenPyXL, Matplotlib, Seaborn, JupyterLab e Pytest.
- Atualização da decisão D-014 com justificativa, dependências, reprodutibilidade, lockfile, segurança e limitações.
- Nenhum gerenciador foi executado, nenhum pacote foi instalado e nenhum ambiente foi criado ou ativado.

#### O que ficou pendente

- Obter aprovação formal do usuário para a F0.8.
- Confirmar futuramente a compatibilidade efetiva entre Python 3.14 e as dependências durante resolução e validação autorizadas.
- Resolver versões transitivas e eventualmente gerar lockfile somente em tarefa futura autorizada.
- Testar criação do ambiente e imports somente após autorização.
- Fase 2 permanece não iniciada.

#### Arquivos criados

- `environment.yml`

#### Arquivos modificados

- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Python 3.14 é a versão-alvo por exigência do curso, não por disponibilidade local.
- Usar `python=3.14`, permitindo que o patch seja resolvido futuramente dentro da linha 3.14.
- Usar Conda/Mamba, `conda-forge` e `nodefaults`.
- Não incluir dependências opcionais ou especulativas.
- Separar especificação declarativa de ambiente resolvido e testado.
- Manter F0.8 como `IN PROGRESS` até aprovação formal.

#### Próxima tarefa recomendada

- Aguardar aprovação formal da F0.8. Nenhuma outra tarefa deve ser iniciada.

### 19. Aprovação formal da F0.6 e verificação técnica inicial da F0.8

#### O que foi feito

- Registro da aprovação formal da F0.6 em 2026-08-10.
- Atualização da F0.6 de `IN PROGRESS` para `DONE`.
- Confirmação de que F0.7 permanece `DONE`, a Fase 1 permanece encerrada e a decisão continua `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`.
- Leitura integral dos documentos de governança e ambiente autorizados.
- Verificação de inexistência de `environment.yml`, `pyproject.toml`, requirements, lockfile ou outra especificação anterior.
- Confirmação de `environment.yml` como entregável nominal no backlog, sem evidência adicional de canal Conda aprovado.
- Verificação local de Python 3.14.2.
- Verificação de que Pandas, OpenPyXL, JupyterLab, Matplotlib, Seaborn, Pytest e PyYAML não estão instalados no runtime local consultado.
- Identificação das decisões necessárias antes de criar uma especificação defensável: versão-alvo do Python, mecanismo Conda/Mamba, canal e política de constraints.
- Nenhum gerenciador foi executado, nenhum pacote foi instalado e nenhum ambiente ou lockfile foi criado.

#### O que ficou pendente

- Aprovar a versão-alvo do Python. A versão local 3.14.2 foi verificada, mas sua compatibilidade com o conjunto necessário não foi validada.
- Confirmar se `environment.yml` deverá usar Conda/Mamba.
- Aprovar o canal autorizado para resolução de pacotes.
- Definir pins exatos ou intervalos para dependências diretas na especificação inicial.
- Após essas decisões, definir somente dependências justificadas e separar runtime, desenvolvimento, opcionais e ferramentas externas.
- Instalação, resolução, lockfile e teste do ambiente permanecem não autorizados e pendentes.
- Fase 2 permanece não iniciada.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Considerar F0.6 formalmente concluída em 2026-08-10.
- Não criar `environment.yml` especulativo sem versão do Python, canal e política de versões defensáveis.
- Não tratar o Python local 3.14.2 como versão-alvo aprovada apenas por estar instalado.
- Não adicionar pacotes por precaução nem transformar formatos condicionais futuros em dependências obrigatórias atuais.
- Manter F0.8 como `IN PROGRESS` até decisão técnica do usuário e posterior conclusão da especificação.

#### Próxima tarefa recomendada

- Resolver exclusivamente as decisões pendentes da F0.8; nenhuma outra tarefa deve ser iniciada.

### 18. Aprovação formal da F0.7 e execução técnica da F0.6

#### O que foi feito

- Registro da aprovação formal da F0.7 em 2026-08-10.
- Atualização da F0.7 de `IN PROGRESS` para `DONE`.
- Preservação do manifesto RAW aprovado e do mapeamento entre formas documentais e técnicas das decisões de feasibility.
- Criação das convenções de nomes, versões, datas, timestamps, identificadores, camadas e artefatos.
- Definição de nomes técnicos em inglês, `snake_case`, transliteração, siglas, unidades e termos proibidos/ambíguos.
- Separação explícita entre publicação, revisão, acesso, download, snapshot e período de referência.
- Definição de ISO 8601, timestamps com segundos e fuso, UTC com `Z` e datas parciais sem preenchimento por inferência.
- Definição de versionamento interno e do publicador, revisões, republicações, snapshots, suplementos, documentação e mudanças silenciosas por checksum.
- Harmonização de `manifest_record_id`, `dataset_id`, `source_id`, componentes, versões, nomes armazenados e caminhos relativos.
- Documentação somente das camadas existentes ou previstas no backlog; `staging` e `curated` não foram criadas/aprovadas.
- Mapeamento explícito entre `CONDITIONAL GO`/`CONDITIONAL_GO`, `CONTEXTUAL ONLY`/`CONTEXTUAL_ONLY`, `NO-GO`/`NO_GO` e demais valores aprovados.
- Validação de compatibilidade integral com `00_project/raw_data_manifest_template.md`.
- Nenhum arquivo existente foi renomeado e nenhum dado, código, checksum ou tarefa da Fase 2 foi criado/executado.

#### O que ficou pendente

- Obter aprovação formal do usuário para a F0.6.
- Aplicar as convenções somente em tarefas futuras autorizadas, sem renomear retroativamente arquivos existentes por padrão.
- Definir ambiente e dependências em F0.8 somente após autorização.
- Fase 2 permanece não iniciada.

#### Arquivos criados

- `00_project/data_conventions.md`

#### Arquivos modificados

- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Considerar F0.7 formalmente concluída e aprovada em 2026-08-10.
- Usar inglês e `snake_case` nos novos nomes técnicos controlados.
- Usar ISO 8601 e preservar precisão, timezone e significado de cada tipo de data.
- Separar versão declarada pelo publicador de versão interna; data de download nunca substitui versão externa.
- Proibir sobrescrita de versões anteriores e nomes ambíguos como `final`, `latest`, `new`, `old` e `fixed` sem definição.
- Manter `original_filename` separado do nome operacional.
- Manter formas técnicas e documentais como representações equivalentes, não novas classificações.
- Manter F0.6 como `IN PROGRESS` até aprovação formal.

#### Próxima tarefa recomendada

- Após aprovação da F0.6 e autorização específica, executar F0.8: definir ambientes e dependências. Não iniciar automaticamente.

### 17. Aprovação formal da F1.10, encerramento da Fase 1 e execução técnica da F0.7

#### O que foi feito

- Registro da aprovação formal da F1.10 em 2026-08-10.
- Atualização da F1.10 de `IN PROGRESS` para `DONE`.
- Encerramento formal da Fase 1 com decisão `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`.
- Preservação integral das classificações funcionais, limitações e lacunas aprovadas.
- Criação do template obrigatório de manifesto de arquivos RAW.
- Definição de campos para identificação, aquisição, arquivo, integridade, temporalidade, cobertura, esquema, controle RAW, validação inicial, relação com o projeto e auditoria.
- Definição de convenções estáveis para IDs, nomes armazenados e caminhos relativos RAW, sem criar diretórios.
- Definição de SHA-256 como algoritmo principal obrigatório e do fluxo de geração, verificação, divergência e quarentena.
- Definição de imutabilidade, cadeia de custódia e versionamento sem sobrescrita.
- Definição de vocabulários controlados e de formatos Markdown/tabular futuro.
- Inclusão de um único exemplo fictício explicitamente identificado como não adquirido.
- Nenhum download, checksum real, diretório RAW, código, ingestão, transformação ou análise foi criado/executado.

#### O que ficou pendente

- Obter aprovação formal do usuário para a F0.7.
- Implementar o manifesto operacional somente em tarefa futura autorizada.
- Preencher metadados, calcular checksums e validar arquivos somente após aquisições autorizadas.
- Permanecem abertas as lacunas de self-pay, pacientes autofinanciados, população clinicamente apropriada/coberta, indicação observada, participação GKV nos custos, T2D agregado, fração evitável, uptake, adesão, persistência, efetividade alemã, pacientes tratados e projeções epidemiológicas não publicadas.
- Fase 2 permanece não iniciada.

#### Arquivos criados

- `00_project/raw_data_manifest_template.md`

#### Arquivos modificados

- `00_project/TASKS.md`
- `00_project/decision_log.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Manter a decisão final da Fase 1 como `CONDITIONAL GO`, sem promoção para `GO` irrestrito.
- Considerar a F1.10 concluída e a Fase 1 formalmente encerrada em 2026-08-10.
- Usar SHA-256 como mecanismo principal obrigatório; MD5 e SHA-1 não serão mecanismos principais.
- Proibir sobrescrita, correção manual ou substituição silenciosa de arquivos RAW.
- Bloquear processamento quando houver divergência de integridade e exigir quarentena lógica e registro do incidente.
- Tratar novas publicações, revisões, snapshots e substituições na origem como novos registros/versionamentos.
- Manter F0.7 como `IN PROGRESS` até aprovação formal do usuário.

#### Próxima tarefa recomendada

- Após aprovação da F0.7 e autorização específica, executar F0.6: definir convenções de nomes, versões e datas. Não iniciar automaticamente.

### 16. F1.10 — Decisão consolidada de feasibility por fonte e função

#### O que foi feito

- Formalização das decisões operacionais consolidadas por dataset, componente de evidência e função analítica.
- Criação da lista operacional aprovada com instituição, natureza da evidência, decisão, funções aprovadas/proibidas, condições, limitações, arquivo de origem e aprovação.
- Separação dos componentes em uso direto delimitado, uso condicionado, contexto apenas, NO-GO e não disponível/dependente de fonte adicional.
- Preservação das classificações gerais e funcionais aprovadas em F1.2–F1.9.
- Emissão da decisão final proposta `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`.
- Registro separado dos módulos com base observada/oficial, harmonização, evidência contextual, `derived calculations`, `modelled assumptions` e NO-GO.
- Registro das condições e dos limites de autorização para a fase seguinte.
- Validação de que o Data Feasibility Map permanece artefato de governança, não fonte empírica.
- Nenhuma pesquisa, download, cálculo, join, código, nova avaliação de fonte ou tarefa da Fase 2 foi executada.

#### O que ficou pendente

- Obter aprovação formal do usuário para a decisão proposta e para o encerramento da Fase 1.
- Após aprovação específica, concluir F0.7 antes da aquisição: padrão do manifesto e checksums RAW.
- Executar e aprovar F2.1 antes de qualquer download.
- Manter abertas as lacunas de self-pay, indicação observada, pacientes, uptake, adesão, persistência, efetividade real, participação GKV nos custos, T2D, fração evitável e projeções não publicadas.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- `00_project/decision_log.md`
- `00_project/TASKS.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Propor `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`, porque existe base suficiente para preparação e ingestão controlada, mas módulos centrais permanecem condicionais, contextuais ou indisponíveis.
- Manter Destatis Demographics como `GO` para denominador e EMA como `GO` exclusivamente para função regulatória.
- Manter RKI/GEDA, WIdO, Destatis Disease Costs e evidências clínicas como `CONDITIONAL GO` nos respectivos papéis.
- Manter RKI Diabetes, GKV-GAmSi, IQVIA pública contextual e persistência clínica de longo prazo como contexto apenas.
- Manter dataset público IQVIA reproduzível, quantificação pública self-pay e comparação bruta entre ensaios como `NO-GO` para os usos pretendidos.
- Não autorizar download, ingestão, cálculo, modelagem ou início automático da Fase 2.
- Manter F1.10 como `IN PROGRESS` até aprovação formal do usuário.

#### Próxima tarefa recomendada

- Após aprovação formal da F1.10 e autorização específica, executar F0.7: definir o padrão do manifesto e checksums RAW. Não iniciar automaticamente.

### 15. Reconciliação da governança documental e conclusão da F0.5

#### O que foi feito

- Verificação interna do `TASKS.md`, do `PROJECT_STATUS.md`, dos documentos de governança, do Data Feasibility Map e dos entregáveis aprovados de F1.1–F1.9.
- Confirmação da existência de todos os entregáveis de F1.1–F1.9.
- Atualização de F0.4 para `DONE`, em conformidade com a aprovação do backlog.
- Atualização de F1.1–F1.9 para `DONE`, em conformidade com a execução e as aprovações registradas.
- Correção do entregável da F1.4 para `00_project/feasibility/rki_obesity_geda.md`.
- Criação do registro formal de decisões previsto pela F0.5.
- Registro conciso das decisões aprovadas de governança, template, avaliações F1.2–F1.8 e consolidação F1.9.
- Inclusão de F0.5 como dependência operacional explícita da F1.10.
- Atualização da próxima tarefa proposta para F1.10, mantida como `TODO`.
- Nenhuma pesquisa, download, reavaliação de fonte ou decisão final da Fase 1 foi realizada.

#### O que ficou pendente

- Obter autorização do usuário antes de iniciar a F1.10.
- Na F1.10, registrar as decisões formais consolidadas por dataset e a lista aprovada de datasets.
- Encerrar a Fase 1 somente após a execução e aprovação da F1.10.

#### Arquivos criados

- `00_project/decision_log.md`

#### Arquivos modificados

- `00_project/TASKS.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Considerar F0.4 concluída porque o backlog foi criado, revisado e aprovado.
- Considerar F0.5 concluída porque seu entregável formal foi criado com estrutura rastreável e somente decisões explicitamente aprovadas.
- Preservar as classificações gerais e funcionais já aprovadas, sem emitir uma nova decisão final por dataset.
- Manter F1.10 pendente e não iniciada.
- Registrar a dependência operacional de F1.10 em relação a F1.9 e F0.5.

#### Próxima tarefa recomendada

- Após autorização explícita, executar somente F1.10: registrar a decisão GO/NO-GO por dataset, produzir a lista aprovada de datasets e submeter o encerramento da Fase 1 à aprovação do usuário.

### 14. F1.9 — Consolidação do Data Feasibility Map

#### O que foi feito

- Criação do mapa consolidado das fontes aprovadas em F1.2–F1.8.
- Consolidação separada de WIdO/PharMaAnalyst, GKV-GAmSi, RKI Diabetes, RKI Obesity/GEDA agregado e SUF, Destatis Disease Costs, Destatis Demographics corrente e projetado, fontes públicas IQVIA, contexto regulatório alemão, EMA e ensaios clínicos.
- Registro de população/mercado coberto, período, granularidade, métricas, unidades, formatos, acesso, natureza da evidência, classificação, papel analítico e arquivo interno de origem.
- Criação das matrizes de cobertura funcional, acessibilidade, chaves de integração e compatibilidade entre fontes.
- Separação explícita entre dados administrativos, dados de survey, estimativas oficiais, projeções oficiais, painéis projetados, evidência regulatória, ensaios clínicos, cálculos derivados e `modelled assumptions`.
- Consolidação de limitações, lacunas críticas e regras operacionais para aquisição e análise futuras.
- Validação da presença e rastreabilidade de todas as avaliações F1.2–F1.8.
- Nenhuma pesquisa externa, download, cálculo, join, análise, código ou nova decisão por dataset foi realizado.

#### O que ficou pendente

- Obter aprovação do usuário para o mapa consolidado.
- Executar F1.10 somente após autorização, registrando a decisão formal consolidada por dataset e encerrando a Fase 1.
- Em etapas posteriores autorizadas, confirmar formatos e esquemas ainda desconhecidos, obter acesso a microdados quando necessário e definir as harmonizações antes de combinar fontes.
- Resolver futuramente a dívida documental do `TASKS.md`, sem correção nesta tarefa.

#### Arquivos criados

- `00_project/data_feasibility_map.md`

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Preservar integralmente as classificações globais e funcionais aprovadas nas avaliações individuais.
- Não tratar fontes contextuais como datasets quantitativos completos.
- Manter WIdO/PharMaAnalyst como fonte de utilização e despesa ambulatorial reembolsada pelo GKV, sem inferir indicação ou mercado total.
- Manter RKI/GEDA como baseline epidemiológico oficial de obesidade, Destatis Demographics como denominador oficial e Destatis Disease Costs como baseline econômico oficial nacional.
- Manter RKI Diabetes e IQVIA em papéis contextuais aprovados.
- Restringir parâmetros clínicos às populações, doses, estimandos e horizontes correspondentes.
- Reservar a decisão formal consolidada da Fase 1 para a F1.10.
- Registrar GKV-GAmSi apenas como fonte complementar, pois não foi avaliada como substituta para séries por princípio ativo.
- Não criar um registro independente para “Arzneimittel-Kompass”, pois esse nome não corresponde a uma avaliação separada nos arquivos aprovados da F1.2.

#### Próxima tarefa recomendada

- Após aprovação do usuário, executar exclusivamente F1.10: registrar a decisão formal GO/NO-GO por dataset e encerrar a Fase 1.

### 13. F1.8 — Avaliação da EMA e das evidências clínicas

#### O que foi feito

- Avaliação regulatória e clínica separada de semaglutida, tirzepatida e liraglutida por marca, indicação, população e dose.
- Consulta prioritária a EPARs, Product Information/SmPCs e assessment reports da EMA, complementada por publicações primárias dos ensaios.
- Mapeamento de critérios regulatórios, ensaios STEP, SURMOUNT, SURPASS, SCALE e estudos SELECT, LEADER e FLOW.
- Classificação de parâmetros de peso, HbA1c, descontinuação, segurança, eventos cardiovasculares/renais e persistência.
- Avaliação de heterogeneidade, comparação direta, validade externa e transferibilidade para a Alemanha.
- Decisões separadas para as dez funções solicitadas e classificação geral `CONDITIONAL GO`.
- Nenhum dataset/microdado foi baixado, nenhum código ou meta-análise foi criado e nenhuma população, uptake, custo ou projeção foi calculada.

#### O que ficou pendente

- Obter aprovação do usuário para a avaliação F1.8.
- Extrair formalmente parâmetros e intervalos de confiança somente após especificação do modelo e aprovação das fontes.
- Obter evidência real de persistência/adesão alemã ou europeia.
- Confirmar disponibilidade alemã das apresentações/doses e avaliar separadamente reembolso e custos.
- Corrigir futuramente os status F1.1–F1.7 e o caminho da F1.4 no `TASKS.md`, apenas mediante autorização.

#### Arquivos criados

- `00_project/feasibility/ema_clinical_evidence.md`

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Usar EMA como fonte normativa primária de indicação, população, dose e limitações, não como fonte de reembolso GKV.
- Usar resultados clínicos somente na população, dose, estimando e horizonte correspondentes.
- Não combinar silenciosamente participantes com e sem diabetes.
- Não converter perda de peso em eventos ou custos evitados sem evidência/modelagem específica.
- Restringir eventos cardiovasculares e renais às populações sustentadas por CVOTs e FLOW.
- Não produzir ranking entre medicamentos; comparações só serão aceitas quando diretas ou metodologicamente formais.

#### Próxima tarefa recomendada

- Aguardar aprovação do usuário. Nenhuma tarefa subsequente deve ser iniciada antes dessa aprovação.

### 12. F1.7 — Avaliação das fontes públicas IQVIA e do mercado autofinanciado

#### O que foi feito

- Avaliação exclusiva de fontes públicas da IQVIA e de fontes oficiais alemãs relevantes para o mercado GLP-1/GIP fora do reembolso regular do GKV.
- Separação conceitual entre pagamento integral, receita privada, PKV, copagamento GKV, vendas sem receita, canais legais e compras externas/ilegais.
- Verificação de conteúdo público, métricas, cobertura de canais, metodologia de painel, acesso técnico, produtos, indicações e limitações.
- Criação de tabela de evidências com fonte, período, métrica, cobertura, acesso, natureza e utilidade.
- Classificação das fontes públicas IQVIA como `NO-GO` para dataset quantitativo reproduzível e `GO` para contexto/valores pontuais.
- Classificação da quantificação pública do mercado autofinanciado como `NO-GO`.
- Classificação geral da fonte como `CONTEXTUAL DATASET`.
- Nenhum dataset ou arquivo comercial foi baixado, nenhum cadastro ou paywall foi contornado, nenhum contato comercial foi realizado, nenhum código foi criado e nenhuma estimativa de mercado foi calculada.

#### O que ficou pendente

- Obter aprovação do usuário para a avaliação F1.7.
- Decidir futuramente se a quantificação do self-pay é indispensável e, se for, avaliar aquisição comercial, nova fonte verificável ou pressuposto modelado com sensibilidade.
- Verificar termos de uso antes da reprodução de material IQVIA em entregáveis públicos.
- Corrigir futuramente os status desatualizados do `TASKS.md`, somente mediante autorização específica.

#### Arquivos criados

- `00_project/feasibility/iqvia_public_sources.md`

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Utilizar fontes públicas IQVIA apenas como evidência contextual e para valores pontuais rigorosamente rotulados.
- Não tratar os materiais públicos como dataset quantitativo reproduzível.
- Não quantificar o mercado autofinanciado apenas com os recortes públicos disponíveis.
- Não equiparar PKV, receita privada, pagamento integral ou indicação de obesidade.
- Não derivar pacientes de pacotes/vendas nem uptake futuro de valores comerciais pontuais.
- Usar G-BA, BMG e BfArM para delimitar regras oficiais, não para inferir volumes de mercado.

#### Próxima tarefa recomendada

- Aguardar aprovação do usuário. Nenhuma tarefa subsequente deve ser iniciada antes dessa aprovação.

### 11. F1.6 — Avaliação de viabilidade do Destatis Demographics

#### O que foi feito

- Avaliação exclusiva das tabelas oficiais de população e projeções do Destatis/GENESIS-Online.
- Identificação das tabelas `12411-0013`, `12411-0041`, `12411-0020`, `12421-0002` e `12421-0004`, com seus papéis e estatísticas de origem.
- Verificação de cobertura temporal, data de referência, população-alvo, cobertura geográfica, idade, sexo, estados federais e condições de acesso técnico.
- Separação explícita entre contagem censitária, população oficial atualizada, projeção oficial, cálculo derivado e pressuposto modelado.
- Registro das revisões associadas aos Censos 2011 e 2022 e do risco de combinar séries incompatíveis.
- Avaliação da compatibilidade dos denominadores com RKI/GEDA, RKI Diabetes, WIdO e os cenários futuros.
- Classificação da fonte como `GO` para o papel de denominador demográfico oficial.
- Nenhum arquivo foi baixado, nenhum código foi criado, nenhuma projeção foi calculada e nenhuma análise dos valores foi realizada.

#### O que ficou pendente

- Obter aprovação do usuário para a avaliação F1.6.
- Em etapa futura autorizada, escolher a data de referência ou população média compatível com cada prevalência.
- Definir e documentar a variante oficial da 16ª projeção coordenada caso seja necessário um denominador anual detalhado para 2026.
- Verificar precisão epidemiológica antes de realizar qualquer segmentação estadual.

#### Arquivos criados

- `00_project/feasibility/destatis_demographics.md`

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Utilizar o Destatis Demographics como denominador demográfico oficial do projeto.
- Tratar os resultados da `Fortschreibung des Bevölkerungsstandes` como `official population estimate` e os resultados da estatística `12421` como `official population projection`.
- Não tratar população residente como população segurada pelo GKV ou elegível para GLP-1/GIP.
- Construir faixas etárias somente no nível sustentado pelas prevalências de origem, evitando falsa precisão.
- Não selecionar nesta etapa uma variante populacional para 2026 nem calcular uma projeção própria.

#### Próxima tarefa recomendada

- Aguardar aprovação do usuário. Nenhuma avaliação subsequente deve ser iniciada antes dessa aprovação.

### 10. F1.4 — Avaliação de viabilidade do RKI Obesity/GEDA

#### O que foi feito

- Avaliação exclusiva das fontes oficiais do RKI associadas à prevalência de obesidade em adultos, com foco no GEDA.
- Verificação de fonte, método, período, população, amostragem, definição de BMI, granularidade, acesso técnico e natureza da evidência.
- Identificação de estimativas agregadas oficiais até 2023 e de Scientific Use Files GEDA confirmados até 2019/2020.
- Diferenciação entre dados observados de pesquisa, estimativas ponderadas, estimativas modeladas e pressupostos externos.
- Registro explícito das limitações de autorrelato, comparabilidade entre ondas, extrapolação para 2026, elegibilidade clínica e cobertura pelo GKV.
- Classificação da fonte como `CONDITIONAL GO`.
- Nenhum arquivo foi baixado, nenhum código foi criado e nenhuma análise de dados foi realizada.

#### O que ficou pendente

- Obter aprovação do usuário para a avaliação F1.4.
- Em etapa futura autorizada, inspecionar a documentação do SUF 2019/2020 para confirmar BMI contínuo, diabetes, comorbidades e variáveis socioeconômicas.
- Confirmar a precisão amostral das classes de obesidade nos estratos que forem usados.
- Definir separadamente, com fontes clínicas e regulatórias defensáveis, os critérios de elegibilidade para GLP-1/GIP.

#### Arquivos criados

- `00_project/feasibility/rki_obesity_geda.md`

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Utilizar o RKI/GEDA como baseline epidemiológico populacional oficial de obesidade em adultos na Alemanha.
- Usar as estimativas agregadas de 2023 para atualidade e considerar o SUF 2019/2020 para segmentações customizadas somente após acesso e verificação.
- Não tratar prevalência de obesidade como diagnóstico, cobertura pelo GKV ou elegibilidade automática para GLP-1/GIP.
- Classificar qualquer projeção para 2026 ou estimativa de elegibilidade como `modelled estimate`, mantendo-a separada dos dados observados.
- Considerar DEGS1 apenas como referência contextual antiga com antropometria medida, não como estimativa atual.

#### Próxima tarefa recomendada

- Aguardar aprovação do usuário. Nenhuma avaliação subsequente deve ser iniciada antes dessa aprovação.

### 9. Avaliação de viabilidade do Destatis Disease Costs

#### O que foi feito

- Registro da aprovação do RKI Diabetes como dataset contextual, não como base principal para modelar diabetes tipo 2.
- Avaliação exclusiva da Krankheitskostenrechnung do Destatis.
- Consulta apenas a páginas, metodologia e tabelas oficiais do Destatis/GENESIS-Online.
- Verificação de custos para diabetes E10–E14 e obesidade/hiperalimentação E65–E68.
- Verificação de anos, granularidade temporal, demográfica e por estabelecimento.
- Avaliação da adequação do dataset como baseline econômico oficial nacional dos custos diretos atribuídos a diabetes e obesidade.
- Aprovação do dataset como `CONDITIONAL GO`.
- Nenhum arquivo foi baixado, nenhum código foi criado e nenhuma análise dos valores foi realizada.

#### O que ficou pendente

- Após autorização futura de download, confirmar esquema, categorias e formatos exportados das tabelas selecionadas.
- Identificar fontes defensáveis antes de estimar a participação do GKV, a proporção de diabetes tipo 2 ou a fração de custos evitável.
- Registrar como `modelled assumptions` os parâmetros que não forem diretamente observáveis em fontes defensáveis.

#### Arquivos criados

- `00_project/feasibility/destatis_disease_costs.md`

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Utilizar a Krankheitskostenrechnung como baseline econômico oficial nacional dos custos diretos atribuídos a diabetes e obesidade, não como base isolada do modelo econômico.
- Não tratar os custos nacionais como equivalentes automáticos aos gastos do GKV.
- Não tratar todos os custos E10–E14 como diabetes tipo 2 ou como custos evitáveis.
- Considerar a Gesundheitsausgabenrechnung apenas como complemento potencial para estimar a participação do GKV.
- Não definir percentuais para participação do GKV, diabetes tipo 2 ou custos evitáveis antes da identificação de fontes defensáveis.

#### Próxima tarefa recomendada

- Próxima tarefa prevista no backlog: F1.4, avaliação do RKI Obesity/GEDA. Esta tarefa não foi iniciada.

### 8. Avaliação de viabilidade do RKI Diabetes Surveillance

#### O que foi feito

- Registro da aprovação oficial do WIdO pelo usuário.
- Avaliação exclusiva dos indicadores de prevalência e incidência documentadas de diabetes da RKI Diabetes Surveillance.
- Consulta apenas a páginas e publicações oficiais do RKI.
- Verificação de acesso, formato, população, definições, granularidades, cobertura temporal e limitações.
- Investigação específica da possibilidade de separar diabetes tipo 2 dos demais tipos.
- Aprovação do dataset como `CONTEXTUAL DATASET` para prevalência e incidência documentadas de diabetes no GKV, sem isolamento confiável de diabetes tipo 2.
- Nenhum arquivo foi baixado, nenhum código foi criado e nenhuma análise dos dados foi realizada.

#### O que ficou pendente

- Após autorização futura de download, inspecionar os XLSX para confirmar anos, colunas e estratificações efetivamente disponíveis.
- Definir como o modelo tratará a combinação E10–E14 e a separação de diabetes tipo 2.

#### Arquivos criados

- `00_project/feasibility/rki_diabetes.md`

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Utilizar o dataset como fonte contextual epidemiológica para prevalência e incidência documentadas de diabetes no GKV.
- Não considerar os indicadores adultos principais como medidas exclusivas de diabetes tipo 2.
- Não aplicar automaticamente a proporção de tipo 2 encontrada em estudos específicos a todos os anos ou estratos.
- Não utilizar o dataset como principal base para modelar exclusivamente diabetes tipo 2.

#### Próxima tarefa recomendada

- Etapa concluída. O dataset passa a apoiar o contexto epidemiológico e a interpretação dos resultados.

### 7. Verificação prática final do WIdO / PharMaAnalyst

#### O que foi feito

- Acesso direto ao portal oficial sem autenticação ou criação de conta.
- Confirmação de que os anos selecionáveis atualmente vão de 2012 a 2024.
- Confirmação da presença de Semaglutid, Tirzepatid, Liraglutid, Dulaglutid e Exenatid no mecanismo de busca por princípio ativo para 2024.
- Confirmação da existência de um botão funcional de exportação após gerar uma tabela no portal.
- Verificação de documentação oficial que descreve o portal como livremente acessível e disponibilizado para uso gratuito por interessados.
- Nenhum arquivo foi baixado e nenhuma análise dos valores exibidos foi realizada.

#### O que ficou pendente

- Confirmar a extensão e o formato real do arquivo exportado. O portal não informa o formato antes de iniciar o download, que não foi autorizado nesta tarefa.
- Obter aprovação do usuário para a recomendação final `CONDITIONAL GO`.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Manter `CONDITIONAL GO` porque o portal é acessível, possui período útil e contém os cinco princípios ativos exigidos, mas o formato real de exportação ainda não pôde ser confirmado sem baixar o arquivo.
- Não interpretar a expressão `Alle Rechte vorbehalten` como proibição de uso acadêmico dos dados; as páginas oficiais descrevem a ferramenta e seus dados como livremente acessíveis e disponíveis gratuitamente para interessados. Redistribuição de arquivos exportados continua não confirmada.

#### Próxima tarefa recomendada

- Aguardar a aprovação do usuário. Se autorizado futuramente, realizar um único download de teste para confirmar o formato antes da aquisição sistemática dos dados.

### 6. Avaliação de viabilidade do WIdO / PharMaAnalyst

#### O que foi feito

- Avaliação exclusiva do PharMaAnalyst com o template aprovado do Data Feasibility Map.
- Consulta apenas a páginas, portal, glossário e documentação metodológica oficiais do WIdO e do GKV-Spitzenverband.
- Verificação da população coberta, base de prescrições, indicadores, granularidade, classificação ATC e principais limitações.
- Registro explícito de fatos verificados, informações não confirmadas e limitações.
- Classificação preliminar do dataset como `CONDITIONAL GO`.
- Nenhum arquivo de dados foi baixado, nenhum código foi criado e nenhuma análise de dados foi realizada.

#### O que ficou pendente

- Obter aprovação do usuário para a recomendação `CONDITIONAL GO`.
- Antes de qualquer download, confirmar no portal o formato de exportação, os anos selecionáveis e a presença de cada princípio ativo GLP-1/GIP relevante.
- Esclarecer, se necessário, as condições de uso e redistribuição dos exports.

#### Arquivos criados

- `00_project/feasibility/wido.md`

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Utilizar o PharMaAnalyst apenas como representação do mercado ambulatorial reembolsado pelo GKV.
- Não interpretar os dados como consumo total alemão nem como evidência da indicação clínica de cada prescrição.
- Tratar divergências entre documentos oficiais sobre cobertura temporal e percentual do mercado como limitações a verificar.
- Condicionar o uso do dataset à verificação técnica do portal antes do download.

#### Próxima tarefa recomendada

- Aguardar a aprovação do usuário. Não iniciar a avaliação de outro dataset.

### 5. Criação do template do Data Feasibility Map

#### O que foi feito

- Criação de um template simples para avaliar datasets antes do download.
- Organização dos campos em identificação, acesso e cobertura, conteúdo analítico, avaliação e verificação.
- Inclusão de uma decisão preliminar `GO`, `CONDITIONAL GO` ou `NO-GO`.
- Inclusão de aprovação obrigatória do usuário antes do download.
- Nenhuma fonte externa foi pesquisada e nenhuma avaliação do WIdO foi iniciada.

#### O que ficou pendente

- Obter a aprovação do template.
- Avaliar a viabilidade do WIdO somente após aprovação explícita do usuário.

#### Arquivos criados

- `00_project/data_feasibility_template.md`

#### Arquivos modificados

- `PROJECT_STATUS.md`

#### Decisões tomadas

- Manter o template curto e orientado à decisão de aquisição.
- Registrar informações não verificadas como `não confirmado`, sem inventar dados.
- Não incluir métricas que normalmente só podem ser avaliadas depois do download, como valores ausentes e número real de observações.
- Exigir uma justificativa explícita para a decisão preliminar de cada dataset.

#### Próxima tarefa recomendada

- Após aprovação do usuário, executar F1.2: avaliar exclusivamente a viabilidade dos dados WIdO/PharMaAnalyst.

### 4. Revisão estrutural do backlog oficial

#### O que foi feito

- Reorganização integral do backlog oficial em tarefas identificadas por IDs.
- Inclusão de status, prioridade, esforço, dependências, entregável e necessidade de aprovação para cada tarefa.
- Separação da Fase 1 em avaliações independentes para WIdO, RKI Diabetes, RKI Obesity, Destatis Disease Costs, Destatis Demographics, IQVIA Public Sources e EMA/evidências clínicas.
- Inclusão de pontos explícitos de aprovação antes de downloads, processamento, modelagem e encerramento de fases críticas.
- Inclusão da seção `Definition of Done`.
- Nenhuma pesquisa externa foi iniciada.

#### O que ficou pendente

- Obter a aprovação da estrutura revisada do backlog.
- Iniciar a tarefa F1.1 somente após a aprovação do usuário.
- Criar o modelo e os campos obrigatórios do Data Feasibility Map.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- `00_project/TASKS.md`
- `PROJECT_STATUS.md`

#### Decisões tomadas

- Cada tarefa terá um ID estável para permitir o registro explícito de dependências.
- As avaliações individuais das sete fontes da Fase 1 não dependerão umas das outras.
- A tarefa F1.1 exigirá aprovação antes do início de qualquer pesquisa.
- Uma tarefa somente será considerada concluída quando atender à `Definition of Done`.

#### Próxima tarefa recomendada

- Aprovar o backlog revisado e, depois, executar F1.1: definir o modelo do Data Feasibility Map sem iniciar a pesquisa das fontes.

### 1. Revisão inicial do projeto

#### O que foi feito

- Leitura da estrutura completa disponível no projeto.
- Leitura integral de `00_project/project_handoff.md`.
- Leitura de `README.md`.
- Confirmação do objetivo, das fontes planejadas, da abordagem metodológica e das limitações do projeto.
- Avaliação da organização atual das pastas.

#### O que ficou pendente

- Criar o Data Feasibility Map.
- Identificar e validar individualmente os datasets oficiais.
- Verificar se os dados do RKI permitem separar diabetes tipo 2 dos demais tipos.
- Preencher o `README.md`.
- Corrigir futuramente a renderização Markdown de `00_project/project_handoff.md`, mediante autorização prévia.

#### Arquivos criados

- Nenhum.

#### Arquivos modificados

- Nenhum.

#### Decisões tomadas

- Manter a estrutura atual do projeto neste estágio.
- Preservar integralmente todos os dados originais em `01_raw_data`.
- Não iniciar modelagem antes de concluir o Data Feasibility Map.
- Separar claramente dados observados de cenários modelados.

#### Próxima tarefa recomendada

- Criar o Data Feasibility Map antes de baixar ou processar datasets.

### 2. Documentação das regras permanentes

#### O que foi feito

- Criação de um documento com as regras permanentes de comunicação, código, nomenclatura, preservação de dados, transparência analítica, organização e reprodutibilidade.

#### O que ficou pendente

- Aplicar continuamente as regras documentadas durante as próximas etapas do projeto.

#### Arquivos criados

- `00_project/codex_instructions.md`

#### Arquivos modificados

- Nenhum.

#### Decisões tomadas

- Toda comunicação será realizada em português do Brasil.
- Todo código, comentário de código e nomenclatura técnica será escrito em inglês.
- Arquivos RAW serão tratados como imutáveis.
- Informações analíticas serão classificadas como fato verificado, hipótese, limitação ou próximo passo quando aplicável.
- Decisões importantes e tarefas concluídas serão documentadas.

#### Próxima tarefa recomendada

- Criar e manter o registro de status do projeto.

### 3. Criação do registro de status do projeto

#### O que foi feito

- Criação deste arquivo para acompanhar formalmente a evolução do projeto.
- Definição das informações obrigatórias para cada tarefa concluída.

#### O que ficou pendente

- Atualizar este arquivo ao final de cada tarefa importante futura.

#### Arquivos criados

- `PROJECT_STATUS.md`

#### Arquivos modificados

- Nenhum arquivo preexistente foi modificado.

#### Decisões tomadas

- Cada registro de tarefa deverá informar o que foi feito, o que ficou pendente, os arquivos criados, os arquivos modificados, as decisões tomadas e a próxima tarefa recomendada.
- O histórico deverá ser preservado para garantir rastreabilidade e reprodutibilidade.

#### Próxima tarefa recomendada

- Criar o Data Feasibility Map com a estrutura definida em `00_project/project_handoff.md`.
