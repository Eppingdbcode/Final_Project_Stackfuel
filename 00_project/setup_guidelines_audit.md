# Auditoria de setup e diretrizes

**Data:** 2026-08-12  
**Escopo:** auditoria read-only do estado encontrado antes das únicas alterações documentais autorizadas nesta tarefa.  
**Referência externa:** guia oficial StackFuel, `project_guide.md`, em `https://github.com/stackfuel/dpp_guide/blob/main/project_guide.md` (acesso em 2026-08-12).  
**Referências internas:** `PROJECT_STATUS.md`, `00_project/TASKS.md`, `00_project/decision_log.md`, `00_project/data_conventions.md`, `00_project/data_feasibility_map.md`, `00_project/project_handoff.md`, `README.md`, `environment.yml`, demais documentos de governança e estrutura completa do repositório.

## Resultado executivo

O projeto possui governança metodológica incomumente forte para sua fase: escopo, fontes, limitações, imutabilidade RAW, convenções, decisões e backlog estão detalhados. O novo `AGENTS.md` transforma essas regras em instruções curtas e permanentes sem substituir os documentos de origem.

O setup técnico, porém, ainda não é reproduzível nem está alinhado de forma resolvida com o guia do curso. Há uma decisão aprovada por Conda/Mamba em conflito explícito com o padrão UV da StackFuel; não há `pyproject.toml`, lockfile, `.gitignore` ou repositório Git detectável; o ambiente declarado não foi resolvido/testado; e a documentação de estado ficou desatualizada após a aquisição RAW parcial. Nenhuma dessas correções foi executada nesta tarefa.

## Divergências

### CRITICAL-01 — controle de versão Git não detectável

- **Estado atual:** `git status --short --branch` falha com “not a git repository”; não existe `.git` na estrutura acessível da raiz. Assim, não foi possível determinar alterações preexistentes, autoria, histórico ou produzir um diff Git confiável.
- **Esperado:** o guia StackFuel exige Git/GitHub e fluxo versionado; a solicitação atual também exige preservar mudanças do usuário e mostrar diff.
- **Risco concreto:** alterações podem ser sobrescritas ou atribuídas incorretamente; não há rollback, auditoria de autoria, comparação com baseline ou colaboração segura.
- **Correção recomendada:** confirmar se esta pasta é uma cópia sem `.git` ou se a raiz correta está em outro local. Se for a raiz pretendida, inicializar/conectar Git somente em tarefa autorizada, após preservar um snapshot e definir remoto/branch.
- **Arquivos afetados:** raiz do repositório e todos os artefatos versionáveis.
- **Pode quebrar:** caminhos/imports/ambiente, não diretamente; reprodutibilidade e histórico, sim, se um repositório novo for associado ao remoto errado. Exige decisão explícita.

### HIGH-01 — conflito UV + `pyproject.toml` versus Conda/Mamba + `environment.yml`

- **Estado atual:** D-014 aprovou Conda/Mamba, `environment.yml`, `conda-forge`, `nodefaults` e Python 3.14. O guia oficial StackFuel prescreve `uv init`, dependências em `pyproject.toml`, ambiente `.venv` e sincronização por `uv sync`. Não existe `pyproject.toml` nem `uv.lock`.
- **Esperado:** uma estratégia de ambiente única, explícita e reproduzível, alinhada ao curso ou com desvio formalmente justificado. Dois sistemas concorrentes não devem ser mantidos sem necessidade e autoridade clara.
- **Risco concreto:** comandos de setup incompatíveis, versões divergentes, dupla fonte de verdade e avaliação do curso potencialmente desalinhada.
- **Correção recomendada:** abrir uma tarefa decisória única: (a) migrar formalmente para UV; ou (b) manter Conda/Mamba e registrar a exceção aprovada à norma StackFuel. Não criar `pyproject.toml` paralelo enquanto essa decisão estiver aberta. Se houver necessidade real de ambos, definir papéis não concorrentes e mecanismo de sincronização verificável.
- **Arquivos afetados:** `environment.yml`, futuro `pyproject.toml`/`uv.lock`, `README.md`, `00_project/decision_log.md`, `00_project/TASKS.md`, `PROJECT_STATUS.md`.
- **Pode quebrar:** ambiente e reprodutibilidade, sim; imports e caminhos, possivelmente, dependendo das versões/resolução. Migração exige teste limpo.

