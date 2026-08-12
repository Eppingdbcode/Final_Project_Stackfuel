# Raw Data Manifest Template

**Task:** F0.7  
**Created:** 2026-08-10  
**Purpose:** padrão obrigatório de rastreabilidade, integridade, versionamento e preservação de futuros arquivos RAW.  
**Current state:** template documental; não registra aquisição real e não autoriza download, ingestão ou processamento.

## 1. Princípios obrigatórios

1. O arquivo original adquirido é imutável e nunca deve ser sobrescrito.
2. SHA-256 é o algoritmo padrão obrigatório de integridade, salvo incompatibilidade técnica documentada e aprovada.
3. Descompressão, conversão, limpeza, correção ou renomeação operacional deve gerar outro artefato; arquivos derivados não pertencem à camada RAW.
4. Problemas encontrados no RAW devem ser documentados, nunca corrigidos no original.
5. Uma nova versão, revisão, publicação ou snapshot nunca substitui uma versão anterior.
6. Mesmo nome de arquivo não prova conteúdo idêntico; versão, timestamps, metadados e checksum devem ser comparados.
7. Campos desconhecidos não serão preenchidos por inferência. Usar somente os valores de ausência controlados definidos neste documento.
8. Funções analíticas autorizadas devem vir do `decision_log.md`, não ser inventadas durante a aquisição.
9. A validação inicial confirma integridade e estrutura técnica; não substitui validação analítica ou de qualidade.

## 2. Valores padronizados de ausência

| Valor | Uso |
|---|---|
| `unknown` | A informação pode existir, mas ainda não foi confirmada |
| `not_available` | A informação não é fornecida ou não está acessível |
| `not_applicable` | O campo não se aplica ao registro |
| `pending_verification` | A confirmação depende de uma verificação futura autorizada |

Campos obrigatórios podem aceitar esses valores somente quando a regra individual permitir. Eles não podem ser usados para ocultar uma falha de aquisição ou validação.

## 3. Dicionário completo do manifesto

### 3.1 Identificação

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `manifest_record_id` | Identificador único e imutável do registro | Yes | lowercase ID | `mfr_example_dataset_2026-01-15_v01_c01_f001` | Convenção da seção 4; único no manifesto | No |
| `dataset_id` | Identificador estável do dataset através de versões | Yes | lowercase slug | `example_dataset` | `^[a-z0-9]+(?:_[a-z0-9]+)*$` | No |
| `source_id` | Identificador estável da fonte/instituição | Yes | lowercase slug | `example_source` | Mesmo padrão de slug | No |
| `source_name` | Nome publicado da fonte | Yes | text | `Example Official Source` | Corresponder à fonte oficial documentada | `pending_verification` |
| `institution` | Instituição publicadora/responsável | Yes | text | `Example Institution` | Não inferir por domínio sem confirmação | `pending_verification` |
| `dataset_title` | Título oficial do dataset | Yes | text | `Example Dataset Title` | Preservar grafia publicada | `pending_verification` |
| `component_or_table` | Tabela, componente, endpoint ou pacote específico | Yes | text/list | `table_example_001` | Distinguir componentes materialmente diferentes | `not_applicable` |
| `internal_owner` | Responsável interno pela custódia | Yes | controlled text | `data_engineering` | Pessoa ou papel aprovado | `pending_verification` |
| `related_task` | ID da tarefa que autorizou a aquisição | Yes | task ID/list | `F2.x` | Deve existir no `TASKS.md` | No |
| `feasibility_decision_reference` | Referência à decisão aprovada | Yes | decision ID/list | `D-0xx` | Deve existir no `decision_log.md` | No |
| `approval_status` | Estado da aprovação para aquisição/uso | Yes | controlled vocabulary | `approved` | Vocabulário da seção 8 | No |

