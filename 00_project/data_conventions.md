# Data, Naming, Versioning, and Date Conventions

**Task:** F0.6  
**Created:** 2026-08-10  
**Scope:** convenções estáveis e auditáveis para documentos, dados, código e outputs do projeto.  
**Compatibility:** alinhado ao `00_project/raw_data_manifest_template.md`; nenhuma incompatibilidade material foi identificada.

## 1. Princípios gerais

1. Nomes técnicos — arquivos, diretórios, IDs, tabelas, colunas, variáveis, funções e classes — devem ser escritos em inglês.
2. Identificadores e nomes controlados usam letras ASCII minúsculas, números e underscore (`snake_case`), salvo exceções específicas deste documento.
3. Espaços, acentos, símbolos e pontuação não são permitidos em novos nomes técnicos controlados.
4. O nome original recebido de uma fonte nunca é alterado no campo `original_filename`; um nome operacional fica em `stored_filename`.
5. Nomes devem ser legíveis, específicos, estáveis e suficientemente curtos para uso prático. Clareza tem prioridade sobre abreviação.
6. Identificadores não devem conter conclusões mutáveis, como `best`, `final_result`, `high_risk`, `successful` ou `cost_saving`.
7. Versões e datas nunca devem ser inferidas quando ausentes.
8. Nenhum nome, data ou versão pode provocar sobrescrita de um artefato anterior.

## 2. Regras de nomenclatura

### 2.1 Caracteres e separadores

| Element | Convention | Example |
|---|---|---|
| Identificadores, tabelas e colunas | `snake_case` | `reference_period_start` |
| Diretórios novos autorizados | `snake_case` | `example_dataset` |
| Arquivos | `snake_case` com sufixos estruturados | `example_dataset_2026-01-15_v01_table_a.csv` |
| Classes de código futuras | `PascalCase` | `ExampleDatasetLoader` |
| Funções e variáveis futuras | `snake_case` | `validate_schema` |
| Constantes futuras | `UPPER_SNAKE_CASE` | `DEFAULT_ENCODING` |
| Notebooks | prefixo numérico de dois dígitos + `snake_case` | `01_example_eda.ipynb` |

- Hífen é reservado para datas ISO e rótulos documentais aprovados, como `NO-GO`; não usar hífen em IDs técnicos controlados.
- Extensões são minúsculas quando o nome armazenado for controlado.
- Não transliterar silenciosamente o `original_filename`; transliteração aplica-se apenas ao nome operacional.
- Caracteres alemães em nomes controlados seguem: `ä→ae`, `ö→oe`, `ü→ue`, `ß→ss`. Outros diacríticos são removidos por transliteração documentada.

### 2.2 Abreviações e siglas

- Usar abreviações somente quando amplamente reconhecidas no projeto ou definidas no glossário deste documento.
- Siglas tornam-se minúsculas em `snake_case`: `gkv`, `rki`, `ema`, `bmi`, `atc`, `ddd`, `icd`, `suf`.
- Não criar duas abreviações para o mesmo conceito.
- Na primeira ocorrência em texto documental, escrever o termo e a sigla quando isso melhorar a compreensão.
- Evitar abreviações ambíguas como `data`, `info`, `misc`, `temp`, `new`, `old`, `final`, `latest` ou `vfinal` como identificadores autônomos.

### 2.3 Números, singular e plural

- Números podem aparecer em versões, sequências, datas, códigos oficiais ou IDs de tarefa; não iniciar slugs com número, salvo notebook ordenado.
- Usar singular para uma entidade/registro (`dataset_id`, `source_id`) e plural para coleções (`clinical_events`, `model_results`).
- Nomes de tabelas/datasets devem descrever o conjunto de linhas; nomes de colunas devem descrever um valor por linha.
- Unidades não devem ser ocultadas: quando necessário, usar sufixos como `_eur`, `_bytes`, `_count`, `_rate`, `_pct`, `_mg`, `_days`.

### 2.4 Termos proibidos ou ambíguos

Não usar sem definição explícita:

