# Data Feasibility Map — Destatis Disease Costs

Data da avaliação: 2026-08-10

## 1. Identificação

| Campo | Informação |
|---|---|
| Dataset | **FATO VERIFICADO:** Krankheitskostenrechnung, estatística 23631 do GENESIS-Online. |
| Instituição responsável | **FATO VERIFICADO:** Statistisches Bundesamt (Destatis). |
| Fonte oficial / URL | **FATO VERIFICADO:** [Krankheitskosten](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Krankheitskosten/_inhalt.html), [metodologia](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Krankheitskosten/Methoden/krankheitskostenrechnung.html) e [estatística 23631 no GENESIS-Online](https://genesis.destatis.de/datenbank/online/statistic/23631/details). |
| Objetivo no projeto | **FATO VERIFICADO:** fornecer a âncora oficial para os custos diretos de diabetes e obesidade no sistema de saúde alemão, apoiando o dimensionamento da carga econômica e a calibração do modelo. |

## 2. Acesso e cobertura

| Campo | Informação |
|---|---|
| Forma de acesso (arquivo, API ou portal) | **FATO VERIFICADO:** tabelas públicas no portal Destatis e no GENESIS-Online. **NÃO CONFIRMADO:** configuração final da extração e uso de API para este projeto, pois nenhum dado foi solicitado ou baixado. |
| Formato disponível | **FATO VERIFICADO:** visualização tabular no GENESIS-Online com função de download. **NÃO CONFIRMADO:** formato específico que será adotado na aquisição futura. |
| Acesso gratuito e público? | **FATO VERIFICADO:** as páginas e tabelas consultadas são públicas e não exigiram login. |
| Licença ou restrição de uso | **NÃO CONFIRMADO:** as condições específicas de reutilização do arquivo exportado deverão ser registradas no momento da aquisição. |
| Período disponível | **FATO VERIFICADO:** anos publicados: 2002, 2004, 2006, 2008, 2015, 2020 e 2023. As tabelas detalhadas atuais do GENESIS indicam período disponível de 2015 a 2023. **LIMITAÇÃO:** isso representa pontos selecionados, não uma série anual completa. |
| Frequência de atualização | **FATO VERIFICADO:** a partir do ano de referência 2023, o Destatis prevê publicação anual no verão do segundo ano seguinte. O último ano atualmente confirmado nas tabelas é 2023. |
| População coberta | **FATO VERIFICADO:** população da Alemanha e recursos consumidos no sistema de saúde alemão. A estatística mede a carga para a economia alemã, não apenas para pessoas seguradas pelo GKV. |

## 3. Conteúdo analítico

| Campo | Informação |
|---|---|
| Principais indicadores disponíveis | **FATO VERIFICADO:** custos diretos em milhões de euros e custos por habitante, atribuídos a diagnósticos ICD-10. Estão disponíveis diabetes mellitus (E10–E14) e obesidade/outras formas de hiperalimentação (E65–E68). |
| Granularidade temporal | **FATO VERIFICADO:** anual para cada ano publicado. **LIMITAÇÃO:** somente 2015, 2020 e 2023 formam a série recente altamente comparável disponível. Os resultados de 2002–2008 e de 2015–2023 são tratados pelo Destatis como duas séries separadamente comparáveis. |
| Granularidade geográfica | **FATO VERIFICADO:** Alemanha total. **NÃO CONFIRMADO:** não foi identificada desagregação por estado federal na estatística 23631. |
| Granularidade demográfica | **FATO VERIFICADO:** sexo e grupos etários nas tabelas 23631-0002, 23631-0003 e 23631-0005. |
| Possíveis chaves de integração | **FATO VERIFICADO:** ano, código/grupo ICD-10, sexo e grupo etário. **LIMITAÇÃO:** as faixas etárias precisam ser harmonizadas com os datasets epidemiológicos e demográficos. |
| Variável crítica disponível? | **FATO VERIFICADO:** custos para diabetes E10–E14 e obesidade/hiperalimentação E65–E68 estão disponíveis. **LIMITAÇÃO:** a tabela principal não separa diabetes tipo 2 (E11) dos demais tipos e o grupo E65–E68 é mais amplo que obesidade isolada. |

## 4. Avaliação

| Campo | Informação |
|---|---|
| Pontos fortes | **FATO VERIFICADO:** fonte oficial nacional; metodologia documentada; valores absolutos e por habitante; classificação ICD-10; desagregação por idade, sexo e tipo de estabelecimento; disponibilidade específica para diabetes e obesidade; continuidade anual planejada a partir de 2023. |
| Limitações e lacunas | **LIMITAÇÃO:** os valores representam custos diretos totais do sistema de saúde e não possuem dimensão por pagador na estatística 23631. Portanto, não isolam a parcela paga pelo GKV. Não separam diabetes tipo 2 dentro de E10–E14. Não representam automaticamente custos evitáveis e não incluem toda a carga econômica indireta em cada tabela de custos diretos. |
| Riscos para a análise | **LIMITAÇÃO:** usar o custo total de E10–E14 como custo evitável de diabetes tipo 2 superestimaria a economia. Aplicar diretamente custos nacionais totais ao orçamento do GKV também seria incorreto. Multimorbidade e diferenças na codificação podem afetar a atribuição de custos; o Destatis utiliza abordagem top-down e algoritmos de alocação. Valores nominais entre anos também refletem preços e mudanças do sistema, não apenas alterações da carga de doença. |
| Dataset alternativo, se necessário | **FATO VERIFICADO:** a Gesundheitsausgabenrechnung do Destatis separa despesas por pagador, incluindo GKV, mas não simultaneamente por diagnóstico. Ela pode ser usada futuramente como complemento para construir uma hipótese de participação do GKV. **NÃO CONFIRMADO:** a validade de aplicar essa participação aos custos específicos de diabetes ou obesidade ainda precisa ser avaliada. |
| Decisão aprovada (GO, CONDITIONAL GO ou NO-GO) | **CONDITIONAL GO** |
| Justificativa da decisão | A Krankheitskostenrechnung é adequada como baseline econômico oficial nacional dos custos diretos atribuídos a diabetes e obesidade. Seu uso no modelo GKV, porém, depende primeiro da identificação de fontes defensáveis para a participação do GKV, a proporção de diabetes tipo 2 e a fração de custos evitável. Parâmetros não diretamente observáveis deverão ser registrados como `modelled assumptions`. O dataset não será tratado sozinho como base principal do modelo econômico nem como custo automático por caso prevenido. |
| Destino RAW planejado | `01_raw_data/destatis/` |

## 5. Verificação

- [x] As fontes oficiais do Destatis foram consultadas.
- [x] As informações foram verificadas ou marcadas como `NÃO CONFIRMADO`.
- [x] As limitações foram registradas.
- [x] A decisão aprovada foi justificada.
- [ ] O usuário aprovou a decisão antes do download.

## 6. Tabelas oficiais relevantes

| Código | Conteúdo | Papel esperado |
|---|---|---|
| 23631-0001 | Custos e custos por habitante por diagnóstico ICD-10 | Totais nacionais para diabetes e obesidade |
| 23631-0003 | Custos por diagnóstico, sexo e idade | Estratificação demográfica |
| 23631-0004 | Custos por diagnóstico, sexo e estabelecimento | Distribuição por tipo de estabelecimento |
| 23611-0001 / 23611-0004 | Gastos de saúde por pagador | Complemento potencial para estimar participação do GKV |

## 7. Fontes oficiais consultadas

1. Destatis — Krankheitskosten: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Krankheitskosten/_inhalt.html
2. Destatis — Metodologia da Krankheitskostenrechnung: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Gesundheit/Krankheitskosten/Methoden/krankheitskostenrechnung.html
3. GENESIS-Online — Estatística 23631: https://genesis.destatis.de/datenbank/online/statistic/23631/details
4. GENESIS-Online — Tabela 23631-0001: https://genesis.destatis.de/datenbank/online/statistic/23631/table/23631-0001
5. GENESIS-Online — Tabela 23631-0003: https://genesis.destatis.de/datenbank/online/statistic/23631/table/23631-0003
6. GENESIS-Online — Tabela de gastos por pagador 23611-0001: https://genesis.destatis.de/datenbank/online/statistic/23611/table/23611-0001

Não foram utilizadas fontes secundárias nesta avaliação.