### 3.2 Origem e aquisição

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `source_url` | URL oficial específica da fonte/tabela | Yes | absolute HTTPS URL | `https://example.invalid/official/table` | Preferir página específica; não usar busca quando existir URL oficial | `not_available` |
| `landing_page_url` | Página oficial de contexto, se diferente | No | absolute HTTPS URL | `https://example.invalid/official` | Diferente de `source_url` quando aplicável | `not_applicable` |
| `direct_download_url` | URL direta usada na aquisição | No | absolute URL | `https://example.invalid/file.ext` | Registrar somente se efetivamente aplicável | `not_applicable`, `not_available` |
| `access_mechanism` | Mecanismo de acesso | Yes | controlled vocabulary | `web_download` | Vocabulário da seção 8 | No |
| `access_date` | Data em que a fonte foi consultada | Yes | ISO date | `2026-01-15` | `YYYY-MM-DD`; não confundir com download | No |
| `download_timestamp` | Momento efetivo da aquisição | Yes | ISO 8601 datetime with zone | `2026-01-15T10:30:00+01:00` | Deve refletir o evento real | `pending_verification` antes da aquisição |
| `acquired_by` | Pessoa ou processo que adquiriu o arquivo | Yes | text | `authorized_operator` | Deve ser auditável | `pending_verification` |
| `acquisition_method` | Método/procedimento utilizado | Yes | controlled text | `manual_official_download` | Descrever sem credenciais ou segredos | `pending_verification` |
| `license_or_terms_url` | URL oficial de licença/termos | No | absolute URL | `https://example.invalid/terms` | Não inferir licença | `not_available`, `pending_verification` |
| `access_restrictions` | Restrições de acesso, uso ou redistribuição | Yes | text/list | `citation_required` | Registrar texto resumido e referência | `unknown`, `not_applicable` |
| `authentication_required` | Se autenticação foi necessária | Yes | boolean/controlled | `false` | `true`, `false` ou `unknown` | `unknown` |
| `commercial_or_public` | Natureza do acesso | Yes | controlled vocabulary | `public` | Vocabulário da seção 8 | No |
| `notes_on_source_provenance` | Observações sobre origem e cadeia de publicação | No | text | `Official publisher landing page` | Apenas fatos documentados | `not_applicable` |

### 3.3 Identificação do arquivo

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `original_filename` | Nome recebido exatamente da origem | Yes | filename | `original_example.ext` | Preservar sem alteração no campo | No |
| `stored_filename` | Nome único usado na preservação RAW | Yes | filename | `example_dataset_2026-01-15_v01_component_f001.ext` | Convenção da seção 4; não sobrescrever | No |
| `relative_raw_path` | Caminho relativo planejado/real na camada RAW | Yes | POSIX-style relative path | `01_raw_data/example_source/example_dataset/2026-01-15/` | Deve iniciar em `01_raw_data/`; nunca absoluto | No |
| `file_extension` | Extensão do arquivo | Yes | lowercase text | `.ext` | Corresponder ao nome armazenado | `not_available` |
| `mime_type` | MIME type detectado/declarado | Yes | IANA MIME type | `application/octet-stream` | Validar contra conteúdo quando possível | `pending_verification` |
| `compression_format` | Formato de compactação | No | controlled text | `zip` | `none` se não compactado | `not_applicable`, `pending_verification` |
| `archive_contents` | Inventário de itens do arquivo compactado | No | list/reference | `file_001.ext` | Não extrair para RAW por sobrescrita; registrar conteúdo | `not_applicable`, `pending_verification` |
| `file_size_bytes` | Tamanho exato do arquivo | Yes | non-negative integer | `123456` | Medido após aquisição; bytes | `pending_verification` |
| `number_of_files` | Quantidade de arquivos representados pelo pacote | Yes | positive integer | `1` | ≥1; conferir inventário | `pending_verification` |
| `language` | Idioma(s) do conteúdo | No | ISO 639-1 list | `en` | Lista controlada quando múltipla | `unknown`, `not_applicable` |
| `encoding` | Codificação de texto | No | controlled text | `utf-8` | Aplicável somente a texto | `not_applicable`, `pending_verification` |