- `final`, `latest`, `new`, `old`, `copy`, `fixed`, `clean`, `cleaned`, `temp`, `tmp`, `misc`, `data`, `output`;
- `patient` quando a unidade observada for prescrição, DDD, embalagem, venda ou dispensação;
- `observed` para projeções, cálculos derivados ou assumptions;
- `self_pay` quando o campo representar receita privada, PKV ou mercado fora do GKV sem confirmação do pagador final;
- `type_2_diabetes` quando a fonte agregar E10–E14 sem separação validada;
- `eligible_population` para prevalência de obesidade sem aplicação documentada dos critérios regulatórios e clínicos.

## 3. Convenções de datas e horários

### 3.1 Formatos

| Concept | Field example | Required format | Meaning |
|---|---|---|---|
| Data de publicação | `release_date` | `YYYY-MM-DD` | Publicação/liberação pelo publicador |
| Data de revisão | `revision_date` | `YYYY-MM-DD` | Revisão/correção declarada pelo publicador |
| Data de acesso | `access_date` | `YYYY-MM-DD` | Consulta da fonte/página |
| Download | `download_timestamp` | ISO 8601 com segundos e fuso | Momento efetivo da aquisição |
| Snapshot | `snapshot_date` | `YYYY-MM-DD` | Estado capturado de conteúdo mutável/interativo |
| Período de referência | `reference_period_start/end` | ISO conforme precisão publicada | Período representado pelos dados |
| Criação/atualização de registro | `record_created_at`, `record_last_updated_at` | ISO 8601 com segundos e fuso | Evento interno auditável |

### 3.2 UTC e horário local

- Timestamps persistidos devem conter offset explícito: `YYYY-MM-DDTHH:MM:SS+HH:MM`.
- UTC usa sufixo `Z`, por exemplo `2026-01-15T09:30:00Z`.
- Horário local usa o offset efetivo no evento, por exemplo `2026-01-15T10:30:00+01:00`.
- Não armazenar timezone somente como abreviação (`CET`, `CEST`), pois pode ser ambígua.
- Conversões para UTC podem ser adicionadas, mas o timestamp original auditável não deve ser perdido.

### 3.3 Datas parciais, desconhecidas e intervalos

- Data completa conhecida: `YYYY-MM-DD`.
- Apenas mês conhecido: `YYYY-MM`; apenas ano conhecido: `YYYY`. Preservar a precisão; nunca completar com dia/mês inventado.
- Data desconhecida: `unknown`; não disponível: `not_available`; não aplicável: `not_applicable`; a confirmar: `pending_verification`.
- Intervalos usam dois campos, como `reference_period_start` e `reference_period_end`; não concatenar em texto quando houver esquema estruturado.
- Intervalo aberto deve manter o limite desconhecido explicitamente, nunca usar a data de acesso como fim presumido.
- Formatos ambíguos como `10/08/26`, `08-10-2026` ou `Aug-10-26` são proibidos.

### 3.4 Distinções obrigatórias

- `publication_year` não é automaticamente o ano de referência.
- `access_date` não é `release_date` nem versão do publicador.
- `download_timestamp` não é `snapshot_date`, embora possam coincidir em evento específico documentado.
- População de 31 de dezembro, população média anual e resultado trimestral não são datas intercambiáveis.
- Horizonte clínico de um ensaio não deve ser convertido em ano civil.

## 4. Versionamento

### 4.1 Versão do publicador e versão interna

- `publisher_version` preserva exatamente a versão declarada pela fonte.
- Quando não houver versão declarada, usar `not_available` ou `pending_verification`; não usar a data de download como substituto.
- A versão interna usa `vNN`, começando em `v01`, e identifica o artefato preservado dentro do projeto.
- Uma versão interna nova representa conteúdo ou pacote diferente; mudança apenas no registro do manifesto não cria nova versão do arquivo.

### 4.2 Eventos de versão

