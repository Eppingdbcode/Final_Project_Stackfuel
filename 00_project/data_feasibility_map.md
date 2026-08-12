# Data Feasibility Map — Consolidated Sources

**Project:** GLP-1/GIP in Germany  
**Consolidation date:** 2026-08-10  
**Scope:** approved feasibility assessments F1.2–F1.8  
**Method:** internal consolidation only; no new external research, download, join, calculation or estimate was performed.

## 1. Resumo executivo

O conjunto avaliado oferece base adequada para funções diferentes, mas não forma uma base única diretamente integrável.

- **Base adequada:** o Destatis Demographics foi aprovado como denominador demográfico oficial; o WIdO/PharMaAnalyst fornece utilização e despesa ambulatorial reembolsada pelo GKV; o RKI/GEDA fornece o baseline epidemiológico oficial de obesidade adulta; e o Destatis Disease Costs fornece o baseline econômico oficial nacional de custos diretos atribuídos a diabetes e obesidade.
- **Uso condicionado à harmonização:** prevalências e denominadores exigem compatibilidade de população, ano, período de referência, idade, sexo e geografia. Dados clínicos exigem correspondência de medicamento, marca, indicação, dose, status de diabetes, estimando e horizonte.
- **Evidência contextual:** o RKI Diabetes foi aprovado como `CONTEXTUAL DATASET` para prevalência e incidência documentadas de diabetes no GKV, sem isolamento confiável de diabetes tipo 2. As fontes públicas da IQVIA foram aprovadas como `CONTEXTUAL DATASET`, com uso apenas contextual e para valores pontuais rigorosamente rotulados.
- **Mensuração direta inviável com as fontes públicas avaliadas:** população clinicamente apropriada, população efetivamente coberta para GLP-1/GIP, mercado self-pay, pacientes autofinanciados, indicação clínica nas fontes de mercado, persistência real alemã e custos evitáveis não são diretamente observados.
- **Modelled assumptions futuras:** projeção própria ou atualização epidemiológica para 2026, passagem de prevalência para elegibilidade clínica, participação do GKV nos custos por doença, proporção de diabetes tipo 2, fração de custos evitável, uptake, adesão, persistência, efetividade real e extrapolações além dos horizontes observados.

Este mapa não emite a decisão formal consolidada da Fase 1. Essa decisão pertence à F1.10.

## 2. Legenda metodológica

| Categoria | Definição operacional | Regra de uso |
|---|---|---|
| `observed administrative data` | Registros administrativos produzidos para faturamento, vigilância ou gestão pública | Preservar universo, regras de inclusão, codificação e cobertura; não chamar de população total |
| `observed survey data` | Respostas ou medidas registradas diretamente em uma pesquisa amostral | Não confundir observação individual com estimativa populacional ponderada |
| `official survey estimate` | Estimativa oficial ponderada proveniente de pesquisa amostral | Preservar desenho, pesos, população-alvo, período e incerteza |
| `official population count` | Contagem censitária oficial referente ao dia censitário | Não usar como rótulo genérico para toda estatística populacional |
| `official population estimate` | População oficial atualizada a partir do censo e dos componentes demográficos | Preservar data de referência e base censitária |
| `official population projection` | Cenário oficial condicionado a hipóteses e variante publicada | Não apresentar como contagem observada; registrar a variante |
| `projected panel estimate` | Estimativa de mercado projetada a partir de painel amostral/proprietário | Não tratar como registro administrativo integral nem extrapolar valores pontuais |
| `company-reported figure` | Valor pontual publicado por uma empresa sem dados subjacentes públicos reutilizáveis | Usar apenas dentro da definição, período, métrica e cobertura divulgados |
| `regulatory indication` | Indicação, população, dose e condições autorizadas constantes da documentação regulatória | Não equivale a indicação clínica individual, tratamento ou reembolso |
| `randomized clinical trial evidence` | Resultado de ensaio randomizado na população, intervenção, comparador e horizonte estudados | Preservar estimando, incerteza, dose, população e limitações de validade externa |
| `contextual evidence` | Evidência útil para interpretação, validação ou delimitação, sem sustentar sozinha a estimativa central | Não promover a dataset quantitativo completo |
| `derived calculation` | Transformação reproduzível de dados observados, estimados ou projetados | Documentar fórmula, fonte, unidade e harmonização; manter separado da origem |
| `modelled assumption` | Valor não diretamente observado, definido por hipótese, extrapolação ou cenário | Justificar, versionar e submeter a análise de sensibilidade |

As categorias não são equivalentes. Um valor pode ser oficial e ainda assim ser estimativa ou projeção, e não uma contagem observada.

## 3. Tabela mestra de fontes

### 3.1 Fontes administrativas, epidemiológicas e econômicas

