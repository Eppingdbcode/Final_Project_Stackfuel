# Data Feasibility Map — Destatis Demographics

## 1. Identificação e fontes oficiais

**Instituição responsável:** Statistisches Bundesamt (Destatis), Alemanha.  
**Portal:** GENESIS-Online.  
**Data de acesso:** 2026-08-10.

### Tabelas selecionadas

| Código | Nome oficial | Estatística de origem | Papel proposto | URL oficial |
|---|---|---|---|---|
| `12411-0013` | Bevölkerung: Bundesländer, Stichtag, Geschlecht, Altersjahre | `12411` — Fortschreibung des Bevölkerungsstandes | Fonte principal para população de fim de ano por estado, sexo e idade individual | https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0013 |
| `12411-0041` | Durchschnittliche Bevölkerung: Deutschland, Jahre, Nationalität, Geschlecht, Altersjahre | `12411` — Fortschreibung des Bevölkerungsstandes | Denominador médio anual nacional quando for mais compatível com o período epidemiológico | https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0041 |
| `12411-0020` | Bevölkerung: Deutschland, Stichtag zum Quartalsende, Geschlecht | `12411` — Fortschreibung des Bevölkerungsstandes | Verificação do dado nacional oficial mais recente; não possui idade individual | https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0020 |
| `12421-0002` | Vorausberechneter Bevölkerungsstand: Deutschland, Stichtag, Varianten der Bevölkerungsvorausberechnung, Geschlecht, Altersjahre | `12421` — Bevölkerungsvorausberechnungen | Referência nacional projetada para 2026 por sexo e idade | https://genesis.destatis.de/datenbank/online/table/12421-0002/ |
| `12421-0004` | Vorausberechneter Bevölkerungsstand: Bundesländer, Stichtag, Varianten der Bevölkerungsvorausberechnung, Geschlecht, Altersjahre | `12421` — Bevölkerungsvorausberechnungen | Referência estadual projetada para 2026, se uma análise estadual for justificada | https://genesis.destatis.de/datenbank/online/table/12421-0004/ |

### Justificativa da seleção

- **FATO VERIFICADO:** `12411-0013` reúne, na mesma tabela, estado federal, data de referência, sexo e idade individual. É a opção mais direta para construir denominadores compatíveis com estratos epidemiológicos sem depender de faixas etárias predefinidas.
- **FATO VERIFICADO:** `12411-0041` contém população média anual por idade individual e sexo, sendo metodologicamente mais adequada que uma fotografia de 31 de dezembro quando a prevalência representar um período anual.
- **FATO VERIFICADO:** `12411-0020` alcança 31/03/2026, mas não fornece a granularidade etária necessária. Portanto, não substitui o denominador detalhado anual.
- **FATO VERIFICADO:** `12421-0002` e `12421-0004` são projeções oficiais com variantes, sexo e idade individual. Foram selecionadas somente para cenários futuros, nunca como contagens observadas.
- **LIMITAÇÃO:** não foi selecionada silenciosamente uma única tabela universal. A escolha entre população de fim de ano, média anual e projeção deve acompanhar a data ou o período da prevalência aplicada.

## 2. Cobertura temporal

### População atualizada — estatística `12411`

- **FATO VERIFICADO:** a tabela `12411-0013` possui resultados anuais em 31 de dezembro de 1967 a 2025, com idade individual, sexo e estados federais.
- **FATO VERIFICADO:** `12411-0041` fornece população média anual e inclui 2025.
- **FATO VERIFICADO:** existem resultados para 2023, 2024 e 2025.
- **FATO VERIFICADO:** `12411-0020` possui resultados trimestrais nacionais até 31/03/2026, por sexo, mas sem idade.
- **FATO VERIFICADO:** a população corrente é produzida pela atualização dos resultados do censo com nascimentos, óbitos e movimentos migratórios informados pelas autoridades competentes.
- **CLASSIFICAÇÃO:** os resultados da `Fortschreibung des Bevölkerungsstandes` serão tratados como `official population estimate`, embora o GENESIS apresente a unidade como número de pessoas. Não são uma nova contagem censitária direta a cada ano.