### HIGH-02 — ambiente declarado não resolvido, bloqueado ou validado

- **Estado atual:** `environment.yml` declara Python 3.14 e dependências sem versões resolvidas; não há lockfile. Os documentos registram que nenhum ambiente foi criado e nenhum import/teste foi executado.
- **Esperado:** ambiente instalável e verificável, com versões reproduzíveis; o guia StackFuel prevê sincronização das dependências entre colaboradores.
- **Risco concreto:** Python 3.14 ou dependências podem não resolver em conjunto; execuções futuras podem variar por data/plataforma.
- **Correção recomendada:** depois da decisão HIGH-01, resolver em ambiente limpo, registrar versões, executar smoke tests de imports e `pytest`, e adotar o lockfile do sistema escolhido.
- **Arquivos afetados:** `environment.yml` ou futuro `pyproject.toml`/lockfile, `README.md`, relatório de reprodutibilidade.
- **Pode quebrar:** ambiente e imports, sim; caminhos, não em princípio.

### HIGH-03 — camada RAW contém cópia não registrada na governança atual

- **Estado atual:** existem dois arquivos de 556 bytes com SHA-256 idêntico: `01_raw_data/wido/wirkst_export.csv` e `01_raw_data/wido/pharmaanalyst/year=2024/atc=A10BJ06/wirkst_export.csv`. D-018 e `PROJECT_STATUS.md` registram somente o primeiro. O segundo caminho também diverge do padrão aprovado `01_raw_data/<source_id>/<dataset_id>/<snapshot_date>/` e usa segmentos `key=value` não previstos.
- **Esperado:** toda instância RAW deve ser imutável, possuir um registro de manifesto e caminho/versionamento aprovado; nenhuma cópia, movimentação ou renomeação deve ocorrer silenciosamente.
- **Risco concreto:** cadeia de custódia ambígua, dupla contagem no inventário, origem/autoria da cópia desconhecida e futuras rotinas podendo processar o mesmo conteúdo duas vezes.
- **Correção recomendada:** não apagar nem mover. Em tarefa própria, identificar a origem da segunda cópia e decidir qual representação será canônica; registrar ambas e sua relação no manifesto/checksums, ou preservar uma como incidente/cópia documentada. Qualquer mudança de caminho exige decisão e validação prévias.
- **Arquivos afetados:** os dois CSVs RAW, futuro `01_raw_data/raw_data_manifest.csv`, checksums, `decision_log.md` e documentos de status.
- **Pode quebrar:** caminhos e reprodutibilidade, sim; imports/ambiente, não.

### HIGH-04 — ausência de `.gitignore`

- **Estado atual:** não existe `.gitignore`.
- **Esperado:** o guia StackFuel exige exclusão de `.venv`, caches Python/Jupyter, segredos, artefatos de IDE/SO e outros arquivos temporários; a política de dados deve ser decidida conforme tamanho, licença e privacidade.
- **Risco concreto:** commit acidental de ambiente, credenciais, caches, outputs volumosos ou dados cuja redistribuição não esteja autorizada.
- **Correção recomendada:** criar `.gitignore` em tarefa própria após decidir Git e ambiente. Não ignorar indiscriminadamente toda a camada RAW: alinhar padrões com a estratégia de aquisição, licenças e necessidade de manifesto.
- **Arquivos afetados:** futuro `.gitignore`, `.env*`, `.venv/`, caches, notebooks, dados e outputs.
- **Pode quebrar:** caminhos/imports/ambiente, não; visibilidade e versionamento de arquivos, sim, se padrões forem amplos.

### MEDIUM-01 — README e status operacional desatualizados