### 3.4 Integridade

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `checksum_algorithm` | Algoritmo principal de integridade | Yes | controlled vocabulary | `sha256` | Deve ser `sha256`, salvo exceção aprovada | No |
| `checksum_value` | Digest calculado do arquivo original | Yes | 64 lowercase hex chars | `pending_verification` | `^[a-f0-9]{64}$` após cálculo; nunca inventar | `pending_verification` |
| `checksum_generated_at` | Momento da geração | Yes | ISO 8601 datetime with zone | `2026-01-15T10:31:00+01:00` | Imediatamente após download | `pending_verification` |
| `checksum_tool_or_method` | Ferramenta ou método utilizado | Yes | text | `approved_sha256_method` | Registrar versão/método quando implementado | `pending_verification` |
| `integrity_verification_status` | Resultado da verificação de integridade | Yes | controlled vocabulary | `pending` | Vocabulário da seção 8 | No |
| `integrity_verified_at` | Momento da última verificação | No | ISO 8601 datetime with zone | `2026-01-15T10:35:00+01:00` | Obrigatório quando status for `verified`/`failed` | `not_applicable`, `pending_verification` |
| `integrity_verified_by` | Responsável pela verificação | No | text | `authorized_operator` | Obrigatório quando verificado | `not_applicable`, `pending_verification` |
| `duplicate_status` | Resultado da comparação com registros existentes | Yes | controlled vocabulary | `unique` | `unique`, `exact_duplicate`, `possible_duplicate`, `pending` | No |
| `duplicate_reference` | ID do registro duplicado | No | manifest ID/list | `mfr_example_previous` | Obrigatório para duplicata exata/possível | `not_applicable` |

### 3.5 Versão e temporalidade

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `publisher_version` | Versão declarada pelo publicador | Yes | text | `v1.0` | Preservar texto oficial | `not_available`, `pending_verification` |
| `release_date` | Data de publicação/liberação | Yes | ISO date | `2026-01-10` | Não confundir com acesso | `not_available`, `pending_verification` |
| `revision_date` | Data da revisão do publicador | No | ISO date | `2026-01-12` | ≥ release date quando aplicável | `not_applicable`, `not_available` |
| `reference_period_start` | Início do período coberto pelos dados | Yes | ISO date/year/period | `2025-01-01` | Usar precisão publicada; não inventar dia | `unknown`, `not_applicable` |
| `reference_period_end` | Fim do período coberto | Yes | ISO date/year/period | `2025-12-31` | ≥ início | `unknown`, `not_applicable` |
| `publication_year` | Ano de publicação | Yes | four-digit year | `2026` | Derivar apenas quando suportado pela data oficial | `unknown` |
| `data_frequency` | Frequência declarada dos dados | Yes | controlled vocabulary | `annual` | Vocabulário controlado | `unknown`, `not_applicable` |
| `snapshot_date` | Data do snapshot de portal/tabela | No | ISO date | `2026-01-15` | Obrigatória para conteúdo mutável/interativo | `not_applicable` |
| `supersedes_record_id` | Registro substituído por esta versão | No | manifest ID | `mfr_example_previous` | Não apagar o registro anterior | `not_applicable`, `unknown` |
| `superseded_by_record_id` | Registro que substituiu este | No | manifest ID | `mfr_example_next` | Atualização auditável | `not_applicable`, `unknown` |
| `latest_known_version_status` | Se é a versão mais recente conhecida | Yes | controlled vocabulary | `latest_known` | `latest_known`, `superseded`, `unknown` | No |