| ID | Fonte e instituição | Domínio e cobertura | Exclusões relevantes | Período e atualização | Granularidade | Métrica e unidade | Acesso público | Natureza | Feasibility aprovada e papel | Origem interna |
|---|---|---|---|---|---|---|---|---|---|---|
| `WIDO-PMA` | PharMaAnalyst / GKV-Arzneimittelindex — WIdO | Prescrições ambulatoriais cobradas do GKV por farmácias públicas e farmácias hospitalares na assistência ambulatorial; mais de 70 milhões de segurados | Receitas privadas, self-pay, OTC não reembolsado e uso hospitalar; indicação clínica não observada | Cobertura publicada 2012–2024; portal descrito como disponível desde 2016; anual; calendário exato desconhecido | Alemanha; ano; medicamento, princípio ativo e ATC; idade/sexo públicos não confirmados | Prescrições; DDD; custos líquidos absolutos, por prescrição e por DDD; EUR e contagens | Portal HTML/tabela interativa com exportação; extensão do arquivo e API pública desconhecidas; sem login confirmado | `observed administrative data` ajustado à estatística KV 45 | `CONDITIONAL GO`; utilização e despesa ambulatorial reembolsada pelo GKV | `00_project/feasibility/wido.md` |
| `GKV-GAMSI` | GKV-Arzneimittel-Schnellinformation — GKV-Spitzenverband | Mercado farmacêutico agregado do GKV | Não avaliada como substituta para séries por princípio ativo; demais dimensões não confirmadas na F1.2 | Desconhecido nesta avaliação | Agregada; chaves detalhadas desconhecidas | Tendências agregadas do mercado GKV; unidades específicas não consolidadas | Portal oficial `https://www.gkv-gamsi.de/`; formato não avaliado | `contextual evidence` | Fonte complementar de validação; sem classificação independente e sem autorização para substituir o PharMaAnalyst | `00_project/feasibility/wido.md` |
| `RKI-DIAB-PREV` | Prävalenz dokumentierter Diabetes — RKI Diabetes Surveillance | Adultos ≥18 anos residentes na Alemanha, segurados pelo GKV por ≥360 dias e com cobertura integral; diabetes documentado E10–E14 | PKV; diabetes não documentado; T2D não isolado com confiança | Resultados públicos confirmados para 2011 regional e 2013 por idade/sexo; série adicional no XLSX desconhecida | Alemanha; estado federal; ano; sexo; faixa etária | Número absoluto, prevalência e estimativa padronizada por idade | Página HTML/visualização e XLSX público; sem login; API desconhecida | `observed administrative data` e estimativas derivadas desses registros | `CONTEXTUAL DATASET`; contexto de prevalência documentada de diabetes no GKV | `00_project/feasibility/rki_diabetes.md` |
| `RKI-DIAB-INC` | Inzidenz dokumentierter Diabetes — RKI Diabetes Surveillance | Mesmo universo adulto GKV; novo diabetes após um ano anterior sem diagnóstico | PKV; T2D não isolado; washout limitado a um ano | Ano público confirmado: 2012; anos adicionais no XLSX desconhecidos | Alemanha; ano; sexo e faixa etária; estado para incidência não confirmado | Número absoluto e incidência | Página HTML/visualização e XLSX público; sem login; API desconhecida | `observed administrative data` e estimativas derivadas desses registros | `CONTEXTUAL DATASET`; contexto de incidência documentada, não base longitudinal exclusiva de T2D | `00_project/feasibility/rki_diabetes.md` |
| `RKI-GEDA-AGG` | GEDA 2019/2020-EHIS e publicação de tendências até 2023 — RKI | Adultos em domicílios privados na Alemanha; pesquisa nacional por CATI | Pessoas fora da população-alvo da pesquisa; diagnóstico e cobertura GKV não observados | Ondas 2009, 2010, 2012, 2014/2015 e 2019/2020; estimativas agregadas de 2022 e 2023; atualização não anual garantida | Nacional; ano/onda; idade; sexo; educação; estado no dashboard, sujeito à precisão | Prevalência ponderada de overweight/obesity; BMI calculado de peso e altura autorrelatados; porcentagem e IC quando publicados | Publicações PDF/HTML e dashboard; CSV/XLSX/API do dashboard não confirmados | `official survey estimate`; respostas individuais são `observed survey data` | `CONDITIONAL GO`; baseline oficial de prevalência de obesidade adulta e segmentação publicamente verificada | `00_project/feasibility/rki_obesity_geda.md` |
| `RKI-GEDA-SUF` | GEDA Scientific Use Files — FDZ/RKI | Microdados anonimizados das ondas GEDA | Uso comercial excluído; acesso condicionado; classes de BMI, comorbidades e pesos ainda não verificados tecnicamente | SUFs confirmados até 2019/2020 | Potencialmente individual; variáveis e precisão por segmento dependem do dicionário e do arquivo | Respostas e variáveis do survey; unidade por variável ainda a confirmar | Solicitação formal, justificativa científica, contrato; SAS, SPSS e Stata; CSV/XLSX não nativos; sem acesso obtido | `observed survey data` com estimativas futuras ponderadas | `CONDITIONAL GO`; segmentações customizadas e classes de obesidade somente após verificação técnica e acesso | `00_project/feasibility/rki_obesity_geda.md` |
| `DESTATIS-KK` | Krankheitskostenrechnung, estatística 23631 — Destatis | Custos diretos nacionais atribuídos a diagnósticos no sistema de saúde alemão | Não separa pagador/GKV; E10–E14 não isola T2D; E65–E68 é mais amplo que obesidade isolada; não mede custo evitável | 2002, 2004, 2006, 2008, 2015, 2020 e 2023; séries 2002–2008 e 2015–2023 separadamente comparáveis; continuidade anual planejada a partir de 2023 | Alemanha; ano; ICD-10; sexo; grupo etário; tipo de estabelecimento em tabela específica | Custos diretos em milhões de EUR e custos por habitante | GENESIS/tabela interativa com download; formato final e API para aquisição ainda não selecionados | Estimativa oficial de custos por doença baseada em abordagem top-down | `CONDITIONAL GO`; baseline econômico oficial nacional, não estimativa direta do GKV ou de custos evitáveis | `00_project/feasibility/destatis_disease_costs.md` |
| `DESTATIS-POP` | Fortschreibung des Bevölkerungsstandes, tabelas 12411-0013, 12411-0041 e 12411-0020 — Destatis | População residente registrada na Alemanha; nacional e estados | Não identifica GKV, diagnóstico, BMI ou elegibilidade; universo difere de surveys domiciliares | 12411-0013: 31/12/1967–2025; 12411-0041 inclui média anual de 2025; 12411-0020 chega a 31/03/2026 sem idade | Ano/data; idade individual nas tabelas detalhadas; sexo; estado; nacionalidade em tabelas específicas | Pessoas | GENESIS, CSV, flat-file CSV, XLSX e REST/JSON; autenticação geralmente necessária; limite interativo de 40.000 valores | `official population estimate`; Censo 2022 no dia censitário é `official population count` | `GO`; denominador demográfico oficial compatível com o período epidemiológico | `00_project/feasibility/destatis_demographics.md` |
| `DESTATIS-PROJ` | 16ª projeção coordenada, tabelas 12421-0002 e 12421-0004 — Destatis | Cenários populacionais nacional e estaduais | Não representa população observada; depende da variante; não identifica GKV ou condições clínicas | Base 31/12/2024; 2025–2070, incluindo 31/12/2026 | Ano/data; variante; idade individual; sexo; estado | Pessoas projetadas | GENESIS, formatos reutilizáveis e API nas condições do portal | `official population projection` | `GO` como cenário demográfico; variante deve ser escolhida e justificada posteriormente | `00_project/feasibility/destatis_demographics.md` |

### 3.2 Mercado contextual, regulação e evidência clínica

| ID | Fonte e instituição | Domínio e cobertura | Exclusões relevantes | Período e atualização | Granularidade | Métrica e unidade | Acesso público | Natureza | Feasibility aprovada e papel | Origem interna |
|---|---|---|---|---|---|---|---|---|---|---|
| `IQVIA-PUBLIC` | Flashlight, infográficos, Marktberichte e páginas públicas — IQVIA Germany | Recortes do mercado farmacêutico alemão, painéis PharmaScope/DPM, GKV, receitas privadas e canais específicos conforme publicação | Não separa self-pay, receita privada de segurado GKV e reembolso PKV; indicação, pacientes e adesão não observados; vendas sem receita não são componente relevante para GLP-1/GIP de prescrição obrigatória | Valores pontuais de 2022–2025 conforme publicação; frequência de uma série GLP-1 pública não aplicável | Período/ATC/produto/canal apenas quando impresso; seleção subjacente não reproduzível | Units, pacotes, vendas/faturamento a APU, crescimento e participações; não equivalem a pacientes ou gasto líquido | PDF/HTML/infográfico; sem série pública CSV/XLSX/API ou microdados; núcleo detalhado é proprietário/licenciado | `projected panel estimate`, `company-reported figure` e contexto metodológico | Geral `CONTEXTUAL DATASET`; `NO-GO` como dataset quantitativo reproduzível; `GO` para contexto/valores pontuais; `NO-GO` para quantificação pública do self-pay | `00_project/feasibility/iqvia_public_sources.md` |
| `DE-REG-CONTEXT` | G-BA, BMG e BfArM | Regras de reembolso, prescrição, mercado legal, disponibilidade e uso apropriado na Alemanha | Não fornece volumes, pacientes ou valor do mercado self-pay | Datas específicas das decisões/páginas registradas na avaliação IQVIA | Produto/indicação/regra quando publicada | Regra administrativa ou regulatória; sem unidade de mercado | HTML público | `contextual evidence` e evidência regulatória/administrativa oficial | Delimitação de reembolso e mercado legal; inadequada para inventar volumes | `00_project/feasibility/iqvia_public_sources.md` |
| `EMA-REG` | EPARs, Product Information/SmPCs e assessment reports — EMA | Wegovy, Ozempic, Rybelsus, Mounjaro, Saxenda e Victoza; indicação, população, dose e segurança por marca | Não define reembolso GKV, apropriação clínica individual, tratamento ou uptake | Versões e datas por produto registradas; data de acesso 2026-08-10 | Marca; princípio ativo; indicação; idade; BMI; comorbidade; dose; regra regulatória | Critério normativo; não é métrica de prevalência | HTML e PDF públicos | `regulatory indication` | Geral `CONDITIONAL GO`; `GO` para definição da população regulatoriamente elegível, sem calcular seu tamanho | `00_project/feasibility/ema_clinical_evidence.md` |
| `CLINICAL-RCT` | STEP, SURMOUNT, SURPASS, SCALE, SELECT, LEADER, FLOW e outros ensaios primários | Populações clínicas específicas com e sem T2D, doses, comparadores e horizontes definidos | Validade externa limitada; não mede efetividade ou persistência real alemã; não autoriza extrapolação entre populações | Horizonte próprio de cada ensaio; nenhuma série populacional contínua | Medicamento/marca quando relevante; dose; população; diabetes; estimando; endpoint; horizonte | Mudança de peso/BMI/HbA1c, HR, proporções, eventos adversos, descontinuação e incerteza | Publicações e documentos regulatórios; dados subjacentes/microdados não avaliados como públicos | `randomized clinical trial evidence`; extensões e withdrawal studies mantidas separadas | Geral `CONDITIONAL GO`; parâmetros clínicos condicionados à correspondência exata; persistência de longo prazo apenas contextual | `00_project/feasibility/ema_clinical_evidence.md` |