### Projeções — estatística `12421`

- **FATO VERIFICADO:** a 16ª projeção populacional coordenada baseia-se na população em 31/12/2024 e cobre 2025–2070.
- **FATO VERIFICADO:** `12421-0002` e `12421-0004` incluem 31/12/2026, várias variantes, sexo e idades individuais.
- **FATO VERIFICADO:** as projeções são cenários “se–então” baseados em hipóteses de fecundidade, mortalidade e migração; o Destatis declara que não pretendem prever exatamente o futuro.
- **CLASSIFICAÇÃO:** qualquer valor de 2026 obtido dessas tabelas será `official population projection`.
- **LIMITAÇÃO:** a seleção de uma variante para 2026 será uma decisão metodológica explícita. Não será feita nesta etapa.

### Quebras e revisões censitárias

- **FATO VERIFICADO:** resultados a partir de 2011 usam o Censo 2011; resultados a partir de 2022 usam o Censo 2022.
- **FATO VERIFICADO:** após a divulgação do Censo 2022, os resultados mensais desde maio de 2022, trimestrais desde o segundo trimestre de 2022 e anuais desde 2022 foram recalculados na nova base.
- **FATO VERIFICADO:** o Destatis registra quebra de série e comparabilidade limitada entre dados até 2021 e dados desde 2022. O Censo 2022 alterou o nível populacional de referência de forma material.
- **LIMITAÇÃO:** séries que atravessem 2011 ou 2022 não devem ser combinadas ou interpretadas como contínuas sem conferir a base censitária e as notas metodológicas.

## 3. População e cobertura geográfica

- **FATO VERIFICADO:** há resultados para a Alemanha total e para os 16 estados federais.
- **FATO VERIFICADO:** a população estatística compreende pessoas sujeitas ao registro obrigatório na Alemanha, registradas no local da residência única ou principal. Pessoas refugiadas e solicitantes de proteção sujeitas ao registro também integram a população.
- **FATO VERIFICADO:** o Censo 2022 corrige registros para pessoas registradas que não residem no local, registros duplicados e pessoas residentes não registradas.
- **FATO VERIFICADO:** o conceito não se limita a cidadãos alemães. Nacionalidade é uma dimensão adicional em algumas tabelas; para o denominador do projeto deve ser usado `Insgesamt`, salvo justificativa diferente.
- **FATO VERIFICADO:** pessoas residentes em alojamentos coletivos ou institucionais não são automaticamente excluídas do conceito geral de população por estarem fora de domicílios privados; o critério central é residência única/principal e obrigação de registro. Isso difere da população-alvo de pesquisas domiciliares como o GEDA.
- **LIMITAÇÃO:** a população total não equivale à população adulta. A população adulta deverá ser calculada a partir das idades compatíveis com a fonte epidemiológica.
- **LIMITAÇÃO:** população residente não equivale à população segurada pelo GKV. O Destatis Demographics não identifica tipo de seguro de saúde.

## 4. Granularidade

| Dimensão | Disponibilidade oficial verificada | Observação para o projeto |
|---|---|---|
| Ano/data de referência | Sim | Anual em 31/12, média anual e parte da série trimestral |
| Idade individual | Sim | `12411-0013`, `12411-0041`, `12421-0002` e `12421-0004` |
| Faixas etárias | Podem ser construídas a partir da idade individual | Resultado será `derived calculation` |
| Sexo | Masculino, feminino e total | Categorias oficiais disponíveis nas tabelas selecionadas |
| Estado federal | Sim | População atualizada e projeções possuem tabelas estaduais |
| Nacionalidade | Disponível em tabelas específicas e na população média | Não é necessária ao denominador principal neste momento |