### 3.6 Cobertura e conteúdo

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `population_or_market_coverage` | Universo populacional ou mercado coberto | Yes | text | `Defined source population` | Copiar/parafrasear metadado oficial; não concluir além dele | `unknown` |
| `geographic_coverage` | Territórios cobertos | Yes | text/list | `Example national coverage` | Vocabulário geográfico consistente | `unknown` |
| `geographic_level` | Nível geográfico mínimo | Yes | controlled vocabulary | `national` | `national`, `state`, `regional`, `local`, `unknown` | `unknown` |
| `demographic_coverage` | Idades, sexo e outros grupos cobertos | No | text/list | `adults` | Não confundir cobertura com granularidade | `unknown`, `not_applicable` |
| `clinical_coverage` | Diagnósticos, condições ou população clínica | No | text/list | `not_applicable` | Somente metadado da fonte | `unknown`, `not_applicable` |
| `medicine_or_substance_coverage` | Medicamentos, marcas, substâncias ou ATC | No | text/list | `not_applicable` | Não inferir indicação por substância | `unknown`, `not_applicable` |
| `payer_or_channel_coverage` | Pagador/canal coberto | No | text/list | `not_applicable` | Private, PKV, GKV e self-pay permanecem distintos | `unknown`, `not_applicable` |
| `unit_of_observation` | Unidade elementar do arquivo | Yes | text | `one row per published cell` | Confirmar após inspeção | `pending_verification` |
| `primary_measures` | Medidas principais publicadas | Yes | text/list | `measure_example` | Preservar definições/unidades | `pending_verification` |
| `exclusions` | Exclusões declaradas | Yes | text/list | `none_documented` | `none_documented` não significa ausência real de exclusões | `unknown`, `not_available` |
| `known_limitations` | Limitações documentadas da fonte | Yes | text/list/reference | `See feasibility decision` | Vincular aos documentos aprovados | `unknown` |

### 3.7 Esquema e estrutura

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `format` | Formato efetivo do arquivo | Yes | controlled text | `xlsx` | Confirmar por conteúdo, não apenas extensão | `pending_verification` |
| `sheet_or_table_names` | Abas/tabelas existentes | No | list | `table_1` | Preservar nomes originais | `not_applicable`, `pending_verification` |
| `delimiter` | Delimitador de arquivo tabular | No | controlled character | `comma` | Aplicável a formatos delimitados | `not_applicable`, `pending_verification` |
| `decimal_separator` | Separador decimal | No | `dot`/`comma` | `dot` | Confirmar por inspeção | `not_applicable`, `pending_verification` |
| `date_format` | Formatos de data observados | No | text/list | `YYYY-MM-DD` | Não converter no RAW | `not_applicable`, `pending_verification` |
| `header_row` | Linha/caminho do cabeçalho | No | integer/text | `1` | ≥1 quando tabular | `not_applicable`, `pending_verification` |
| `row_count` | Número de linhas por tabela/arquivo | Yes | non-negative integer/list | `pending_verification` | Contagem técnica reproduzível | `pending_verification`, `not_applicable` |
| `column_count` | Número de colunas | Yes | non-negative integer/list | `pending_verification` | Contagem técnica reproduzível | `pending_verification`, `not_applicable` |
| `schema_reference` | Referência ao esquema/dicionário oficial | No | URL/path/reference | `not_available` | Preferir documentação oficial | `not_available`, `pending_verification` |
| `documented_primary_keys` | Chaves primárias declaradas oficialmente | No | list | `not_available` | Somente se documentadas | `not_available`, `not_applicable` |
| `candidate_keys` | Combinações potencialmente únicas | No | list | `pending_verification` | Rotular como candidata; nunca como confirmada | `pending_verification`, `not_applicable` |
| `known_identifiers` | Códigos e identificadores existentes | No | list | `identifier_example` | Registrar definição e domínio | `unknown`, `not_applicable` |
| `missing_value_codes` | Códigos de ausência no arquivo | No | list/map | `not_available` | Preservar códigos originais | `not_available`, `pending_verification` |
| `unit_definitions` | Definições oficiais das unidades | Yes | list/map/reference | `See official metadata` | Não converter silenciosamente | `pending_verification` |
| `structural_notes` | Observações técnicas de estrutura | No | text | `not_applicable` | Sem interpretação analítica nova | `not_applicable` |