### 3.3 Nomenclatura interna não sustentada como fonte separada

O escopo autorizado menciona “WIdO / Arzneimittel-Kompass”. O arquivo aprovado da F1.2 avalia **WIdO / PharMaAnalyst** e não documenta uma avaliação independente denominada Arzneimittel-Kompass. Para preservar rastreabilidade e não inventar cobertura, nenhum registro separado foi criado com esse nome. O GKV-GAmSi foi mantido como fonte complementar, exatamente no papel limitado documentado pela F1.2.

## 4. Cobertura por função analítica

| Função | Fonte principal | Complementar | Cobertura | Uso permitido | Limitação principal | Harmonização | Modelled assumption futura |
|---|---|---|---|---|---|---|---|
| População residente | `DESTATIS-POP` | `DESTATIS-PROJ` para cenário 2026 | Disponível | Denominador oficial por idade, sexo, ano e estado quando compatível | Não representa GKV nem população clínica | Data, base censitária, idade, sexo e geografia | Não para anos observados; sim se houver extrapolação própria |
| Prevalência de obesidade | `RKI-GEDA-AGG` | `RKI-GEDA-SUF` condicional | Disponível nacionalmente; parcialmente disponível para classes/segmentos customizados | Baseline adulto por ano/onda, idade, sexo e educação; estado sujeito à precisão | Peso e altura autorrelatados; não é diagnóstico | População-alvo, período, faixas e pesos | Sim para atualização/projeção a 2026 e elegibilidade |
| Prevalência de diabetes | Nenhuma fonte principal para T2D exclusivo | `RKI-DIAB-PREV` contextual | Parcialmente disponível para diabetes documentado E10–E14 no GKV | Contexto epidemiológico e segmentação documentada | T2D não isolado com confiança e cobertura temporal curta | Universo GKV, ano, idade, sexo e estado | Sim se separar T2D sem observação direta |
| População regulatoriamente elegível | `EMA-REG` define critérios, não tamanho | `RKI-GEDA-AGG`, `DESTATIS-POP` | Critérios disponíveis; quantidade não disponível | Aplicar futuramente critérios por marca, BMI, idade e comorbidades | Prevalência não contém todos os critérios e contraindicações | BMI, idade, comorbidade, marca e período | Sim |
| População clinicamente apropriada | Nenhuma | EMA e epidemiologia apenas delimitam | Não disponível | Apenas cenário futuro com regras clínicas aprovadas | Avaliação individual, contraindicações e preferência não observadas | Extensa | Sim |
| População coberta pelo GKV | Nenhuma fonte única para elegibilidade/tratamento | RKI Diabetes e WIdO cobrem universos GKV distintos | Parcialmente disponível | Descrever universos observados de cada fonte | População residente ≠ segurados GKV; cobertura do medicamento depende de indicação | Universo, regra de inclusão, indicação e ano | Sim para participação não observada |
| Consumo ou despesa no GKV | `WIDO-PMA` | `GKV-GAMSI` para validação agregada | Disponível com condições | Prescrições, DDD e custos líquidos ambulatoriais reembolsados | Sem indicação; formato de exportação não confirmado; painel anual pode ser desequilibrado | ATC por ano, substância, marca e unidade | Não para observado; sim para indicação/uso não identificado |
| Consumo fora do GKV | Nenhuma fonte quantitativa pública principal | `IQVIA-PUBLIC` contextual | Parcial, apenas recortes | Contextualizar existência e ordem de grandeza quando publicada | Canal, pagador, indicação e paciente não separáveis | Métrica, preço, período, canal e produto | Sim se quantificado sem fonte direta |
| Mercado autofinanciado | Nenhuma | IQVIA e regras oficiais apenas contextuais | Não disponível publicamente de forma defensável | Não estimar como resultado central com as fontes atuais | Private prescription ≠ self-pay; PKV e GKV pagando privadamente não separáveis | Incompatibilidade material | Sim, ou fonte comercial/nova fonte |
| Perda de peso | `CLINICAL-RCT` | `EMA-REG` | Disponível com condições | Parâmetro por medicamento, marca, dose, população, diabetes, estimando e horizonte | Eficácia de ensaio ≠ efetividade real | Obrigatória em todos os metadados clínicos | Sim além do horizonte/para prática real |
| Controle glicêmico | `CLINICAL-RCT` | `EMA-REG` | Disponível com condições em T2D | Usar ensaios compatíveis e terapia de fundo | Não transferir a população sem T2D | HbA1c basal, terapia, dose, horizonte e estimando | Sim para extrapolação |
| Descontinuação | `CLINICAL-RCT` | SmPC | Disponível com condições | Separar qualquer causa de evento adverso | Não equivale a persistência real; run-in pode selecionar toleradores | Definição, período e população | Sim para prática real/horizonte longo |
| Eventos adversos | `CLINICAL-RCT` | `EMA-REG` | Disponível com condições | Frequência e segurança por produto/dose/população | Eventos raros podem exigir farmacovigilância | Definição, gravidade, dose e horizonte | Possivelmente |
| Eventos cardiovasculares | Ensaios correspondentes, incluindo SELECT/LEADER | EMA | Disponível somente para populações estudadas | SELECT apenas em sobrepeso/obesidade + CVD estabelecida sem diabetes; outros CVOTs em T2D compatível | Não generalizar a obesidade geral | Risco basal, diabetes, dose e endpoint | Sim fora da população/horizonte |
| Eventos renais | FLOW | EMA | Disponível para T2D + DRC estudados | Aplicação restrita à população e desfecho composto do FLOW | Não generalizar para toda obesidade | T2D, DRC, dose, risco e endpoint | Sim fora da população/horizonte |
| Persistência do efeito | Extensões e withdrawal studies | RCTs em tratamento | Apenas evidência contextual de longo prazo | Informar manutenção observada e recuperação após retirada | Não define curva vitalícia nem persistência real | Desenho, seleção e horizonte | Sim |
| Comparação entre medicamentos | Head-to-head randomizado ou método formal futuro | Nenhuma comparação descritiva simples | Condicional | SURPASS-2/SURMOUNT-5 somente nas populações e doses estudadas; indireta apenas com método formal | Percentuais brutos entre STEP/SURMOUNT/SCALE não estimam superioridade | População, comparador, dose, estimando e horizonte | Possível em cenário formal validado |
| Parâmetros para modelo econômico posterior | Destatis Costs + evidência clínica + epidemiologia + demografia | WIdO e contexto de mercado | Parcial e condicional | Alimentar módulos separados após especificação e validação | Não existem custos automaticamente evitáveis nem participação GKV por diagnóstico | Todas as dimensões relevantes | Sim para participação GKV, T2D, evitabilidade, uptake e extrapolação |