- **Estado atual:** `README.md` afirma que a Fase 2 não começou, nenhum dataset foi baixado, RAW está vazio e F0.9/F2.1/F6.1 ainda aguardam etapas já concluídas. A realidade registrada em `PROJECT_STATUS.md`/`TASKS.md` é F2.2 parcialmente em progresso com RAW adquirido.
- **Esperado:** README factual e coerente com o backlog/status, conforme guia StackFuel e D-015.
- **Risco concreto:** novos agentes e avaliadores podem executar tarefas incorretas, presumir ausência de dados ou repetir aquisições.
- **Correção recomendada:** atualizar somente os trechos de status, estrutura e próximos passos em tarefa documental própria, preservando o histórico nos documentos de governança.
- **Arquivos afetados:** `README.md`.
- **Pode quebrar:** não; melhora reprodutibilidade operacional.

### MEDIUM-02 — manifesto e checksums ainda ausentes para RAW adquirido

- **Estado atual:** não existem `01_raw_data/raw_data_manifest.csv` nem `01_raw_data/raw_data_checksums.sha256`; o backlog posterga-os para F2.7/F2.8 após as aquisições e D-018 explicita a pendência.
- **Esperado:** metadados e integridade completos para cada dataset/arquivo RAW, conforme governança interna e o novo `AGENTS.md`.
- **Risco concreto:** alterações silenciosas ou perda de origem podem ocorrer antes do encerramento da Fase 2; a duplicação atual já torna a identificação ambígua.
- **Correção recomendada:** resolver primeiro o escopo/caminho da F2.2; depois executar as tarefas formais de manifesto e checksum. Considerar, mediante decisão registrada, se a integridade mínima deve ser capturada imediatamente após cada aquisição futura em vez de apenas no final da fase.
- **Arquivos afetados:** RAW WIdO, manifesto, checksums, `TASKS.md`, `decision_log.md`.
- **Pode quebrar:** caminhos, potencialmente; ambiente/imports, não; reprodutibilidade, sim se adiado ou feito sobre alvo ambíguo.

### MEDIUM-03 — estrutura recomendada para código e testes ainda ausente

- **Estado atual:** não existem `src/` nem `tests/`; não há scripts, módulos, notebooks ou testes analíticos. O backlog prevê pipelines e testes futuros, mas não define ainda o pacote de código.
- **Esperado:** o guia StackFuel recomenda `src/` para lógica reutilizável e `tests/` para testes, com abordagem híbrida notebooks/scripts.
- **Risco concreto:** quando o processamento começar, lógica pode se concentrar em notebooks, dificultando testes, imports e reprodução.
- **Correção recomendada:** definir a estrutura mínima de código na tarefa imediatamente anterior à implementação; criar apenas diretórios/módulos necessários, sem scaffolding especulativo.
- **Arquivos afetados:** futuros `src/`, `tests/`, notebooks e configuração de ambiente.
- **Pode quebrar:** imports e caminhos, sim, se introduzida depois de código dependente de caminhos ad hoc; ambiente, não necessariamente.

### MEDIUM-04 — `project_handoff.md` possui Markdown escapado

- **Estado atual:** cabeçalhos e marcadores aparecem como `\#`, `\*` e `\---`, prejudicando renderização; a dívida já está registrada historicamente.
- **Esperado:** documentação legível e navegável.
- **Risco concreto:** leitura humana e extração automatizada ficam mais difíceis; regras podem ser interpretadas incorretamente.
- **Correção recomendada:** corrigir apenas a marcação em tarefa documental específica, com comparação textual para garantir que o conteúdo não mudou.
- **Arquivos afetados:** `00_project/project_handoff.md`.
- **Pode quebrar:** não; risco baixo de diff amplo, mitigável por validação.

### LOW-01 — ausência de automação para limpar outputs de notebooks

- **Estado atual:** não há configuração `nbstripout`, pre-commit ou política automatizada; ainda não existem notebooks.
- **Esperado:** o guia StackFuel requer limpar outputs antes de commit e sugere automação após teste.
- **Risco concreto:** futuros notebooks podem inflar o repositório e gerar diffs ruidosos.
- **Correção recomendada:** após decidir ambiente/Git e antes da primeira entrega de notebooks, escolher e testar uma política de limpeza; documentar exceções para outputs exigidos como entregáveis verificados.
- **Arquivos afetados:** futuros notebooks, `.gitattributes`/pre-commit/configuração de ambiente, se adotados.
- **Pode quebrar:** outputs incorporados podem ser removidos; não afeta imports ou ambiente, salvo dependência opcional escolhida.

### LOW-02 — documentação permanente duplicada em dois pontos