| Event | Required action |
|---|---|
| Nova publicação | Novo registro, `snapshot_date`, versão interna e checksum |
| Revisão retroativa | Novo registro; preencher `supersedes_record_id`; preservar anterior |
| Republicação | Comparar checksum/metadados; registrar como novo snapshot mesmo com nome igual |
| Correção do publicador | Novo registro e versão; documentar `revision_date` e motivo |
| Snapshot de portal | Registrar data, seleção, mecanismo e componente; nunca sobrescrever snapshot anterior |
| Vários arquivos da mesma publicação | Mesmo dataset/versão, componentes e sequências de arquivo distintas |
| Suplemento | Componente próprio, como `supplement_a`; vincular à publicação |
| Documentação | Componente próprio, como `methodology` ou `data_dictionary`; não confundir com dados |
| Alteração silenciosa | Se checksum divergir, preservar ambos, colocar o incidente sob revisão e criar novo registro |
| Versão desconhecida | `publisher_version=not_available`; usar versão interna e snapshot, sem inventar versão externa |

- Versões anteriores nunca são apagadas ou sobrescritas.
- A relação sucessora/anterior usa `supersedes_record_id` e `superseded_by_record_id`.
- `latest_known_version_status` descreve conhecimento atual e pode mudar sem alterar o conteúdo do arquivo.

## 5. Identificadores e nomes armazenados

### 5.1 IDs estáveis

| Identifier | Pattern | Neutral example |
|---|---|---|
| `source_id` | `<institution_or_portal_slug>` | `example_source` |
| `dataset_id` | `<source_id>_<dataset_slug>` ou slug estável aprovado | `example_source_dataset` |
| Component ID | `<component_type>_<component_slug_or_code>` | `table_component_a` |
| Internal version ID | `vNN` | `v01` |
| File sequence | `fNNN` | `f001` |
| `manifest_record_id` | `mfr_<dataset_id>_<snapshot_date>_vNN_<component_id>_fNNN` | `mfr_example_source_dataset_2026-01-15_v01_table_a_f001` |

IDs não incluem classificação de feasibility, qualidade, resultado analítico ou condição mutável.

### 5.2 `stored_filename`

Padrão geral:

`<dataset_id>_<reference_or_snapshot>_vNN_<component_id>[_<language>]_fNNN.<ext>`

Exemplo fictício:

`example_source_dataset_2025_v01_table_a_en_f001.csv`

Regras:

- Usar período de referência quando ele identificar inequivocamente o conteúdo; usar snapshot quando a fonte for mutável/interativa.
- Se ambos forem necessários, registrar ambos nos metadados e incluir no nome somente o necessário para unicidade e legibilidade.
- Idioma usa ISO 639-1 quando relevante (`de`, `en`).
- O nome operacional nunca substitui `original_filename`.
- Original e derivado devem ser distinguidos pela camada/caminho e pelo manifesto; adicionar `raw` ao nome não transforma um derivado em RAW.

### 5.3 Caminhos relativos

RAW aprovado:

`01_raw_data/<source_id>/<dataset_id>/<snapshot_date>/`

Exemplo fictício:

`01_raw_data/example_source/example_source_dataset/2026-01-15/`

Regras:

- Caminhos do manifesto usam `/`, são relativos ao projeto e nunca contêm drive ou diretório pessoal.
- O caminho deve distinguir fonte, dataset e snapshot.
- Não criar diretórios nesta tarefa; o padrão será aplicado somente após autorização.
- Caminhos existentes não serão renomeados retroativamente sem tarefa própria aprovada.

## 6. Camadas e estados dos artefatos

Somente categorias existentes ou explicitamente previstas no backlog são reconhecidas:

| Layer/category | Approved location | Meaning |
|---|---|---|
| Governança/documentação | `00_project/` | Regras, decisões, templates, status e relatórios de qualidade |
| RAW original | `01_raw_data/` | Arquivo original imutável adquirido da fonte |
| Processed intermediate | `02_processed_data/intermediate/` | Conversão, descompressão operacional, limpeza e padronização futuras |
| Processed analytical | `02_processed_data/analytical/` | Datasets analíticos validados futuros |
| Notebooks | `03_notebooks/` | Análises reproduzíveis e documentadas |
| Outputs | `04_outputs/` | Tabelas, gráficos, relatórios e resultados do modelo |
| Sources/documentation | `05_sources/documentation/` | Documentação oficial preservada |
| Sources/studies | `05_sources/studies/` | Estudos e evidências preservados |