## 5. Formatos e acessibilidade

| Fonte | Relatório público | Tabela estruturada pública | Série reproduzível | Microdados | Acesso comercial/proprietário | Situação operacional |
|---|---|---|---|---|---|---|
| WIdO/PharMaAnalyst | HTML e documentação PDF | Tabela interativa com exportação | Potencialmente anual; extensão do export desconhecida | Não confirmado | Não aplicável ao portal avaliado | Acesso público sem login confirmado; não baixar antes da aprovação |
| GKV-GAmSi | Portal oficial | Desconhecido nesta avaliação | Desconhecido | Desconhecido | Não confirmado | Apenas complemento contextual aprovado |
| RKI Diabetes | HTML/visualizações | XLSX público | Conteúdo temporal completo ainda desconhecido sem inspeção | Não avaliado | Não | Sem login; arquivos ainda não baixados |
| RKI/GEDA agregado | PDF/HTML/dashboard | Tabelas publicadas; export do dashboard não confirmado | Estimativas agregadas por onda/ano publicado | Não no componente agregado | Não | Reproduzível apenas no nível publicado |
| RKI/GEDA SUF | Documentação pública | Não aplicável | Requer processamento do microdado | SAS, SPSS e Stata, mediante solicitação/contrato | Uso comercial excluído | Acesso ainda não obtido; dicionário e variáveis não verificados |
| Destatis Disease Costs | HTML/GENESIS | Tabelas GENESIS com download | Potencialmente reproduzível | Não aplicável | Não | Formato de aquisição ainda não selecionado |
| Destatis Demographics | HTML/GENESIS | CSV, flat-file CSV, XLSX e REST/JSON | Sim, com seleção e metadados versionados | Não aplicável | Não | API geralmente autenticada; limite interativo de 40.000 valores |
| IQVIA pública | PDF, HTML e infográfico | Não para série GLP-1 self-pay | Não | Não | Sim, núcleo detalhado licenciado | Valores pontuais apenas; preservar métrica, período, cobertura e preço |
| EMA | HTML e PDF | Documentos regulatórios estruturados, não dataset tabular único | Reprodutível por extração documentada de critérios | Não avaliado | Não | Versão do documento deve ser registrada |
| Ensaios clínicos | Artigos e documentos regulatórios | Tabelas publicadas por estudo | Parâmetros podem ser extraídos com protocolo | Microdados não avaliados | Pode haver restrições por estudo | Extração somente em fase autorizada |

## 6. Chaves e possibilidades de integração

| Chave | Fontes em que aparece | Disponibilidade | Harmonização/incompatibilidade | Risco de perda de granularidade |
|---|---|---|---|---|
| Ano/período | Todas, com definições diferentes | Direta, salvo séries desconhecidas | Ano civil, onda, MAT, trimestre, data censitária e horizonte clínico não são equivalentes | Alto ao reduzir períodos distintos a um único ano |
| Trimestre | Destatis 12411-0020; algumas publicações IQVIA | Parcial | Resultado trimestral não substitui média ou fim de ano; IQVIA pode usar Q/MAT | Alto |
| Idade individual | Destatis atual/projeção | Direta | Deve ser agregada às faixas da prevalência, nunca o contrário | Baixo se agregado corretamente; alto se criar falsa precisão |
| Faixa etária | RKI/GEDA, RKI Diabetes, Destatis Costs, ensaios | Direta, mas categorias distintas | Harmonizar pelo maior agrupamento comum e preservar limites abertos | Médio/alto |
| Sexo | Destatis, RKI/GEDA, RKI Diabetes, Destatis Costs | Direta em parte | Categorias e disponibilidade por ano precisam ser verificadas | Médio |
| Estado federal | Destatis, RKI/GEDA e prevalência RKI Diabetes | Disponível com condições | Precisão amostral/epidemiológica pode impedir uso apesar do denominador disponível | Alto em segmentos pequenos |
| Educação/condição socioeconômica | RKI/GEDA | Parcialmente disponível | Não possui chave equivalente principal nas outras fontes avaliadas | Alto |
| Substância/nome | WIdO e alguns recortes IQVIA; evidência clínica | Direta ou textual | Padronizar nomes; substância não identifica marca, indicação ou pagador | Médio |
| ATC | WIdO e IQVIA quando publicado | Direta em parte | Classificação pode variar por ano; cobertura ATC4 não equivale a produto | Médio/alto |
| Marca | EMA, ensaios e alguns materiais de mercado | Parcial | Marcas do mesmo princípio ativo não são intercambiáveis | Alto se reduzida a substância |
| Indicação | EMA e população definida dos ensaios | Não observada nas fontes de mercado | Não pode ser inferida por molécula, marca ou canal | Muito alto |
| Status de diabetes | Ensaios; RKI Diabetes mede diabetes agregado; GEDA SUF não confirmado | Parcial | Com/sem T2D dos ensaios não equivale a E10–E14 documentado | Alto |
| BMI/categoria de BMI | GEDA e ensaios; EMA define limiares | Parcial | Autorrelato, classes não publicadas separadamente e critérios regulatórios adicionais | Alto |
| ICD-10 | RKI Diabetes e Destatis Costs | Direta em grupos | E10–E14 não isola T2D; E65–E68 não é obesidade isolada | Alto |
| Pagador | WIdO = GKV; IQVIA usa categorias; Destatis Costs não separa | Parcial/incompatível | Private prescription, PKV e self-pay não são equivalentes | Muito alto |
| Canal | IQVIA e escopo WIdO | Parcial | Sell-in, sell-out, farmácia pública, mail order e hospital não são equivalentes | Alto |
| Endpoint | Ensaios clínicos | Direta por estudo | Preservar definição, medida de efeito e hierarquia | Alto |
| Horizonte temporal | Ensaios e modelo futuro | Direta por estudo | Não extrapolar além do acompanhamento sem assumption | Alto |

Não existe ligação individual entre as fontes. Qualquer integração futura será agregada, dependerá de validação semântica e poderá exigir perda controlada de granularidade.

## 7. Matriz de compatibilidade