- **Estado atual:** `00_project/codex_instructions.md` e o novo `AGENTS.md` se sobrepõem parcialmente. O primeiro contém detalhes de comunicação; o segundo é a entrada operacional reconhecida por agentes e referencia a governança.
- **Esperado:** uma porta de entrada curta, com documentos detalhados claramente subordinados/referenciados e sem regras contraditórias.
- **Risco concreto:** divergência futura entre instruções duplicadas.
- **Correção recomendada:** manter `AGENTS.md` conciso como índice normativo e, em revisão documental futura, declarar explicitamente a relação entre os dois arquivos sem apagar histórico.
- **Arquivos afetados:** `AGENTS.md`, `00_project/codex_instructions.md`, possivelmente `README.md`.
- **Pode quebrar:** não.

## Conformidades relevantes

- Escopo investigativo não predetermina resultado e separa observação de modelagem.
- Fontes oficiais alemãs e EMA têm prioridade e funções delimitadas.
- RAW é definido como imutável; processamento e outputs possuem camadas separadas.
- Convenções cobrem nomes, versões, datas, unidades e valores ausentes.
- Backlog possui dependências, pontos de aprovação e Definition of Done.
- Decisões metodológicas e limitações possuem rastreabilidade extensa.
- Python/Pandas, notebooks focados e scripts reutilizáveis são compatíveis com o guia; a implementação ainda não começou.

## Validação desta tarefa

- Nenhuma pasta foi reorganizada e nenhum dataset, notebook, código analítico ou ambiente foi alterado.
- Nenhum arquivo RAW foi aberto para análise de conteúdo, alterado, movido ou renomeado; somente existência, tamanho e hashes foram comparados em modo leitura.
- O conflito de ambiente foi documentado sem criar um segundo sistema.
- A ausência de Git impediu uma comparação contra baseline; a lista de alterações desta tarefa foi controlada pelos alvos autorizados.

## Resolução e superação — 2026-08-12

Esta seção preserva a auditoria acima como fotografia correta da antiga pasta `C:\Users\eppin\GLP1_Germany_Final_Project`. Os fatos históricos não foram reescritos retroativamente.

- **CRITICAL-01 resolvida:** foi localizada a raiz Git oficial `C:\Users\eppin\Desktop\Final_Project_Stackfuel`, conectada a `https://github.com/Eppingdbcode/Final_Project_Stackfuel.git`; `main` estava limpa e sincronizada antes da consolidação.
- **HIGH-01 resolvida:** UV foi adotado definitivamente como único sistema ativo; `environment.yml` não foi incorporado e D-019 substitui D-014 para execução futura.
- **HIGH-02 resolvida para o setup atual:** `pyproject.toml` e `uv.lock` foram atualizados somente pelo UV, `uv sync` foi executado e imports foram incluídos na validação final. Reprodutibilidade analítica completa continuará dependente de código/testes futuros.
- **HIGH-03 controlada:** os dois RAW duplicados foram preservados, registrados e associados no manifesto, sem deduplicação. A origem do segundo caminho continua não confirmada.
- **HIGH-04 resolvida:** `.gitignore` ampliado e validado antes da cópia RAW.
- **MEDIUM-01 resolvida:** README atualizado para o estado consolidado real.
- **MEDIUM-02 parcialmente resolvida:** manifesto e checksums foram criados para os dois RAW atuais; F2.7/F2.8 permanecem abertas para futuras aquisições.
- **MEDIUM-03 parcialmente resolvida:** `src/` foi preservado e `tests/` documentado; ainda não há código/testes analíticos.
- **MEDIUM-04 resolvida:** escapes Markdown do handoff foram corrigidos mecanicamente e o estado operacional atual foi acrescentado sem apagar o brief histórico.
- **LOW-01 aberta:** automação de limpeza de outputs de notebooks não foi implantada por ausência de notebooks analíticos.
- **LOW-02 controlada:** `AGENTS.md` é a entrada operacional; `codex_instructions.md` permanece histórico/complementar.

As validações e o commit/push desta consolidação são registrados em `PROJECT_STATUS.md` e no handoff. A próxima tarefa única volta ao trabalho substantivo: concluir F2.2.