- `staging` e `curated` não estão atualmente aprovados como novas camadas e não devem ser criados por esta convenção.
- Uma cópia descomprimida é derivada e pertence à camada intermediária futura, não ao RAW original.
- A extensão ou o nome não determina a camada; origem, transformação, caminho e cadeia de custódia determinam o estado.
- A camada RAW nunca recebe correção, limpeza ou conversão.

## 7. Convenções futuras para dados e código

Este documento define nomes, mas não cria código.

### 7.1 Datasets, tabelas e colunas

- Datasets e tabelas: `snake_case`, com domínio e granularidade claros, por exemplo `example_events_by_year`.
- Colunas: `snake_case`, uma variável por coluna e uma definição única.
- IDs terminam em `_id`; códigos oficiais em `_code`; nomes descritivos em `_name`.
- Datas terminam em `_date`; timestamps em `_at` ou `_timestamp`; início/fim em `_start`/`_end`.
- Booleanos usam prefixos `is_`, `has_`, `requires_` ou forma afirmativa inequívoca.
- Contagens usam `_count`; proporções `_proportion`; percentuais `_pct`; taxas `_rate` com denominador documentado.
- Valores monetários incluem moeda, como `_eur`; valores reais/nominais exigem documentação separada.
- Não traduzir códigos/categorias no RAW; padronizações pertencem à camada processada.

### 7.2 DataFrames, funções, variáveis e classes

- DataFrames: substantivo descritivo, sem sufixos genéricos `df1`/`data2`; exemplo `example_population_by_age`.
- Funções: verbo + objeto em `snake_case`, por exemplo `validate_manifest_record`.
- Variáveis: substantivos específicos em `snake_case`.
- Classes: `PascalCase`, substantivo singular.
- Constantes: `UPPER_SNAKE_CASE`.

### 7.3 Scripts, notebooks e configuração

- Scripts futuros: `<action>_<object>.py`, como `validate_raw_manifest.py`.
- Notebooks: `NN_<topic>_<purpose>.ipynb`, preservando a ordem já prevista no backlog.
- Configurações: nome específico + extensão adequada, como `data_sources.yml`; nunca armazenar credenciais no nome ou conteúdo versionado.
- Arquivos temporários não devem ser versionados ou confundidos com entregáveis.

### 7.4 Outputs, figuras e tabelas

- Figuras: `<topic>_<metric>_<segment>_<reference_period>.<ext>`.
- Tabelas: `<topic>_<purpose>_<reference_period>.<ext>`.
- Resultados modelados devem incluir contexto de cenário no nome ou metadado; não usar `observed`.
- Versões finais publicadas recebem versão explícita; nunca usar apenas `final`.

## 8. Mapeamento documental, técnico e de abreviações

### 8.1 Classificações de feasibility

As formas documentais e técnicas são representações do mesmo conceito, não classificações distintas.

| Documentary label | Technical value | Meaning |
|---|---|---|
| `GO` | `GO` | Uso direto para função delimitada |
| `CONDITIONAL GO` | `CONDITIONAL_GO` | Uso condicionado a requisitos explícitos |
| `CONTEXTUAL ONLY` | `CONTEXTUAL_ONLY` | Contexto/triangulação, sem alimentar estimativa principal |
| `NO-GO` | `NO_GO` | Uso pretendido não autorizado |
| não disponível | `not_available` | Fonte/componente não acessível para uso atual |
| não avaliado | `not_evaluated` | Adequação ainda não avaliada |
| sem classificação independente | `no_independent_classification` | Papel aprovado sem nova decisão autônoma |

### 8.2 Valores de ausência

| Documentary label | Technical value |
|---|---|
| desconhecido | `unknown` |
| não disponível | `not_available` |
| não aplicável | `not_applicable` |
| pendente de verificação | `pending_verification` |