| Combinação | Finalidade | Compatibilidade | Transformação futura necessária | Risco metodológico | Classificação operacional |
|---|---|---|---|---|---|
| RKI/GEDA × Destatis Population | Converter prevalência de obesidade em número absoluto | Compatível sob condições | Alinhar população-alvo, ano/período, idade, sexo e geografia; agregar idades | Autorrelato, diferença entre domicílios privados e residentes, período e falsa precisão | Utilizável com harmonização |
| RKI Diabetes × denominador GKV compatível | Contextualizar número/taxa de diabetes documentado | Parcial | Usar denominador do mesmo universo e regra; não substituir por população residente | E10–E14, cobertura temporal e denominador incompatível | Cenário/contexto; não base exclusiva de T2D |
| EMA eligibility × RKI/GEDA × Destatis | Aproximar população regulatoriamente elegível | Parcial | Aplicar critérios por marca e comorbidade no nível suportado | Prevalência não mede todos os critérios; obesidade ≠ elegibilidade | Cenário; exige modelled assumptions |
| WIdO × GKV-GAmSi | Validar tendências agregadas do GKV | Potencial | Alinhar período, métrica e cobertura | GAmSi não foi avaliado como série por substância | Utilizável apenas para validação contextual |
| WIdO GKV × IQVIA mercado | Contextualizar GKV versus mercado mais amplo | Incompatível para subtração direta | Alinhar produtos, canais, unidades, preços, período e projeção | Não isola self-pay; painel projetado versus administração; APU versus custo líquido | Contextual; inadequada para calcular self-pay por diferença |
| Ensaios clínicos × segmentos epidemiológicos | Aplicar parâmetros de efeito a subgrupos | Parcial | Correspondência de medicamento, marca, dose, diabetes, BMI, risco, estimando e horizonte | Validade externa e heterogeneidade | Utilizável com harmonização/cenários |
| SELECT × obesidade geral | Estimar eventos cardiovasculares | Incompatível fora do subgrupo estudado | Restringir a CVD estabelecida, sobrepeso/obesidade e ausência de diabetes | Generalização indevida | Inadequada fora da população; cenário dentro dela |
| FLOW × obesidade geral | Estimar eventos renais | Incompatível fora do subgrupo estudado | Restringir a T2D + DRC e endpoint correspondente | Generalização indevida | Inadequada fora da população; cenário dentro dela |
| Destatis Disease Costs × GKV | Construir baseline econômico GKV | Parcial | Identificar participação defensável do GKV por fonte adicional | Custos nacionais sem pagador; dupla contagem e multimorbidade | Cenário; exige fonte adicional/assumption |
| Efeitos clínicos × custos por doença | Estimar custos evitáveis | Não diretamente compatível | Modelo causal/econômico explícito, horizonte e fração evitável | Perda de peso não é conversor automático de evento/custo | Cenário; inadequada como conversão direta |
| Efeito observado × horizonte econômico posterior | Extrapolar benefícios e custos | Parcial | Curvas e assumptions documentadas, com sensibilidade | Persistência, adesão, recuperação e risco basal | Cenário/modelled assumption |

Nenhum join, cálculo ou resultado numérico derivado foi produzido nesta consolidação.

## 8. Lacunas críticas

1. As fontes de mercado não identificam diretamente a indicação clínica; uso para diabetes, controle de peso e off-label não pode ser inferido automaticamente.
2. Prescrições, DDD, vendas, pacotes, units, dispensações e pacientes são métricas diferentes; nenhuma conversão automática é válida.
3. Private prescriptions não equivalem automaticamente a self-pay: podem representar pagamento direto de segurado GKV ou possível reembolso PKV.
4. Não existe mensuração pública reproduzível e defensável do mercado alemão autofinanciado de GLP-1/GIP nas fontes avaliadas.
5. População residente, população em domicílios privados, população segurada pelo GKV, população diagnosticada, população regulatoriamente elegível e população clinicamente apropriada são universos diferentes.
6. Faixas etárias, categorias de sexo, geografia e períodos de referência diferem entre as fontes e podem exigir agregação ao maior nível comum.
7. O GEDA utiliza peso e altura autorrelatados, com provável subestimação do BMI; classes I–III não estão aprovadas como disponíveis até a inspeção do SUF e do dicionário.
8. O RKI Diabetes adulto principal agrega E10–E14 e não sustenta isolamento longitudinal confiável de T2D.
9. O Destatis Disease Costs agrega E10–E14 e E65–E68, não separa pagador e não mede automaticamente custos evitáveis.
10. A série populacional possui quebras/revisões associadas aos Censos 2011 e 2022; população de 31/03/2026 não equivale à média anual de 2026.
11. Qualquer população anual detalhada de 2026 baseada na 16ª projeção deverá preservar a classificação `official population projection` e a variante escolhida.
12. Eficácia em ensaio não equivale a efetividade real alemã; médias não podem ser aplicadas indiscriminadamente a todos os elegíveis.
13. Persistência real, adesão, descontinuação fora de ensaios e recuperação de peso no longo prazo permanecem insuficientemente observadas.
14. SELECT e FLOW são aplicáveis somente às populações estudadas; seus resultados não podem ser generalizados para toda pessoa com obesidade.
15. Percentuais brutos de STEP, SURMOUNT e SCALE não permitem ranking ou superioridade relativa. Comparações exigem head-to-head randomizado ou método formal defensável.
16. Transferibilidade demográfica e clínica dos ensaios para a Alemanha exige estratificação, validação e cenários.
17. Fontes adicionais ou assumptions serão necessárias para participação do GKV nos custos por doença, T2D, fração evitável, efetividade real, uptake, adesão, persistência e self-pay.
18. Ausência de evidência nunca será transformada em efeito zero.

## 9. Função aprovada de cada fonte

| Fonte | Funções aprovadas | Funções condicionais | Funções inadequadas/NO-GO |
|---|---|---|---|
| WIdO/PharMaAnalyst | Utilização GKV; despesa GKV | Série por substância após confirmar exportação, anos e presença; validação de tendências | Mercado total, self-pay, pacientes, indicação clínica |
| GKV-GAmSi | Validação/contextualização agregada | Nenhuma função quantitativa adicional aprovada | Substituir silenciosamente o WIdO por série de substância |
| RKI Diabetes | Contextualização da prevalência e incidência documentadas no GKV | Segmentações e conteúdo adicional após inspeção dos XLSX | Base principal exclusiva para T2D |
| RKI/GEDA agregado | Prevalência e segmentação adulta por dimensões publicamente verificadas | Estado sujeito à precisão; atualização para cenários | Diagnóstico, GKV ou elegibilidade automática |
| RKI/GEDA SUF | Nenhuma antes de acesso/verificação | Classes de BMI, estado e segmentações customizadas | Tratar classes como disponíveis antes da verificação técnica |
| Destatis Demographics | Denominador oficial; segmentação demográfica | Estado e projeção 2026 com compatibilidade/variante documentada | GKV, diagnóstico, BMI ou elegibilidade clínica |
| Destatis Disease Costs | Baseline econômico oficial nacional; segmentação de custos | Parâmetros econômicos após fontes para pagador/T2D/evitabilidade | Custo direto do GKV ou custo automaticamente evitável |
| IQVIA pública | Contexto de mercado e valores pontuais rotulados | Validação qualitativa de demanda fora do GKV | Dataset quantitativo reproduzível, estimativa central self-pay, pacientes ou uptake |
| G-BA/BMG/BfArM | Delimitação regulatória, reembolso e mercado legal | Validação contextual | Inferir volumes ou pacientes |
| EMA | Elegibilidade regulatória por marca; dose e regras normativas | Aplicação futura dos critérios à epidemiologia | Reembolso, cobertura, apropriação clínica individual ou tratamento observado |
| Ensaios clínicos | Parâmetros clínicos dentro de população/dose/estimando/horizonte | Peso, glicemia, segurança, descontinuação, CV/renal e comparações formais | Generalização, ranking bruto, persistência real ou custos evitáveis automáticos |

