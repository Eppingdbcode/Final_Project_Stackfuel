# Final Project — GLP-1 & Public Health in Germany

## Objetivo

Projeto acadêmico de Data Analytics que investiga, sem conclusão predeterminada, se, quando e para quais grupos de risco a ampliação do reembolso de tratamentos GLP-1/GIP para obesidade poderia reduzir a carga clínica e econômica do diabetes tipo 2 no seguro-saúde estatutário alemão (GKV).

**Deadline final:** 2026-08-26. **Apresentação final:** dashboard interativo em Microsoft Power BI, alimentado por tabelas processadas e validadas em Python/Pandas.

Pergunta principal: **o reembolso de tratamentos GLP-1 para obesidade poderia reduzir, no longo prazo, a carga financeira associada à obesidade e ao diabetes tipo 2 no GKV alemão?** A análise é nacional; resultados estaduais serão apenas complementares e condicionados à disponibilidade, comparabilidade e qualidade dos dados.

O projeto constrói cenários, não uma demonstração causal prévia. Toda evidência deve ser classificada como `observed data`, `literature parameters`, `official estimates/projections`, `derived calculations` ou `modelled assumptions`.

O Power BI deverá reconciliar métricas e filtros com os controles produzidos em Python e distinguir visualmente dados observados de premissas. A proposta mínima, sujeita aos dados e ao prazo, inclui visão executiva, tendências observadas, análise de cenários e métodos/limitações.

## Fontes principais

- Destatis: demografia, projeções populacionais e custos por doença;
- RKI/GEDA: prevalência de obesidade;
- RKI Diabetes Surveillance: contexto de diabetes documentado no GKV;
- WIdO/PharMaAnalyst: prescrições, DDD e despesas ambulatoriais reembolsadas pelo GKV;
- EMA: indicações, populações e doses regulatórias;
- estudos clínicos publicados: parâmetros de eficácia, segurança e persistência, após seleção documentada.

## Estrutura

```text
00_project/          governança, decisões, feasibility e metodologia
01_raw_data/         arquivos originais locais, imutáveis e não publicados
02_processed_data/   dados derivados e analíticos reproduzíveis
03_notebooks/        exploração e comunicação analítica
04_outputs/          tabelas, gráficos e relatórios
05_sources/          documentação e estudos sujeitos a direitos de uso
src/                 código Python reutilizável
tests/               testes automatizados
```

## Ambiente UV

Requer Python 3.14 e [UV](https://docs.astral.sh/uv/). O ambiente oficial usa exclusivamente `.python-version`, `pyproject.toml`, `uv.lock` e `.venv` gerenciada pelo UV.

```powershell
uv sync
uv run python -c "import pandas, matplotlib, seaborn, openpyxl"
uv run pytest
```

Execute scripts com `uv run python <script.py>`. Abra notebooks no VS Code usando o kernel da `.venv`; notebooks devem ser executáveis do início ao fim e manter a lógica reutilizável em `src/`.

## Política RAW

`01_raw_data/` é local, imutável e ignorada pelo Git, exceto `README.md`, manifesto e checksums. Nunca editar, corrigir, transformar, sobrescrever ou publicar RAW sem licença e autorização explícitas. No estado atual, há duas cópias byte a byte idênticas de um export WIdO; ambas permanecem preservadas e registradas, sem deduplicação.

## Estado atual

- Fase 1 de feasibility encerrada com `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`.
- F2.2 permanece `IN PROGRESS`: existe aquisição parcial WIdO local; os demais datasets não foram todos adquiridos.
- A execução integrada F2.2–F2.8 está autorizada sem aprovações intermediárias; a Fase 3 não pode ser iniciada durante essa execução.
- Para WIdO, o escopo aprovado é 2012–2024 e os princípios ativos ATC A10BJ efetivamente disponíveis no PharMaAnalyst, armazenados no caminho canônico documentado. Combinações indisponíveis devem ser registradas, não inventadas.
- Nenhum RAW está publicado no GitHub.
- O ambiente oficial foi consolidado em UV; não existe `environment.yml` na raiz oficial.
- Ainda não existem resultados analíticos nem conclusão econômica.

## Limitações centrais

População residente, população de survey, segurados GKV, pessoas diagnosticadas, regulatoriamente elegíveis, clinicamente apropriadas e tratadas são universos distintos. WIdO não mede o mercado total ou indicação clínica; GEDA usa peso/altura autorrelatados; custos Destatis não equivalem automaticamente a gastos ou custos evitáveis do GKV; eficácia de ensaio não equivale a efetividade alemã; projeções e premissas devem ser rotuladas e testadas em sensibilidade.

Consulte `AGENTS.md`, `PROJECT_STATUS.md`, `00_project/TASKS.md`, `00_project/decision_log.md`, `00_project/project_handoff.md` e `00_project/WORKFLOW.md` antes de continuar o desenvolvimento.
