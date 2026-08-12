# Data Feasibility Map — RKI Diabetes Surveillance

Data da avaliação: 2026-08-10

## 1. Identificação

| Campo | Informação |
|---|---|
| Dataset | **FATO VERIFICADO:** indicadores “Prävalenz dokumentierter Diabetes” e “Inzidenz dokumentierter Diabetes” da Diabetes Surveillance do RKI. |
| Instituição responsável | **FATO VERIFICADO:** Robert Koch-Institut (RKI). |
| Fonte oficial / URL | **FATO VERIFICADO:** [Prevalência documentada](https://diabsurv.rki.de/Webs/Diabsurv/DE/diabetes-in-deutschland/2-112_Praevalenz_dokumentierter_Diabetes.html) e [incidência documentada](https://diabsurv.rki.de/Webs/Diabsurv/DE/diabetes-in-deutschland/1-01_Inzidenz_dokumentierter_Diabetes.html). |
| Objetivo no projeto | **FATO VERIFICADO:** fornecer estimativas observadas de prevalência e incidência de diabetes documentado entre adultos segurados pelo GKV, com números absolutos, taxas e estratificações úteis para dimensionar a carga de doença. |

## 2. Acesso e cobertura

| Campo | Informação |
|---|---|
| Forma de acesso (arquivo, API ou portal) | **FATO VERIFICADO:** páginas públicas do RKI com visualizações e links diretos para tabelas de dados. **NÃO CONFIRMADO:** existência de API pública específica para esses indicadores. |
| Formato disponível | **FATO VERIFICADO:** XLSX; cada página informa uma tabela de aproximadamente 3 MB. Nenhum arquivo foi baixado nesta avaliação. |
| Acesso gratuito e público? | **FATO VERIFICADO:** as páginas e os links de download são públicos e não apresentam exigência de login. |
| Licença ou restrição de uso | **NÃO CONFIRMADO:** as páginas oferecem uma forma recomendada de citação, mas esta avaliação não confirmou uma licença específica anexada aos arquivos XLSX. |
| Período disponível | **FATO VERIFICADO:** a página de prevalência apresenta resultados de 2011 para diferenças regionais e de 2013 para idade e sexo; a página de incidência apresenta o ano de 2012. **NÃO CONFIRMADO:** presença de anos adicionais dentro dos arquivos XLSX, pois eles não foram baixados. |
| Frequência de atualização | **FATO VERIFICADO:** a Diabetes Surveillance foi concebida para atualização recorrente dos indicadores. **NÃO CONFIRMADO:** calendário fixo de atualização dos dois arquivos e disponibilidade atual de uma série anual contínua. |
| População coberta | **FATO VERIFICADO:** adultos com 18 anos ou mais, residentes na Alemanha, segurados pelo GKV por pelo menos 360 dias no ano e com cobertura integral de suas despesas médicas pelo seguro estatutário. A fonte DaTraV reúne dados de aproximadamente 70 milhões de segurados; cerca de 55 milhões são adultos. |

## 3. Conteúdo analítico

| Campo | Informação |
|---|---|
| Principais indicadores disponíveis | **FATO VERIFICADO:** prevalência e incidência observadas, números absolutos, taxas relativas e resultados padronizados por idade. A prevalência é baseada em diagnóstico hospitalar em pelo menos um trimestre ou diagnóstico ambulatorial confirmado em pelo menos dois trimestres. A incidência requer novo diabetes documentado e ausência de diagnóstico no ano anterior. |
| Granularidade temporal | **FATO VERIFICADO:** anual para os anos apresentados. **LIMITAÇÃO:** não foi confirmada uma série anual longa e contínua nos arquivos públicos atuais. |
| Granularidade geográfica | **FATO VERIFICADO:** Alemanha e estados federais para a prevalência; a localização estadual utiliza o endereço residencial. **NÃO CONFIRMADO:** disponibilidade de incidência por estado federal no arquivo XLSX. |
| Granularidade demográfica | **FATO VERIFICADO:** sexo e faixas etárias; a prevalência também possui resultados padronizados por idade. |
| Possíveis chaves de integração | **FATO VERIFICADO:** ano, sexo, faixa etária e estado federal, quando presentes na respectiva tabela. **LIMITAÇÃO:** as categorias precisam ser comparadas com as definições dos datasets de população e obesidade antes de qualquer junção. |
| Variável crítica disponível? | **LIMITAÇÃO:** os indicadores adultos principais definem diabetes pelos códigos ICD-10 E10–E14 combinados. A tabela pública principal não está confirmada como separável em diabetes tipo 2. Uma publicação oficial do RKI apresenta um algoritmo para distinguir E11 e estimou prevalência de diabetes tipo 2 em 2011, mas destaca que a diferenciação dos tipos é difícil devido à prática de codificação. Não foi localizado um indicador adulto longitudinal público equivalente exclusivamente para diabetes tipo 2. |

## 4. Avaliação

| Campo | Informação |
|---|---|
| Pontos fortes | **FATO VERIFICADO:** fonte oficial do RKI; grande cobertura do GKV; inclusão de diagnósticos ambulatoriais e hospitalares; definições transparentes; números absolutos e relativos; estratificação por idade, sexo e estado federal; arquivos XLSX públicos. |
| Limitações e lacunas | **LIMITAÇÃO:** exclui pessoas com seguro privado. Os dados foram produzidos para faturamento e dependem da prática de documentação e codificação. Os indicadores adultos principais agregam E10–E14. A incidência usa somente um ano anterior sem diagnóstico como período de exclusão. A cobertura temporal pública confirmada é curta e não constitui, por si só, uma série longitudinal suficiente para observar mudanças recentes. |
| Riscos para a análise | **LIMITAÇÃO:** tratar todos os casos E10–E14 como diabetes tipo 2 superestimaria o desfecho do modelo. A proporção de casos classificados como tipo 2 em estudos específicos não deve ser aplicada automaticamente a todos os anos ou estratos. Diferenças entre dados de faturamento e surveys podem afetar comparações. |
| Dataset alternativo, se necessário | **FATO VERIFICADO:** o próprio RKI utiliza adicionalmente surveys de saúde, registros de diabetes e outras fontes em sua vigilância. **NÃO CONFIRMADO:** nesta etapa não foi avaliada nenhuma fonte alternativa, conforme o escopo solicitado. |
| Decisão preliminar (GO, CONDITIONAL GO ou NO-GO) | **CONDITIONAL GO** |
| Justificativa da decisão | O dataset é adequado para estabelecer um baseline oficial da carga de diabetes documentado no GKV e apoiar estratificações demográficas e regionais. Entretanto, não é suficiente sozinho para modelar longitudinalmente diabetes tipo 2, porque os indicadores adultos principais agregam E10–E14 e a série temporal pública confirmada é limitada. Seu uso deverá ser condicionado à inspeção posterior dos XLSX e à definição explícita de como tratar a separação do tipo 2. |
| Destino RAW planejado | `01_raw_data/rki_diabetes/` |

## 5. Verificação

- [x] As fontes oficiais do RKI foram consultadas.
- [x] As informações foram verificadas ou marcadas como `NÃO CONFIRMADO`.
- [x] As limitações foram registradas.
- [x] A decisão preliminar foi justificada.
- [ ] O usuário aprovou a decisão antes do download.

## 6. Fontes oficiais consultadas

1. RKI Diabetes Surveillance — Prevalência documentada de diabetes: https://diabsurv.rki.de/Webs/Diabsurv/DE/diabetes-in-deutschland/2-112_Praevalenz_dokumentierter_Diabetes.html
2. RKI Diabetes Surveillance — Incidência documentada de diabetes: https://diabsurv.rki.de/Webs/Diabsurv/DE/diabetes-in-deutschland/1-01_Inzidenz_dokumentierter_Diabetes.html
3. RKI Diabetes Surveillance — Fontes de dados: https://diabsurv.rki.de/Webs/Diabsurv/DE/projekt/methodik/datenquellen/datenquellen-node.html
4. RKI — “Prävalenz und Inzidenz des dokumentierten Diabetes mellitus – Referenzauswertung für die Diabetes-Surveillance auf Basis von Daten aller gesetzlich Krankenversicherten”: https://edoc.rki.de/handle/176904/7565
5. RKI Gesundheitsberichterstattung — Diabetes mellitus: https://www.gbe.rki.de/DE/Themen/Gesundheitszustand/KoerperlicheErkrankungen/DiabetesMellitus/diabetesmellitus_node.html

Não foram utilizadas fontes secundárias nesta avaliação.