### 3.8 Controle de RAW

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `raw_immutability_status` | Estado de imutabilidade do original | Yes | controlled vocabulary | `immutable_original` | Vocabulário da seção 8 | No |
| `original_file_preserved` | Se o arquivo recebido foi preservado intacto | Yes | boolean | `true` | Deve ser `true` para liberar processamento | No |
| `renamed_copy_created` | Se foi criada cópia com nome operacional | Yes | boolean | `false` | Cópia deve ter registro/referência própria | No |
| `decompressed_copy_created` | Se foi criada cópia descompactada | Yes | boolean | `false` | Deve ficar fora do original RAW ou em área derivada aprovada | No |
| `processed_copy_reference` | Referência a artefato processado | No | relative path/record ID | `not_applicable` | Nunca apontar o original como processado | `not_applicable` |
| `manual_modification_status` | Estado de modificação manual do original | Yes | controlled vocabulary | `not_modified` | `modified` bloqueia uso e exige incidente | No |
| `modification_reason` | Motivo de qualquer modificação detectada | No | text | `not_applicable` | Não legitima alteração proibida; documenta incidente | `not_applicable` |
| `chain_of_custody_notes` | Histórico de custódia, cópia e transferência | Yes | append-only text/reference | `Acquired and preserved` | Não apagar entradas anteriores | `pending_verification` |

### 3.9 Validação inicial

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `file_opens_successfully` | Se o arquivo abre tecnicamente | Yes | boolean/unknown | `true` | Não implica qualidade analítica | `pending_verification` |
| `archive_integrity_valid` | Resultado da verificação do arquivo compactado | No | boolean/unknown | `true` | Obrigatório para arquivos compactados | `not_applicable`, `pending_verification` |
| `expected_format_confirmed` | Se formato real corresponde ao esperado | Yes | boolean/unknown | `true` | Validar conteúdo e MIME | `pending_verification` |
| `unexpected_format_change` | Se houve mudança frente à versão anterior | Yes | boolean/unknown | `false` | Se `true`, documentar e revisar | `pending_verification` |
| `expected_columns_present` | Se colunas esperadas estão presentes | No | boolean/unknown | `true` | Somente após esquema esperado documentado | `not_applicable`, `pending_verification` |
| `schema_validation_status` | Resultado da validação estrutural | Yes | controlled vocabulary | `pending` | Vocabulário da seção 8 | No |
| `row_count_validation_status` | Resultado da validação da contagem | Yes | controlled vocabulary | `pending` | Comparar apenas com expectativa documentada | No |
| `checksum_validation_status` | Resultado da verificação do checksum | Yes | controlled vocabulary | `pending` | Deve refletir SHA-256 | No |
| `quarantine_status` | Estado de quarentena lógica | Yes | controlled vocabulary | `not_quarantined` | Falha de integridade exige `quarantined` | No |
| `quarantine_reason` | Motivo da quarentena | No | controlled text/list | `not_applicable` | Obrigatório quando em quarentena | `not_applicable` |
| `validation_notes` | Notas factuais da validação técnica | No | text | `not_applicable` | Não incluir análise substantiva | `not_applicable` |

### 3.10 Relação com o projeto

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `authorized_analytical_functions` | Funções autorizadas pela decisão aprovada | Yes | controlled list | `denominator` | Deve corresponder ao `decision_log.md` | No |
| `prohibited_analytical_functions` | Funções explicitamente proibidas | Yes | controlled list | `patient_estimation` | Deve preservar NO-GO/limitações | `not_applicable` |
| `conditions_of_use` | Condições obrigatórias para uso | Yes | text/list/reference | `harmonization_required` | Vincular à decisão aprovada | `not_applicable` |
| `required_harmonization` | Dimensões que exigem harmonização | Yes | controlled list | `reference_period` | Não executar harmonização na RAW | `not_applicable`, `pending_verification` |
| `related_model_module` | Módulo futuro relacionado | No | controlled list | `demographic_denominator` | Não implica autorização de modelagem | `not_applicable`, `unknown` |
| `requires_derived_calculation` | Se o uso exige cálculo derivado | Yes | boolean/controlled | `true` | Deve ser consistente com a decisão | `unknown` |
| `requires_modelled_assumption` | Se o uso exige assumption | Yes | boolean/controlled | `false` | Não converter assumption em observado | `unknown` |
| `citation_reference` | Citação oficial recomendada | No | text/URL | `pending_verification` | Preservar texto oficial quando disponível | `not_available`, `pending_verification` |
| `related_internal_documents` | Documentos internos vinculados | Yes | relative path/list | `00_project/decision_log.md` | Caminhos relativos existentes | No |