Uma mesma fonte mantém classificações diferentes por função. Nenhuma decisão funcional foi substituída por uma classificação global simplificada.

## 10. Regras operacionais para fases posteriores

1. Preservar todos os dados originais em `01_raw_data`; nunca sobrescrever arquivos RAW.
2. Registrar URL, data de acesso, nome original, versão, período, licença/condição de uso e checksum de cada aquisição.
3. Manter camada processada separada dos arquivos originais.
4. Documentar cada harmonização de período, população, faixa etária, sexo, geografia, código, unidade e categoria.
5. Manter `observed data`, `official estimates`, `official projections`, `derived calculations` e `modelled assumptions` separados e rotulados.
6. Preservar unidade, definição, preço, canal, pagador e universo de cada métrica.
7. Validar chaves e compatibilidade semântica antes de combinar fontes; nomes semelhantes não provam equivalência.
8. Evitar dupla contagem entre diagnósticos, canais, pagadores, marcas, eventos e populações.
9. Não imputar informação ausente nem converter `desconhecido` em `não` sem regra aprovada.
10. Não inferir indicação clínica a partir de substância, marca, ATC, venda ou canal.
11. Não converter vendas/prescrições/DDD/pacotes em pacientes sem metodologia e parâmetros verificados.
12. Para parâmetros clínicos, preservar medicamento e marca quando relevante, dose, população, diabetes, estimando, horizonte, medida de efeito, incerteza, fonte e limitação.
13. Para 2026, registrar se o valor é estimativa oficial, projeção oficial, cálculo derivado ou assumption; nunca chamar projeção de contagem observada.
14. Implementar ingestão e análise em Python/Pandas somente quando a etapa correspondente for autorizada.

## 11. Dívida documental preservada

Sem alterar o `TASKS.md`, permanecem registradas as seguintes inconsistências:

- F1.1–F1.8 ainda aparecem como `TODO`.
- F1.4 aponta para `00_project/feasibility/rki_obesity.md`, embora o entregável aprovado seja `00_project/feasibility/rki_obesity_geda.md`.
- F0.4 permanece como `IN PROGRESS`.
- F0.5 ainda não criou `00_project/decision_log.md`.
- F1.10 depende operacionalmente do decision log, mas essa dependência não está formalmente registrada.
- A seção “Próxima tarefa proposta para aprovação” ainda aponta para F1.1.
- A denominação “WIdO / Arzneimittel-Kompass” não corresponde a uma avaliação independente nos arquivos aprovados; F1.2 documenta WIdO / PharMaAnalyst.

## 12. Validação da consolidação

- [x] F1.2–F1.8 estão representadas e apontam para o arquivo interno aprovado.
- [x] O arquivo válido de F1.4 é `rki_obesity_geda.md`.
- [x] Classificações globais e funcionais foram preservadas.
- [x] Dados administrativos, surveys, estimativas populacionais, projeções, painéis, regulação, RCTs, cálculos derivados e assumptions permanecem separados.
- [x] RKI Diabetes e IQVIA não foram promovidos de fontes contextuais a datasets quantitativos principais.
- [x] SELECT, FLOW e demais ensaios permanecem restritos às populações, doses, estimandos e horizontes correspondentes.
- [x] Nenhuma chave, cobertura, frequência ou formato desconhecido foi inventado.
- [x] Nenhum cálculo, join, download, código ou nova estimativa foi realizado.
- [x] As dívidas documentais foram registradas sem alterar o `TASKS.md`.
- [x] A decisão formal consolidada da F1.10 não foi antecipada.

### Resultado da F1.9

O mapa está **completo para as fontes efetivamente avaliadas e aprovadas em F1.2–F1.8**. Ele é operacional para orientar aquisição, inspeção e futura harmonização, mas não elimina as condições e lacunas registradas. A decisão formal final por dataset e o encerramento da Fase 1 permanecem reservados à F1.10.

## 13. Lista final de aquisição — F2.1

**Data da execução técnica:** 2026-08-11  
**Data da aprovação formal:** 2026-08-11  
**Status final da F2.1:** `DONE`; lista documental formalmente aprovada.  
**Base da decisão:** avaliações F1.2–F1.8, consolidação F1.9, decisão D-011 da F1.10 e padrão de preservação RAW aprovado em F0.7.  
**Limite:** `APPROVED` ou `CONDITIONALLY APPROVED` significa aprovação documental para possível aquisição futura somente após autorização específica da tarefa F2.2–F2.6 correspondente. Não significa arquivo adquirido, presença local, licença definitivamente confirmada, acesso operacional validado ou adequação irrestrita. Nenhuma aquisição foi executada na F2.1; todas as classificações, condições, limitações, riscos e informações pendentes permanecem inalteradas.

### 13.1 Datasets e documentos autorizáveis para aquisição futura

