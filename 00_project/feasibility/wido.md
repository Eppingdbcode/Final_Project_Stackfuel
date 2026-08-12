# Data Feasibility Map — WIdO / PharMaAnalyst

Data da avaliação: 2026-08-10

## 1. Identificação

| Campo | Informação |
|---|---|
| Dataset | **FATO VERIFICADO:** PharMaAnalyst, ferramenta online do GKV-Arzneimittelindex. |
| Instituição responsável | **FATO VERIFICADO:** Wissenschaftliches Institut der AOK (WIdO). |
| Fonte oficial / URL | **FATO VERIFICADO:** [WIdO — PharMaAnalyst](https://www.wido.de/publikationen-produkte/analytik/pharmaanalyst/) e [portal PharMaAnalyst](https://arzneimittel.wido.de/PharMaAnalyst/). |
| Objetivo no projeto | **FATO VERIFICADO:** fornecer séries anuais observadas de prescrições, DDD e custos de medicamentos GLP-1/GIP cobrados do GKV, permitindo comparações por medicamento, princípio ativo e grupo ATC. |

## 2. Acesso e cobertura

| Campo | Informação |
|---|---|
| Forma de acesso (arquivo, API ou portal) | **FATO VERIFICADO:** portal público interativo com opção de exportar resultados. **NÃO CONFIRMADO:** existência de API pública ou download único de toda a base. |
| Formato disponível | **FATO VERIFICADO:** resultados em tabela no portal. **NÃO CONFIRMADO:** formato exato do arquivo exportado; deve ser verificado antes do download. |
| Acesso gratuito e público? | **FATO VERIFICADO:** o WIdO descreve o PharMaAnalyst como uma ferramenta livremente acessível. |
| Licença ou restrição de uso | **NÃO CONFIRMADO:** não foi localizada, nas páginas oficiais consultadas, uma licença específica para redistribuição dos resultados exportados. A publicação metodológica informa que reprodução e distribuição de seu conteúdo exigem autorização expressa; isso não confirma as condições aplicáveis aos exports do portal. |
| Período disponível | **FATO VERIFICADO:** publicação oficial do WIdO de 2025 informa cobertura de 2012 a 2024. **LIMITAÇÃO:** a publicação metodológica de 2024 descreve o PharMaAnalyst como disponível desde 2016. O primeiro ano efetivamente selecionável e a consistência da série devem ser confirmados diretamente no portal antes do download. |
| Frequência de atualização | **FATO VERIFICADO:** os resultados são organizados por ano e o conjunto dos medicamentos mais relevantes é definido para cada ano. **NÃO CONFIRMADO:** calendário exato de publicação de novos anos. A base é ajustada ao longo do tempo e estimativas de anos anteriores podem ser atualizadas. |
| População coberta | **FATO VERIFICADO:** mais de 70 milhões de pessoas seguradas pelo GKV; prescrições ambulatoriais cobradas do GKV por farmácias públicas e farmácias hospitalares na assistência ambulatorial. |

## 3. Conteúdo analítico

| Campo | Informação |
|---|---|
| Principais indicadores disponíveis | **FATO VERIFICADO:** ano, medicamento, princípio ativo ou grupo ATC, código ATC, número de prescrições, DDD, custos líquidos absolutos, custos líquidos por prescrição, custos líquidos por DDD, variação anual e rankings. |
| Granularidade temporal | **FATO VERIFICADO:** anual no PharMaAnalyst. **LIMITAÇÃO:** a documentação metodológica informa que a base subjacente permite análises mensais desde 2011, mas não foi confirmado que essa granularidade esteja disponível no portal público. |
| Granularidade geográfica | **FATO VERIFICADO:** total nacional do GKV nos resultados públicos do PharMaAnalyst consultados. **NÃO CONFIRMADO:** disponibilidade de resultados exportáveis por estado, região ou distrito no portal. |
| Granularidade demográfica | **NÃO CONFIRMADO:** idade e sexo existem na base subjacente do GKV-Arzneimittelindex, mas não foram identificados como filtros ou colunas disponíveis no resultado público do PharMaAnalyst. |
| Possíveis chaves de integração | **FATO VERIFICADO:** ano e código ATC; princípio ativo pode ser usado após padronização. **LIMITAÇÃO:** a classificação ATC utilizada corresponde ao ano selecionado e pode mudar entre anos. |
| Variável crítica disponível? | **FATO VERIFICADO:** estão disponíveis as variáveis centrais para a análise de mercado — princípio ativo, ATC, prescrições, DDD e custos líquidos. **LIMITAÇÃO:** a indicação clínica da prescrição não aparece entre os campos confirmados; portanto, não é possível assumir que todas as prescrições de um princípio ativo correspondam a tratamento de obesidade ou de diabetes. |

## 4. Avaliação

| Campo | Informação |
|---|---|
| Pontos fortes | **FATO VERIFICADO:** fonte oficial, pública, específica do GKV, baseada em prescrições ambulatoriais cobradas conforme § 300 SGB V e ajustadas à estatística oficial de despesas KV 45. Permite busca por medicamento, princípio ativo e ATC, além de indicadores anuais de volume e custo. A metodologia de 2024 estima cobertura de aproximadamente 98% das prescrições anuais com os 3.000 medicamentos selecionados. |
| Limitações e lacunas | **LIMITAÇÃO:** não inclui receitas privadas, compras autofinanciadas ou medicamentos OTC não reembolsados pelo GKV. Não inclui medicamentos utilizados em internações. Farmácias hospitalares na assistência ambulatorial só estão completamente incluídas desde 2019. O portal limita análises por medicamento/princípio ativo aos 3.000 itens mais relevantes de cada ano. A página geral atual do WIdO menciona cerca de 95% do mercado, enquanto a metodologia de 2024 menciona cerca de 98% das prescrições; a métrica e a versão da documentação devem ser citadas com precisão. |
| Riscos para a análise | **LIMITAÇÃO:** medicamentos novos ou de menor volume podem não aparecer em todos os anos, criando um painel desequilibrado. Estimativas históricas podem ser revisadas. Mudanças anuais na classificação ATC podem afetar comparabilidade. Os custos líquidos incluem copagamentos e imposto, mas descontos contratuais confidenciais que não podem ser atribuídos a produtos individuais permanecem fora do cálculo. A ausência de indicação clínica impede separar diretamente uso para diabetes e uso para obesidade. |
| Dataset alternativo, se necessário | **FATO VERIFICADO:** GKV-GAmSi é uma fonte oficial complementar para validar tendências agregadas do mercado farmacêutico GKV. **LIMITAÇÃO:** nesta etapa não foi avaliada como substituta para séries por princípio ativo. URL: [GKV-GAmSi](https://www.gkv-gamsi.de/). |
| Decisão preliminar (GO, CONDITIONAL GO ou NO-GO) | **CONDITIONAL GO** |
| Justificativa da decisão | O PharMaAnalyst possui as variáveis centrais e cobertura adequada para analisar prescrições e custos de GLP-1/GIP no GKV. O uso deve ficar condicionado à confirmação do formato de exportação, dos anos selecionáveis e da presença de cada princípio ativo relevante antes do download. Os resultados deverão ser apresentados como mercado ambulatorial reembolsado pelo GKV, nunca como consumo total alemão ou como uso comprovado por indicação clínica. |
| Destino RAW planejado | `01_raw_data/wido/` |

## 5. Verificação

- [x] A fonte oficial foi consultada.
- [x] As informações acima foram verificadas ou marcadas como `NÃO CONFIRMADO`.
- [x] As limitações foram registradas.
- [x] A decisão preliminar foi justificada.
- [ ] O usuário aprovou a decisão antes do download.

## 6. Fontes oficiais consultadas

1. WIdO — PharMaAnalyst: https://www.wido.de/publikationen-produkte/analytik/pharmaanalyst/
2. Portal PharMaAnalyst e glossário: https://arzneimittel.wido.de/PharMaAnalyst/
3. WIdO — Der GKV-Arzneimittelmarkt: Klassifikation, Methodik und Ergebnisse 2024: https://www.wido.de/fileadmin/Dateien/Dokumente/Forschung_Projekte/Arzneimittel/wido_arz_gkv-arzneimittelmarkt_klassifikation_methodik_ergebnisse_2024.pdf
4. WIdO — ATC-Klassifikation für den deutschen Arzneimittelmarkt: https://www.wido.de/publikationen-produkte/analytik/arzneimittel-klassifikation/
5. WIdO — publicação oficial sobre o mercado de 2024, com descrição da cobertura 2012–2024: https://www.wido.de/news-presse/pressemitteilungen/2025/biosimilars/
6. GKV-Spitzenverband — GKV-GAmSi: https://www.gkv-gamsi.de/

Não foram utilizadas fontes secundárias nesta avaliação.