- **FATO VERIFICADO:** a idade individual permite construir exatamente as faixas publicadas pelo RKI/GEDA e outras fontes, respeitando limites superiores abertos.
- **LIMITAÇÃO:** essa flexibilidade não justifica criar estratos mais finos que os da prevalência original. Aplicar uma prevalência ampla a idades individuais produziria falsa precisão.
- **LIMITAÇÃO:** os limites superiores agrupados variam entre tabelas atuais e projetadas. A harmonização deve preservar a categoria aberta da fonte e não desagregar seu conteúdo artificialmente.
- **NÃO CONFIRMADO:** compatibilidade direta de todas as categorias de sexo entre cada fonte epidemiológica e cada ano. Isso deverá ser tratado nas regras futuras de harmonização.

## 5. Acesso técnico e reprodutibilidade

- **FATO VERIFICADO:** as tabelas podem ser consultadas e configuradas no GENESIS-Online.
- **FATO VERIFICADO:** a interface RESTful/JSON permite pesquisa, recuperação de dados e metadados, além de exportações em formatos reutilizáveis, incluindo XLSX, CSV/flat-file CSV e outros formatos documentados.
- **FATO VERIFICADO:** a documentação oficial apresenta integração com Python e Pandas e recomenda `ffcsv` para processamento tabular.
- **FATO VERIFICADO:** desde 30/06/2025 a API usa requisições POST; as credenciais são enviadas no cabeçalho.
- **FATO VERIFICADO:** quase todas as chamadas exigem autenticação por conta gratuita ou token pessoal. Operações em lote com `job=true` exigem usuário/e-mail e senha, não apenas token.
- **FATO VERIFICADO:** chamadas de tabela em modo interativo possuem limite documentado de 40.000 valores; tabelas maiores devem ser divididas ou processadas pela fila em lote.
- **FATO VERIFICADO:** metadados de estatísticas, tabelas, variáveis, classificações e sinais de qualidade podem ser consultados pela API e pela interface web.
- **AVALIAÇÃO TÉCNICA:** a extração futura é reproduzível em Python/Pandas, desde que IDs de tabela, seleções, período, variante, formato, data de extração e notas metodológicas sejam registrados.
- **LIMITAÇÃO:** alterações futuras da API ou atualizações retroativas da base exigem versionamento do momento de extração e preservação dos arquivos RAW.
- Nenhuma chamada de extração ou download foi realizada nesta tarefa.

## 6. Natureza da evidência

| Elemento | Classificação | Uso correto |
|---|---|---|
| Resultado direto do Censo 2022 no respectivo dia censitário | `official population count` | Base censitária oficial, com correções metodológicas do censo |
| População atualizada da estatística `12411` | `official population estimate` | Estimativa oficial atualizada a partir do censo e dos componentes demográficos |
| População média anual da tabela `12411-0041` | `official population estimate` | Denominador oficial médio do ano |
| Resultados da 16ª projeção coordenada (`12421`) | `official population projection` | Cenário oficial condicionado à variante escolhida |
| Soma de idades ou estados; construção de faixas | `derived calculation` | Cálculo reproduzível a partir de células oficiais |
| Interpolação, extrapolação ou combinação não publicada | `modelled assumption` | Deve ser justificada e separada das séries oficiais |

**Regra:** uma projeção oficial não será chamada de contagem observada. Um agregado criado pelo projeto não será chamado de valor diretamente publicado.

## 7. Compatibilidade com o projeto