### 8.3 Abreviações autorizadas

| Abbreviation | Meaning |
|---|---|
| `gkv` | German statutory health insurance |
| `rki` | Robert Koch-Institut |
| `ema` | European Medicines Agency |
| `bmi` | body mass index |
| `atc` | Anatomical Therapeutic Chemical classification |
| `ddd` | defined daily dose |
| `icd` | International Classification of Diseases |
| `suf` | Scientific Use File |
| `raw` | immutable original data layer |

Nenhuma abreviação cria ou modifica uma classificação metodológica.

## 9. Compatibilidade com o manifesto RAW

| Manifest element | Convention alignment |
|---|---|
| `manifest_record_id` | Mesmo padrão `mfr_<dataset_id>_<snapshot_date>_vNN_<component>_fNNN` |
| `dataset_id` / `source_id` | Slugs estáveis em `snake_case`, sem caracteres especiais |
| `stored_filename` | Distingue dataset, período/snapshot, versão, componente, idioma opcional e arquivo |
| `relative_raw_path` | `01_raw_data/<source_id>/<dataset_id>/<snapshot_date>/` |
| Datas/timestamps | ISO 8601, precisão e timezone explícitos |
| Versionamento | Preserva versão externa e interna; nunca sobrescreve |
| Snapshots | Novo registro e data própria para cada captura |
| Substituição | IDs anterior/sucessor e checksum mantêm rastreabilidade |
| `original_filename` | Sempre preservado separadamente |
| Imutabilidade | Nome/caminho não autorizam modificação do original |
| Rótulos de decisão | Mapeamento documental/técnico explícito e equivalente |

Não foi encontrada incompatibilidade material com o manifesto aprovado. Este documento não altera o manifesto.

## 10. Exemplos fictícios

**EXEMPLOS ILUSTRATIVOS — NÃO REPRESENTAM DATASETS ADQUIRIDOS**

| Purpose | Example |
|---|---|
| Dataset ID | `example_source_population` |
| Manifest record | `mfr_example_source_population_2026-01-15_v01_table_a_f001` |
| Stored RAW filename | `example_source_population_2025_v01_table_a_en_f001.csv` |
| RAW relative path | `01_raw_data/example_source/example_source_population/2026-01-15/` |
| Publication date | `2026-01-10` |
| Access date | `2026-01-15` |
| Download timestamp | `2026-01-15T10:30:00+01:00` |
| UTC equivalent | `2026-01-15T09:30:00Z` |
| Partial date | `2026-01` |
| Documentary/technical decision | `CONDITIONAL GO` / `CONDITIONAL_GO` |

Os exemplos não são URLs reais, aquisições, versões de publicadores ou metadados verificados.

## 11. Checklist de validação da F0.6

- [x] Nomes técnicos estão em inglês e usam convenções consistentes.
- [x] Espaços, acentos e caracteres especiais estão excluídos de IDs controlados.
- [x] Datas e timestamps usam ISO 8601 sem ambiguidade.
- [x] Publicação, revisão, acesso, download, snapshot e período de referência permanecem distintos.
- [x] Datas parciais/desconhecidas não são completadas por inferência.
- [x] Versão do publicador e versão interna permanecem separadas.
- [x] Versões anteriores nunca são sobrescritas.
- [x] `original_filename` permanece separado de `stored_filename`.
- [x] Fonte, dataset, componente, versão e arquivo podem ser distinguidos.
- [x] Camadas existentes e planejadas no backlog estão documentadas sem criar novas camadas.
- [x] Rótulos documentais e valores técnicos estão explicitamente mapeados.
- [x] As convenções são compatíveis com o manifesto RAW aprovado.
- [x] Nenhum arquivo existente foi renomeado.
- [x] Nenhum dado, código, checksum, diretório RAW ou tarefa da Fase 2 foi criado/executado.

## 12. Resultado técnico da F0.6

O documento atende integralmente aos critérios documentados da F0.6. Não há conflito material com o manifesto RAW aprovado. A execução técnica está concluída; a aprovação formal permanece pendente do usuário.