### 3.11 Histórico e auditoria

| Field | Definition | Required | Expected type/format | Neutral example | Validation rule | Absence allowed |
|---|---|---|---|---|---|---|
| `record_created_at` | Momento de criação do registro | Yes | ISO 8601 datetime with zone | `2026-01-15T10:32:00+01:00` | Imutável após criação | No |
| `record_created_by` | Autor do registro | Yes | text | `authorized_operator` | Auditável | No |
| `record_last_updated_at` | Momento da última atualização | Yes | ISO 8601 datetime with zone | `2026-01-15T10:40:00+01:00` | ≥ criação | No |
| `record_last_updated_by` | Autor da última atualização | Yes | text | `authorized_reviewer` | Auditável | No |
| `change_reason` | Razão da última mudança | Yes | controlled text | `initial_registration` | Não apagar histórico anterior | No |
| `review_status` | Estado da revisão do registro | Yes | controlled vocabulary | `pending_review` | Vocabulário da seção 8 | No |
| `reviewer` | Revisor responsável | No | text | `authorized_reviewer` | Obrigatório quando revisado | `not_applicable`, `pending_verification` |
| `review_date` | Data da revisão | No | ISO date | `2026-01-16` | Obrigatória quando revisado | `not_applicable`, `pending_verification` |
| `comments` | Comentários adicionais | No | text | `not_applicable` | Não usar para substituir campos estruturados | `not_applicable` |

## 4. Convenção de identificadores, nomes e caminhos

### 4.1 Regras gerais

- Usar somente letras minúsculas ASCII, números, underscore e hífen conforme cada padrão.
- Não usar espaços, acentos ou caracteres especiais.
- Datas sempre em ISO `YYYY-MM-DD`.
- Preservar `original_filename` exatamente como recebido.
- Identificadores não dependem exclusivamente do nome original.
- Versão, snapshot, componente e sequência do arquivo devem impedir sobrescrita.

### 4.2 Padrões

| Element | Pattern | Example |
|---|---|---|
| `source_id` | `<institution_or_portal_slug>` | `example_source` |
| `dataset_id` | `<source_id>_<dataset_slug>` ou slug estável aprovado | `example_source_dataset` |
| `manifest_record_id` | `mfr_<dataset_id>_<snapshot_date>_v<version>_c<component>_f<sequence>` | `mfr_example_source_dataset_2026-01-15_v01_c01_f001` |
| `stored_filename` | `<dataset_id>_<snapshot_date>_v<version>_<component>_f<sequence>.<ext>` | `example_source_dataset_2026-01-15_v01_table_a_f001.csv` |
| RAW path | `01_raw_data/<source_id>/<dataset_id>/<snapshot_date>/` | `01_raw_data/example_source/example_source_dataset/2026-01-15/` |

Versões internas usam sequência com pelo menos dois dígitos (`v01`). Componentes e arquivos usam identificadores estáveis. Um pacote com vários arquivos recebe um registro para o pacote e, quando necessário, registros filhos vinculados para cada arquivo.

## 5. Processo de checksum e integridade

1. Calcular SHA-256 imediatamente após o download e antes de qualquer abertura ou cópia operacional, quando tecnicamente possível.
2. Registrar algoritmo, digest, timestamp e método.
3. Verificar o checksum antes do processamento.
4. Verificar novamente após cópia ou transferência.
5. Não usar MD5 ou SHA-1 como mecanismo principal; hashes fornecidos pelo publicador podem ser registrados adicionalmente, sem substituir SHA-256.
6. Uma divergência altera `integrity_verification_status` para `failed` e `quarantine_status` para `quarantined`.
7. Arquivo em quarentena não pode ser processado, convertido ou usado analiticamente.
8. Registrar incidente, cadeia de custódia e comparação com a origem.
9. Uma nova aquisição exige autorização aplicável e novo `manifest_record_id`; nunca substituir silenciosamente o arquivo com falha.
10. Preservar rastreabilidade entre o registro divergente e qualquer nova cópia.