- **Converter prevalências em números absolutos:** sim, desde que prevalência e denominador compartilhem população-alvo, período e estratos compatíveis.
- **Calcular população adulta por idade e sexo:** sim, por agregação reproduzível das idades individuais.
- **Harmonizar com RKI/GEDA:** sim, mantendo as faixas originais da prevalência e documentando a diferença entre população em domicílios privados do GEDA e população residente do Destatis.
- **Apoiar estimativas de diabetes:** sim, como denominador demográfico quando o indicador epidemiológico for populacional. Para indicadores específicos do GKV, deve-se usar denominador compatível com o GKV, não a população residente por padrão.
- **Segmentação nacional:** sim.
- **Segmentação estadual:** tecnicamente disponível, mas só é defensável se a fonte epidemiológica também tiver estimativas estaduais estáveis e comparáveis.
- **Denominador dos cenários posteriores:** sim. Para 2026, pode-se usar uma projeção oficial claramente identificada, com variante documentada e, idealmente, sensibilidade entre variantes pertinentes.
- **LIMITAÇÃO:** não há ligação individual entre Destatis, RKI/GEDA, RKI Diabetes ou WIdO. A combinação ocorrerá por estratos agregados harmonizados.

## 8. Limitações críticas

1. **Cobertura pelo GKV:** Destatis Demographics não identifica cobertura pelo GKV. População residente e população segurada pelo GKV são universos diferentes.
2. **Elegibilidade:** população residente não equivale à população elegível para GLP-1/GIP.
3. **Datas de referência:** população em 31 de dezembro, população média anual e período de coleta da prevalência não são intercambiáveis. O denominador deve acompanhar o período epidemiológico.
4. **Faixas etárias:** RKI/GEDA, RKI Diabetes e WIdO podem usar faixas diferentes. A harmonização deve ocorrer no maior nível comum sustentado pelas fontes, evitando falsa precisão.
5. **Censo 2022:** a revisão alterou a base populacional e introduziu uma quebra de série.
6. **Comparabilidade:** valores anteriores e posteriores às revisões dos Censos 2011 e 2022 não devem ser combinados sem conferir base, recalculações e notas oficiais.
7. **Ano 2026:** o resultado anual detalhado disponível em `12421` é uma `official population projection`. Interpolação ou extrapolação própria seria `modelled assumption`. O resultado trimestral de 31/03/2026 não representa automaticamente a população média ou de fim de 2026.
8. **Ausência de informação clínica:** os dados demográficos não permitem inferir diagnóstico, BMI, obesidade, diabetes, comorbidades, contraindicações ou elegibilidade clínica/regulatória.
9. **Instituições versus domicílios privados:** o universo de população residente é mais amplo que o universo de algumas pesquisas do RKI. Essa diferença deve ser explicitada ao converter prevalências.
10. **Estimativas estaduais:** disponibilidade demográfica não resolve incerteza ou instabilidade de prevalências estaduais; intervalos de confiança da fonte epidemiológica continuam determinantes.

## 9. Decisão

### `GO`

**Justificativa:** o Destatis fornece denominadores oficiais recentes, anuais e tecnicamente reutilizáveis, com idade individual, sexo, Alemanha total e estados federais. Há resultados da população atualizada até 2025 e projeções oficiais da 16ª população coordenada para 2026, permitindo construir faixas compatíveis com as fontes epidemiológicas sem inventar desagregações.

**Papel exato no projeto:** servir como **denominador demográfico oficial** para transformar prevalências populacionais defensáveis em números absolutos e sustentar cenários nacionais. A população de 2026 deverá ser rotulada conforme sua natureza, com a variante oficial explicitada. O Destatis não será usado como proxy de segurados do GKV nem como fonte de diagnóstico ou elegibilidade para GLP-1/GIP.

## 10. Próximos controles antes do uso analítico

- Escolher a data de referência ou população média de acordo com cada prevalência.
- Registrar a base censitária e impedir mistura silenciosa entre séries incompatíveis.
- Definir e documentar a variante oficial utilizada para 2026; não realizar a projeção nesta etapa.
- Manter as faixas etárias no nível efetivamente sustentado pelas fontes epidemiológicas.
- Verificar, antes de qualquer segmentação estadual, a precisão da estimativa epidemiológica correspondente.
- Aguardar aprovação do usuário antes de prosseguir.