| Acquisition ID | Dataset, documento ou componente | Instituição e URL documental registrada | Território, cobertura e unidade | Período, granularidade e variáveis documentadas | Acesso/formato e licença | Finalidade e relação com o projeto | Condições anteriores à aquisição | Limitações e riscos preservados | Classificação F2.1 | Justificativa |
|---|---|---|---|---|---|---|---|---|---|---|
| `DESTATIS-POP` | Fortschreibung des Bevölkerungsstandes, tabelas `12411-0013`, `12411-0041` e `12411-0020` | Destatis; `https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0013`, `https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0041`, `https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0020` | Alemanha e estados; população residente; pessoas | 1967–2025 na tabela detalhada documentada; média anual de 2025; resultado trimestral até 31/03/2026 sem idade; ano/data, idade, sexo, estado e nacionalidade conforme tabela | GENESIS, CSV, flat-file CSV, XLSX e REST/JSON; autenticação geralmente necessária; condições de reutilização deverão ser registradas no download | Denominador demográfico oficial para converter prevalências em números absolutos | Escolher tabela/data compatível com cada prevalência; registrar base censitária, seleção, versão e licença/termos vigentes | População residente não equivale a GKV, diagnóstico ou elegibilidade; revisões do Censo 2022; limite interativo | `APPROVED` | Fonte oficial, recente, reutilizável e granular, aprovada como denominador oficial |
| `DESTATIS-PROJ` | 16ª projeção coordenada, tabelas `12421-0002` e `12421-0004` | Destatis; `https://genesis.destatis.de/datenbank/online/table/12421-0002/`, `https://genesis.destatis.de/datenbank/online/table/12421-0004/` | Alemanha e estados; população projetada; pessoas | Base 31/12/2024; 2025–2070; ano/data, variante, idade, sexo e estado | GENESIS, formatos reutilizáveis e API nas condições do portal; licença/termos a registrar | Cenário demográfico oficial para 2026 quando necessário | Escolher e justificar variante antes do uso; registrar como `official population projection` | Não é contagem observada; variante e data de referência afetam o resultado | `APPROVED` | Componente oficial adequado ao cenário demográfico, preservada a natureza projetada |
| `WIDO-PMA` | PharMaAnalyst / GKV-Arzneimittelindex | WIdO; `https://www.wido.de/publikationen-produkte/analytik/pharmaanalyst/`, `https://arzneimittel.wido.de/PharMaAnalyst/` | Alemanha; prescrições ambulatoriais cobradas do GKV; prescrição, DDD e EUR | Cobertura publicada 2012–2024; anual; medicamento, princípio ativo, ATC, prescrições, DDD e custos | Portal público com exportação e sem login confirmado; formato real, API e licença de redistribuição não confirmados | Utilização e despesa ambulatorial reembolsada pelo GKV | Confirmar formato do export, seleção de anos/substâncias, esquema, termos de uso e nome/versão do arquivo antes da aquisição sistemática | Não inclui privado/self-pay/hospitalar; sem indicação; mudanças ATC; painel anual potencialmente desequilibrado | `CONDITIONALLY APPROVED` | Variáveis centrais e universo GKV adequados, mas acesso técnico final e reutilização permanecem condicionais |
| `RKI-DIAB-PREV` | Prävalenz dokumentierter Diabetes | RKI Diabetes Surveillance; `https://diabsurv.rki.de/Webs/Diabsurv/DE/diabetes-in-deutschland/2-112_Praevalenz_dokumentierter_Diabetes.html` | Alemanha/GKV; adultos ≥18 anos com critérios DaTraV; casos e taxas | Resultados públicos documentados para 2011 e 2013; Alemanha, estado, sexo, idade; anos adicionais no XLSX não confirmados | XLSX público, aproximadamente 3 MB; sem login; API e licença específica do XLSX não confirmadas | Contexto epidemiológico de prevalência documentada de diabetes no GKV | Verificar arquivo, esquema, anos, dimensões, citação/licença e universo antes do uso | E10–E14 não isola T2D; PKV e diabetes não documentado excluídos; série pública curta | `CONDITIONALLY APPROVED` | Aquisição justificada para contexto, não como dataset principal exclusivo de T2D |
| `RKI-DIAB-INC` | Inzidenz dokumentierter Diabetes | RKI Diabetes Surveillance; `https://diabsurv.rki.de/Webs/Diabsurv/DE/diabetes-in-deutschland/1-01_Inzidenz_dokumentierter_Diabetes.html` | Mesmo universo adulto GKV; novos casos após um ano sem diagnóstico | Ano público documentado: 2012; sexo e idade; incidência estadual e anos adicionais no XLSX não confirmados | XLSX público, aproximadamente 3 MB; sem login; API e licença específica não confirmadas | Contexto epidemiológico de incidência documentada | Mesmas verificações de arquivo, esquema, anos, licença e universo | Não isola T2D; washout de um ano; não é série longitudinal completa confirmada | `CONDITIONALLY APPROVED` | Útil como contexto de incidência sob limites explícitos |
| `RKI-GEDA-AGG` | GEDA 2019/2020-EHIS, tendências e dashboard de obesidade | RKI; `https://edoc.rki.de/handle/176904/10231`, `https://www.rki.de/DE/Themen/Nichtuebertragbare-Krankheiten/Studien-und-Surveillance/Studien/GEDA/GEDA-Dashboard.html` | Alemanha; adultos em domicílios privados; estimativas ponderadas | Ondas 2009, 2010, 2012, 2014/2015 e 2019/2020; agregados de 2022/2023; idade, sexo, educação e estado sujeito à precisão | PDF/HTML/dashboard; formato reutilizável do dashboard não confirmado; termos de reutilização a registrar | Baseline oficial de prevalência de obesidade adulta | Definir exatamente publicação/tabela a preservar; confirmar formato, metadados, precisão e termos | Peso/altura autorrelatados; população de survey ≠ GKV; comparabilidade entre ondas; não mede elegibilidade | `CONDITIONALLY APPROVED` | Fonte epidemiológica oficial adequada, condicionada à seleção e à compatibilidade metodológica |
| `RKI-GEDA-SUF` | GEDA Scientific Use File | RKI/FDZ; `https://www.rki.de/DE/Aktuelles/Publikationen/Forschungsdaten/FDZ/Datenangebot/GEDA/GEDA_inhalt.html`, `https://www.rki.de/DE/Aktuelles/Publikationen/Forschungsdaten/FDZ/Daten-nutzen/Scientific-Use-Files/SUF.html` | Alemanha; microdados anonimizados de survey; observação individual | SUFs confirmados até 2019/2020; variáveis e granularidade dependem do dicionário | Acesso formal, justificativa científica e contrato; SAS/SPSS/Stata; uso comercial excluído | Classes de BMI e segmentações customizadas somente se necessárias | Verificar dicionário, BMI/peso/altura, pesos, comorbidades, tamanho amostral, IC e estabilidade; obter acesso formal | Acesso condicionado; precisão desconhecida; CSV/XLSX não nativos; nenhuma classe considerada disponível antes da inspeção | `CONDITIONALLY APPROVED` | Potencial analítico legítimo, mas aquisição e utilidade dependem de verificação e autorização do FDZ |
| `DESTATIS-KK` | Krankheitskostenrechnung, estatística `23631` | Destatis; `https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Krankheitskosten/_inhalt.html`, `https://genesis.destatis.de/datenbank/online/statistic/23631/details` | Alemanha; custos diretos nacionais atribuídos a diagnósticos; milhões de EUR e EUR por habitante | 2002, 2004, 2006, 2008, 2015, 2020 e 2023; ICD-10, sexo, idade e estabelecimento conforme tabela | GENESIS com download; formato/API final e licença de export não selecionados | Baseline econômico oficial nacional de diabetes e obesidade | Selecionar tabelas, formato e período; registrar termos; preservar séries comparáveis separadas | Sem pagador; E10–E14 não isola T2D; E65–E68 é mais amplo; top-down; não mede custo evitável | `CONDITIONALLY APPROVED` | Fonte oficial adequada ao baseline nacional, mas não ao custo direto do GKV sem fontes/regras adicionais |
| `EMA-REG` | EPARs, Product Information/SmPCs e assessment reports dos produtos documentados | EMA; páginas dos produtos registradas em `00_project/feasibility/ema_clinical_evidence.md`, incluindo `https://www.ema.europa.eu/en/medicines/human/EPAR/wegovy` e `https://www.ema.europa.eu/en/medicines/human/EPAR/mounjaro` | União Europeia; documentos por marca, indicação e população | Versão/data por produto; marca, princípio ativo, indicação, idade, BMI, comorbidade, dose e regras | HTML/PDF públicos; versão e condições de reutilização deverão ser registradas | Fonte normativa para elegibilidade regulatória, nunca para reembolso ou uptake | Preservar documento vigente, versão, data, produto e idioma; adquirir apenas documentação necessária | Autorização UE não equivale a cobertura, apropriação clínica ou tratamento observado | `APPROVED` | Documentação regulatória oficial indispensável e com função delimitada |
| `DE-REG-CONTEXT` | Documentos G-BA, BMG e BfArM já avaliados | G-BA/BMG/BfArM; URLs registradas em `00_project/feasibility/iqvia_public_sources.md` | Alemanha; regras de reembolso, prescrição e mercado legal | Data e granularidade próprias de cada decisão/página | HTML/PDF conforme documento; termos e versão a registrar | Delimitar reembolso e mercado legal | Selecionar somente documentos diretamente pertinentes e registrar snapshot/versão | Não fornecem volumes, pacientes ou tamanho de mercado | `CONDITIONALLY APPROVED` | Documentação oficial contextual útil, condicionada à seleção do documento exato |
| `IQVIA-CONTEXT` | Materiais públicos IQVIA e valores pontuais | IQVIA Germany; URLs específicas registradas em `00_project/feasibility/iqvia_public_sources.md` | Alemanha; recortes de mercado conforme publicação | Valores pontuais de 2022–2025; período/produto/canal somente quando divulgado | PDF/HTML/infográfico; sem série pública reutilizável; termos de reprodução a confirmar | Contextualizar demanda fora do faturamento regular do GKV e métricas comerciais | Selecionar material específico; registrar período, métrica, cobertura, projeção, preço e direitos de uso | Painel projetado; receita privada ≠ self-pay; pacotes/vendas ≠ pacientes; indicação ausente | `CONDITIONALLY APPROVED` | Permitido apenas como documentação contextual/valor pontual, nunca como dataset quantitativo principal |
| `GKV-GAMSI` | GKV-Arzneimittel-Schnellinformation | GKV-Spitzenverband; `https://www.gkv-gamsi.de/` | Alemanha/GKV; cobertura agregada | Período, granularidade e unidades detalhadas não consolidados na F1.2 | Portal oficial; formato e licença não avaliados | Potencial validação agregada das tendências do GKV | Exige feasibility técnica/documental específica antes de qualquer aquisição | Não aprovado como substituto do WIdO; conteúdo detalhado desconhecido | `PENDING DECISION` | Menção contextual aprovada não é suficiente para autorizar aquisição sem avaliação própria |
| `CLINICAL-STUDIES` | Publicações primárias, extensões e estudos observacionais a selecionar | Instituições/publicadores diversos; referências candidatas documentadas na F1.8 | Internacional; populações clínicas específicas | Horizonte, intervenção, dose, comparador, estimando e outcomes por estudo | Artigos/documentos; disponibilidade e direitos variam | Parâmetros clínicos futuros | Executar e autorizar F6.2; aplicar `evidence_inclusion_criteria.md`; decidir fonte e versão antes de preservar | Validade externa, patrocínio, heterogeneidade, acesso e direitos específicos | `PENDING DECISION` | A F1.8 avaliou a classe de evidência, mas a lista real de estudos ainda não foi selecionada |