Métodos aceitáveis futuros incluem ferramentas confiáveis do sistema operacional, bibliotecas padrão ou ferramentas especializadas que produzam SHA-256 reproduzível. A ferramenta definitiva será escolhida somente na implementação autorizada.

## 6. Imutabilidade e cadeia de custódia

- `raw_immutability_status` deve iniciar como `immutable_original` após preservação e verificação.
- Correção manual no original é proibida.
- Renomeação operacional ocorre por cópia; o nome recebido permanece em `original_filename`.
- Conteúdo descompactado é artefato distinto e deve ter rastreabilidade própria; não substitui o arquivo compactado original.
- Conversão de XLSX, PDF, SAS, SPSS, Stata, JSON ou outro formato para CSV/Parquet pertence à camada processada/intermediária, nunca ao RAW original.
- Problemas de encoding, delimitador, cabeçalho, tipos ou valores são documentados em `validation_notes`/`known_limitations`, não corrigidos no original.
- Toda cópia/transferência relevante é acrescentada à cadeia de custódia e seguida de verificação SHA-256.

## 7. Regras de versionamento

| Situation | Required treatment |
|---|---|
| Nova publicação | Novo registro, snapshot e versão; preservar anterior |
| Revisão retroativa | Novo registro; vincular `supersedes_record_id`; documentar revisão |
| Correção do publicador | Nova versão, mesmo `dataset_id`, novo checksum e registro |
| Snapshot de tabela interativa | Registrar seleção, `snapshot_date`, URL/mecanismo e parâmetros disponíveis |
| Substituição silenciosa na origem | Comparar checksum/tamanho/metadados; preservar ambas; registrar incidente de versão |
| Mesmo nome, conteúdo diferente | Novo `stored_filename`, versão e registro; nunca sobrescrever |
| Dataset com vários arquivos | Registro do pacote e/ou registros filhos; `number_of_files` e inventário |
| Arquivo compactado | Preservar arquivo original; registrar conteúdo; derivados separados |
| Suplemento/documentação | Registro próprio ou componente vinculado; não confundir com dados |

## 8. Vocabulários controlados mínimos

| Field | Allowed values |
|---|---|
| `approval_status` | `pending_approval`, `approved`, `approved_with_conditions`, `rejected`, `not_applicable` |
| `access_mechanism` | `web_download`, `interactive_portal_export`, `api`, `authenticated_portal`, `scientific_use_file_request`, `commercial_license`, `email_delivery`, `physical_media`, `other_documented` |
| `commercial_or_public` | `public`, `public_with_registration`, `restricted_scientific`, `commercial`, `mixed`, `unknown` |
| `integrity_verification_status` | `pending`, `verified`, `failed`, `not_applicable` |
| `schema_validation_status` | `pending`, `passed`, `passed_with_warnings`, `failed`, `not_applicable` |
| `row_count_validation_status` | `pending`, `passed`, `passed_with_warnings`, `failed`, `not_applicable` |
| `checksum_validation_status` | `pending`, `verified`, `failed`, `not_applicable` |
| `quarantine_status` | `not_quarantined`, `quarantined`, `released_after_review` |
| `raw_immutability_status` | `pending_preservation`, `immutable_original`, `integrity_failed`, `unauthorized_modification_detected` |
| `review_status` | `pending_review`, `reviewed`, `approved`, `changes_requested`, `rejected` |
| `evidentiary_nature` | `observed_administrative_data`, `observed_survey_data`, `official_survey_estimate`, `official_population_count`, `official_population_estimate`, `official_population_projection`, `projected_panel_estimate`, `regulatory_indication`, `randomized_clinical_trial_evidence`, `contextual_evidence`, `derived_calculation`, `modelled_assumption`, `not_evaluated` |
| `operational_feasibility_decision` | `GO`, `CONDITIONAL_GO`, `CONTEXTUAL_ONLY`, `NO_GO`, `not_available`, `not_evaluated`, `no_independent_classification` |
| `duplicate_status` | `pending`, `unique`, `exact_duplicate`, `possible_duplicate` |
| `latest_known_version_status` | `latest_known`, `superseded`, `unknown` |
| `manual_modification_status` | `not_modified`, `unauthorized_modification_detected`, `unknown` |

