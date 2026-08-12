# Instruções permanentes para agentes

## Objetivo e autoridade

Este projeto investiga, sem conclusão predeterminada, quando e para quem o reembolso de tratamentos GLP-1/GIP para obesidade poderia reduzir a carga clínica e econômica do diabetes tipo 2 no GKV alemão. O escopo e as limitações estão em `README.md`, `00_project/project_handoff.md` e `00_project/data_feasibility_map.md`.

As normas oficiais da StackFuel no [project guide](https://github.com/stackfuel/dpp_guide/blob/main/project_guide.md) têm prioridade para práticas gerais do curso. Decisões específicas e aprovadas deste repositório prevalecem quando documentarem uma adaptação justificada; conflitos devem ser registrados e levados à decisão do usuário, nunca resolvidos silenciosamente. Antes de alterar metodologia, estrutura ou ambiente, consulte `PROJECT_STATUS.md`, `00_project/TASKS.md`, `00_project/decision_log.md`, `00_project/data_conventions.md` e os documentos diretamente aplicáveis.

Antes de iniciar qualquer tarefa, leia nesta ordem: `PROJECT_STATUS.md`, `00_project/TASKS.md`, `00_project/decision_log.md`, `00_project/project_handoff.md` e os documentos metodológicos ou de fontes diretamente relevantes. Consulte `00_project/WORKFLOW.md` para os detalhes operacionais.

## Regras de trabalho

- Trabalhe em apenas uma tarefa elegível e autorizada por vez, respeitando dependências e pontos de aprovação de `00_project/TASKS.md`. Não amplie o escopo nem faça overengineering sem justificativa registrada.
- Priorize fontes oficiais alemãs e, para regulação europeia, fontes oficiais da UE. Nunca invente dados, resultados, fontes, URLs, versões, datas, cobertura, unidades ou quaisquer metadados; use `pending_verification` quando algo não estiver confirmado.
- Separe e rotule explicitamente `observed data`, parâmetros provenientes da literatura, estimativas/projeções oficiais, `derived calculations` e `modelled assumptions`. Não apresente associação como causalidade.
- Para cada dataset, registre no manifesto aplicável ao menos fonte/instituição, URL, data de acesso/download, versão ou snapshot, período e cobertura, unidade observacional, variáveis/unidades, licença/termos, limitações, nome original, caminho e integridade, conforme `00_project/raw_data_manifest_template.md`.
- `01_raw_data/` é imutável: nunca edite, corrija, converta, renomeie, substitua ou sobrescreva RAW. Preserve cada versão original; transformações pertencem a `02_processed_data/` e devem ter linhagem reproduzível.
- Use Python e Pandas para processamento e análise. Código, comentários e nomes técnicos ficam em inglês e seguem `00_project/data_conventions.md`. Fixe seeds quando houver aleatoriedade e evite dependências não justificadas.
- Notebooks servem para exploração e comunicação, devem ser pequenos, focados, executáveis do início ao fim e sem lógica reutilizável relevante; mova essa lógica para scripts/módulos Python. Antes de versionar, remova outputs de notebook, salvo quando um entregável exigir outputs verificados.
- Scripts devem receber entradas e produzir derivados/outputs sem alterar RAW. Tabelas e gráficos ficam em `04_outputs/`, com fonte, período, população/denominador, unidade, definição, rótulo observado/modelado e limitações suficientes para interpretação.
- Trate explicitamente missing values, duplicatas, tipos, codificações, unidades, categorias, chaves, granularidade e denominadores. Nunca converta missing em zero, elimine duplicatas ou harmonize unidades sem regra documentada e validação.
- Registre decisões metodológicas e suas justificativas em `00_project/decision_log.md`. Ao concluir uma tarefa, atualize `PROJECT_STATUS.md` e `00_project/TASKS.md` sem apagar o histórico.
- Antes de declarar conclusão, execute e registre validações proporcionais ao risco: testes relevantes, execução reproduzível, verificações de esquema/linhagem/unidades e inspeção dos entregáveis. Preserve alterações preexistentes do usuário e revise o diff.
- Não declare conclusão com documentação central desatualizada. Mostre o diff e o estado Git e confirme que RAW, segredos e caches não entraram no staging.
- Controle explicitamente o prazo final de `2026-08-26` ao priorizar tarefas e preserve tempo suficiente para preparar e validar a apresentação interativa em Microsoft Power BI.
- Power BI deve consumir somente tabelas processadas e validadas por Python/Pandas. Reconcilie métricas, filtros, denominadores e resultados entre Python e Power BI e mantenha visível a distinção entre dados observados e premissas.

## Definition of Done

- **Código:** implementação no escopo, legível e reproduzível; testes/validações relevantes passam; entradas, outputs, dependências e limitações estão documentados; nenhum RAW foi alterado.
- **Dados:** origem e metadados completos; RAW íntegro e imutável; transformações reproduzíveis; missing, duplicatas, tipos, unidades, denominadores, chaves, cobertura e limitações validados e registrados.
- **Documentação:** conteúdo factual, coerente com os documentos de governança, fontes rastreáveis, decisões/limitações explícitas, links/caminhos verificados e status/backlog atualizados.

## New chat startup protocol

1. Leia os cinco documentos centrais na ordem definida acima.
2. Identifique a raiz Git e confirme branch e working tree.
3. Antes de alterar arquivos, resuma estado atual, última tarefa concluída, bloqueios, próxima tarefa elegível e sua Definition of Done.

## Task completion protocol

1. Atualize `PROJECT_STATUS.md` e `00_project/TASKS.md`.
2. Registre decisões em `00_project/decision_log.md` e atualize `00_project/project_handoff.md` quando houver mudança material.
3. Execute testes e validações; mostre `git status` e o diff.
4. Confirme ausência de RAW, segredos e caches no staging.
5. Sugira ou crie commit somente conforme a autorização da tarefa.