### 13.2 Componentes não aprovados para aquisição ou uso pretendido

| Acquisition ID | Componente | Instituição | Classificação F2.1 | Justificativa e limite |
|---|---|---|---|---|
| `IQVIA-PUBLIC-DATASET` | Dataset quantitativo reproduzível derivado das fontes públicas IQVIA avaliadas | IQVIA | `NOT APPROVED` | Não existe série pública adequada em CSV/XLSX/API/microdados por pagador/canal; não inventar dataset a partir de recortes |
| `SELF-PAY-PUBLIC` | Quantificação defensável do mercado self-pay somente com fontes públicas avaliadas | Não aplicável | `NOT APPROVED` | Pagador final, indicação, pacientes e canais não são separáveis; ausência de reembolso não quantifica consumo |
| `IQVIA-COMMERCIAL` | Produto comercial IQVIA não adquirido | IQVIA | `NOT APPROVED` | Produto não avaliado quanto a conteúdo, licença, adequação e validade; exigiria decisão própria de aquisição |
| `CROSS-TRIAL-RAW` | Comparação bruta STEP × SURMOUNT × SCALE | Não aplicável | `NOT APPROVED` | Não é dataset autorizável nem método válido para inferir superioridade; populações, doses, estimandos e horizontes diferem |
| `FEASIBILITY-MAP-AS-DATA` | Uso do próprio mapa como fonte empírica ou dataset analítico | Projeto | `NOT APPROVED` | O mapa é artefato de governança e rastreabilidade, não contém observações empíricas próprias |

### 13.3 Condições gerais obrigatórias antes de qualquer aquisição

1. Obter aprovação formal da F2.1 e autorização específica da tarefa F2.2–F2.6 correspondente.
2. Confirmar identidade, URL de download, método de acesso, formato real, versão, período, escopo e seleção do arquivo.
3. Confirmar e registrar licença, termos de uso, restrições de redistribuição e citação; acesso público não equivale a reutilização irrestrita.
4. Definir `source_id`, `dataset_id`, componente, snapshot e caminho conforme `data_conventions.md` e `raw_data_manifest_template.md`.
5. Preservar nome original, arquivo original e metadados; nunca sobrescrever ou corrigir RAW.
6. Registrar origem, data de acesso, data/timestamp de download, versão do publicador, período, população, território e cobertura.
7. Calcular e registrar checksum somente na tarefa autorizada correspondente; nenhum checksum foi produzido na F2.1.
8. Tratar formato, anos, variáveis, licença ou acesso não confirmados como `pending_verification`, nunca como confirmação positiva.
9. Não iniciar linkage, limpeza, conversão, descompactação operacional, análise ou modelagem durante aquisição.
10. Não adquirir `PENDING DECISION` ou `NOT APPROVED` sem nova decisão documental específica.

### 13.4 Riscos transversais preservados

- Datas, populações e faixas etárias podem ser incompatíveis entre RKI, Destatis e WIdO.
- População residente, survey, GKV, diagnosticada, regulatoriamente elegível, clinicamente apropriada e tratada são universos diferentes.
- Nenhuma chave de linkage individual foi confirmada; integrações previstas são agregadas e condicionadas à compatibilidade semântica.
- Variáveis derivadas, como faixas etárias harmonizadas, população elegível, pacientes, T2D específico ou fração evitável, não são variáveis diretamente observadas.
- Formatos esperados a partir da documentação não substituem a verificação do arquivo real.
- Acesso público não confirma licença de redistribuição.
- Nenhuma aquisição autoriza automaticamente uso analítico; esquema, qualidade, cobertura e comparabilidade deverão ser verificados em fases posteriores.

### 13.5 Rastreabilidade e dívida documental histórica

- A decisão operacional original permanece preservada na D-011 do `decision_log.md`.
- As classificações desta seção normalizam as decisões funcionais da Fase 1 para as categorias de aquisição `APPROVED`, `CONDITIONALLY APPROVED`, `NOT APPROVED` e `PENDING DECISION`, sem promover usos proibidos.
- A seção 11 registra o estado documental observado durante a F1.9. As referências nela contidas a tarefas então desatualizadas são um snapshot histórico e foram superadas pelo backlog atual; não alteram a lista F2.1.
- Esta seção não registra arquivo adquirido, acesso operacional validado ou início da etapa operacional da Fase 2.

### 13.6 Resultado técnico da F2.1

A lista final foi formalmente aprovada em 2026-08-11. A execução técnica ocorreu em 2026-08-11 e o status final da F2.1 é `DONE`. A decisão geral permanece `CONDITIONAL GO PARA PROSSEGUIR À PRÓXIMA FASE`. Downloads e aquisições continuam dependentes de autorização específica das tarefas F2.2–F2.6; nenhuma aquisição foi executada. Todas as classificações, condições, limitações, riscos e informações pendentes permanecem inalteradas.