Ao automatizar, esses campos não devem permanecer em texto livre. Listas como funções, harmonizações, idiomas, medidas, identificadores e documentos relacionados devem usar representação multivalorada normalizada ou tabela relacionada, não valores concatenados sem padrão.

## 9. Formatos futuros do manifesto

### 9.1 Registro Markdown legível

O dicionário deste documento funciona como template de revisão humana. Um registro Markdown futuro deve usar os mesmos nomes de campo e registrar um valor por campo, com listas claramente delimitadas.

### 9.2 Esquema tabular mínimo futuro

Sem criar CSV/XLSX/banco nesta tarefa, o esquema mínimo para automação deverá conter:

- IDs e aprovação;
- URLs e timestamps de acesso/aquisição;
- nomes/caminho/formato/tamanho;
- SHA-256 e estados de integridade/quarentena;
- versão e período de referência;
- cobertura e unidade de observação;
- esquema, contagens e chaves documentadas/candidatas;
- imutabilidade e cadeia de custódia;
- funções autorizadas/proibidas e decisão operacional;
- auditoria e revisão.

Campos multivalorados: `component_or_table`, `access_restrictions`, `archive_contents`, `language`, coberturas, medidas, exclusões, limitações, nomes de tabela, chaves, identificadores, unidades, funções, harmonizações, documentos e comentários de cadeia de custódia. Na automação, preferir tabelas relacionadas ou arrays estruturados.

Campos obrigatoriamente controlados: todos os vocabulários da seção 8, IDs, datas/timestamps, booleanos, MIME type, encoding, frequência, formato, níveis geográficos e referências de tarefa/decisão.

## 10. EXEMPLO ILUSTRATIVO — NÃO REPRESENTA DATASET ADQUIRIDO

Este exemplo mostra apenas a convenção; não representa download, fonte real ou checksum calculado.

| Field | Illustrative value |
|---|---|
| `manifest_record_id` | `mfr_example_source_dataset_2026-01-15_v01_c01_f001` |
| `dataset_id` | `example_source_dataset` |
| `source_id` | `example_source` |
| `original_filename` | `example_original.ext` |
| `stored_filename` | `example_source_dataset_2026-01-15_v01_component_f001.ext` |
| `relative_raw_path` | `01_raw_data/example_source/example_source_dataset/2026-01-15/` |
| `checksum_algorithm` | `sha256` |
| `checksum_value` | `pending_verification` |
| `integrity_verification_status` | `pending` |
| `raw_immutability_status` | `pending_preservation` |
| `operational_feasibility_decision` | `not_evaluated` |
| `comments` | `Illustrative record only; no acquisition occurred.` |

## 11. Checklist de validação da F0.7

- [x] Fonte, dataset, versão, componente e arquivo são entidades distintas.
- [x] Publicação, acesso, download, período de referência e versão são datas/conceitos separados.
- [x] SHA-256 é o padrão principal obrigatório.
- [x] O arquivo original RAW é imutável.
- [x] Derivados ficam fora do RAW original.
- [x] Divergência de integridade gera quarentena e bloqueia processamento.
- [x] Novas versões não sobrescrevem versões anteriores.
- [x] URL, acesso, versão e licença/restrição possuem campos próprios.
- [x] Decisões funcionais F1.10 podem ser vinculadas por ID e funções autorizadas/proibidas.
- [x] Valores desconhecidos possuem taxonomia explícita e não são inferidos.
- [x] O template define formato Markdown e esquema tabular futuro sem criar artefatos automatizados.
- [x] Nenhum download, checksum real, diretório RAW, código ou análise foi criado/executado.

## 12. Resultado técnico da F0.7

O template atende integralmente ao objetivo documental da F0.7. Sua aprovação formal permanece pendente do usuário. Implementação, criação do manifesto operacional, aquisição, checksums reais e validação de arquivos somente poderão ocorrer em tarefas futuras autorizadas.
