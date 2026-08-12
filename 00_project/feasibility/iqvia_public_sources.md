# Data Feasibility Map — IQVIA Public Sources and the German Self-Pay Market

## 1. Escopo e pergunta de viabilidade

**Data de acesso:** 2026-08-10  
**Mercado:** Alemanha  
**Objetivo:** verificar se fontes públicas permitem quantificar ou contextualizar medicamentos GLP-1/GIP adquiridos fora do reembolso regular do GKV.

### Categorias mantidas separadas

- **Pagamento integral pelo paciente:** desembolso integral, não apenas copagamento legal do GKV.
- **Prescrição privada para segurado do GKV:** receita privada não prova, por si só, identidade do pagador final ou ausência de reembolso posterior.
- **PKV:** cobertura ou reembolso por seguro privado não equivale automaticamente a self-pay.
- **Venda sem receita:** categoria do painel IQVIA aplicável a produtos que podem ser vendidos dessa forma; não deve ser atribuída a GLP-1/GIP de prescrição obrigatória.
- **Canal legal de prescrição:** farmácia pública ou Versandapotheke autorizada, com receita válida quando obrigatória.
- **Canais ilegais, importação pessoal e compras transfronteiriças:** não fazem parte automaticamente do mercado farmacêutico alemão medido por painéis de farmácia.
- **Indicação:** diabetes, obesidade/controle de peso e uso off-label permanecem distintos. A molécula ou o canal de pagamento não determina sozinho a indicação.

## 2. Tabela de evidências

| Fonte | Publicação e período | Métrica/unidade | Cobertura declarada | Acesso | Natureza da evidência | Utilidade e limite |
|---|---|---|---|---|---|---|
| **IQVIA Flashlight 98 — GLP-1 Agonisten** — IQVIA Commercial GmbH & Co. OHG. URL: https://www.iqvia.com/-/media/iqvia/pdfs/germany/flashlight/iqvia-flashlight-ausgabe-98.pdf | Fevereiro de 2024; recorte principal de novembro de 2023 | 292.000 `Units` dispensadas; participação apresentada de 80% GKV e 20% PKV; valor próximo de EUR 50 milhões calculado a APU | Grupo ATC4 A10S0 no mercado alemão; fonte PharmaScope National/DPM Combined. Não separa segurados GKV pagando privadamente, PKV reembolsada e self-pay | PDF público; sem tabela reutilizável, CSV, XLSX ou API pública identificada | `projected panel estimate` | Valor pontual contextual. `Units` não são pacientes; APU não é gasto líquido nem preço efetivamente pago. A categoria apresentada como PKV não quantifica self-pay |
| **IQVIA Infografik — Eine Klasse für sich** — IQVIA Commercial GmbH & Co. OHG. URL: https://www.iqvia.com/-/media/iqvia/pdfs/germany/library/infographic/2024_iqvia-infografik-glp1.pdf | Maio de 2024; MAT 02/2024 e MAT 2023 | Tendências/ranking de faturamento; faturamento agregado GKV + PKV em EUR a APU | GLP-1 antidiabéticos A10S0 no ambulatório alemão | PDF público; gráfico/infográfico, sem série tabular reutilizável | `projected panel estimate` | Confirma atividade e crescimento de mercado, mas agrega pagadores, usa APU e não identifica indicação, self-pay, pacientes ou custo efetivo |
| **IQVIA Marktbericht Q3 2025 — metodologia PharmaScope** — IQVIA Commercial GmbH & Co. OHG. URL: https://www.iqvia.com/-/media/iqvia/pdfs/germany/library/publications/iqvia-marktbericht-q3-2025.pdf | Publicado em dezembro de 2025; mercado até Q3 2025 | Pacotes dispensados e faturamento; descreve GKV, receitas privadas e vendas sem receita | GKV: liquidações dos centros de faturamento; receitas privadas e vendas sem receita: amostra de cerca de 6.500 farmácias públicas; Versandhandel: painel e projeção separados | PDF público; não fornece série GLP-1 detalhada, microdados, CSV, XLSX ou API pública | `projected panel estimate` para PKV/bar/mail order; componente GKV baseado em `official administrative data` processado comercialmente | Principal fonte metodológica. Demonstra que o produto comercial pode distinguir canais, mas os dados detalhados não estão publicados |
| **IQVIA Marktbericht Classic Q3 2024 — notas de métricas** — IQVIA Commercial GmbH & Co. OHG. URL: https://www.iqvia.com/-/media/iqvia/pdfs/germany/library/publications/iqvia-pharma-marktbericht-classic-q3-2024.pdf | Dezembro de 2024; Q1–Q3 2024 | Apothekenmarkt em pacotes; valor a preço de lista APU; GKV em pacotes e despesas calculadas após descontos especificados; clínica em unidades de contagem | Farmácias, Versandhandel, hospital e GKV, conforme capítulo | PDF público; gráficos e notas, sem dados GLP-1 self-pay reutilizáveis | `projected panel estimate` e dados administrativos agregados, conforme o segmento | Permite interpretar métricas e impedir equivalências incorretas; não quantifica o segmento buscado |
| **Anti-Diabetes-Spritze als “Schlankmacher”** — IQVIA Germany. URL: https://www.iqvia.com/de-de/locations/germany/newsroom/2023/07/anti-diabetes-injections-as-slimmer-products | 04/07/2023; números de 2022 | Pacotes vendidos de dulaglutida e semaglutida | Mercado alemão; canal, painel, pagador e método não detalhados suficientemente na página | HTML público; valores pontuais, sem arquivo reutilizável | `projected panel estimate` com documentação pública incompleta | Contexto de volume por substância; não permite separar indicação, marca, pagador ou self-pay |
| **IQVIA Third Party Access Program** — IQVIA. URL: https://www.iqvia.com/de-de/about-us/third-party-access-program | Página vigente na data de acesso | Licenciamento de dados sindicados, subnacionais, RWD e MIDAS | Produtos e metodologias proprietários IQVIA | Acesso comercial/licenciado; não é API pública | Evidência sobre condição de acesso | Confirma o caráter proprietário do núcleo de dados e as restrições de reutilização |
| **G-BA — Verordnungsausschluss von Lifestyle-Arzneimitteln**. URL: https://www.g-ba.de/themen/arzneimittel/arzneimittel-richtlinie-anlagen/lifestyle/ | Página vigente; regra legal e decisões correntes | Regra de reembolso, sem valor de mercado | GKV alemão | HTML público | `official administrative data` / evidência regulatória | Confirma que medicamentos de redução de peso listados não podem ser prescritos como benefício GKV; não mede compras privadas |
| **G-BA — exclusão de Wegovy**. URL: https://www.g-ba.de/presse/pressemitteilungen-meldungen/1170/ | 21/03/2024 | Decisão regulatória; sem volume ou faturamento | Wegovy na indicação de redução de peso e GKV | HTML público | `official administrative data` / evidência regulatória | Sustenta a possibilidade de demanda fora do GKV. Semaglutida em outras marcas/indicações não deve ser automaticamente classificada da mesma forma |
| **G-BA — Tirzepatid und Ritlecitinib als Lifestyle-Arzneimittel**. URL: https://www.g-ba.de/service/fachnews/150/ | 2024 | Regra por indicação; sem valor de mercado | Tirzepatida para redução de peso versus diabetes tipo 2 | HTML público | `official administrative data` / evidência regulatória | Demonstra que o status de reembolso depende da indicação; não permite inferi-la a partir da substância |
| **BfArM — GLP-1-Rezeptor-Agonisten**. URL: https://www.bfarm.de/DE/Arzneimittel/Arzneimittelinformationen/Lieferengpaesse/glp.html | 24/06/2024; contexto desde 2023 | Informação de disponibilidade e risco; sem tamanho de mercado | Medicamentos GLP-1 na Alemanha, com ênfase em abastecimento e uso apropriado | HTML público | `official administrative data` e evidência contextual | Confirma indicações concorrentes, escassez e preocupação com uso off-label; não quantifica canais ou pagamentos |
| **BfArM — Illegaler Arzneimittelversand**. URL: https://www.bfarm.de/DE/Arzneimittel/Arzneimittelinformationen/Versandhandels-Register/Illegaler-Arzneimittelversand/_node.html | Página vigente | Regras e sinais de ilegalidade; sem métricas de mercado | Versandhandel legal e ofertas ilegais | HTML público | `official administrative data` / evidência regulatória | Delimita o mercado legal. Não fornece base para estimar compras ilegais ou transfronteiriças |
| **BMG — Einfuhr von Arzneimitteln nach Deutschland**. URL: https://www.bundesgesundheitsministerium.de/arzneimittel-aus-dem-ausland/seite | Página vigente em 2025/2026 | Regras de importação; sem métricas de mercado | Importações pessoais, viagem e Versandhandel transfronteiriço | HTML público | `official administrative data` / evidência regulatória | Impede incluir silenciosamente importações pessoais no mercado alemão; não quantifica o canal |
| **BMG — Zuzahlung und Erstattung von Arzneimitteln**. URL: https://www.bundesgesundheitsministerium.de/zuzahlung-und-erstattung-arzneimittel | Atualização em 04/12/2025 | Regras de copagamento e reembolso | GKV alemão | HTML público | `official administrative data` / evidência regulatória | Diferencia copagamento GKV de pagamento integral e confirma exclusão geral de produtos para regulação de peso; não mede GLP-1 self-pay |
| **Destatis — Gesundheitsausgaben 2023 / financiamento**. URL: https://www.destatis.de/DE/Presse/Pressemitteilungen/2025/07/PD25_268_23611.html | Publicado em 2025; ano 2023 | Gastos gerais financiados por domicílios privados, em EUR | Sistema de saúde alemão agregado | HTML público e tabelas agregadas | `official administrative data` / estimativa oficial agregada | Contextualiza financiamento privado, mas não isola farmácias, GLP-1/GIP, receitas privadas ou indicação no nível necessário |

## 3. Disponibilidade pública da IQVIA

### Conteúdo identificado

- **FATO VERIFICADO:** existem relatórios trimestrais, artigos, press releases, newsletters, gráficos e infográficos publicamente acessíveis. Algumas publicações mais recentes requerem formulário gratuito para acesso; outras são diretamente acessíveis.
- **FATO VERIFICADO:** materiais públicos contêm valores pontuais e explicações metodológicas úteis, inclusive para PharmaScope National, DKM, painel de Versandhandel e mercado GKV.
- **FATO VERIFICADO:** o PharmaScope comercial abrange dispensações de farmácias públicas para GKV, receitas privadas e vendas sem receita. O GKV deriva de faturamentos de centros de processamento; receitas privadas e vendas sem receita são estimadas a partir de amostra de aproximadamente 6.500 farmácias. Versandhandel usa painel e projeção próprios.
- **FATO VERIFICADO:** a IQVIA descreve produtos de dados licenciados e metodologias proprietárias no Third Party Access Program.
- **NÃO IDENTIFICADO:** API pública, CSV, XLSX, microdados ou série tabular pública de GLP-1/GIP que permita reproduzir a separação entre GKV, PKV, receita privada e self-pay.
- **LIMITAÇÃO:** gráficos e PDFs permitem reproduzir apenas os números impressos, não a consulta subjacente, a seleção de produtos, a projeção do painel ou uma série completa.

### O que as métricas medem

- **PharmaScope/apothekenmarkt:** pacotes dispensados (`sell-out`) e faturamento calculado conforme a base de preço declarada.
- **IQVIA DPM:** relatório de compras das farmácias, conceitualmente próximo de `sell-in`; não deve ser confundido com dispensação ao paciente.
- **GKV:** prescrições/dispensações faturadas ao GKV, com metodologia distinta do painel privado/bar.
- **Clínica:** consumo em unidades de contagem e faturamento avaliado; não equivale ao mercado ambulatorial self-pay.
- **NÃO CONFIRMADO:** número de pacientes únicos no conjunto público analisado.

## 4. Cobertura do mercado

| Canal/categoria | Cobertura publicamente documentada | Capacidade de isolar GLP-1 self-pay publicamente |
|---|---|---|
| Farmácias públicas | Sim; amostra/projeção para privado e bar, faturamento para GKV | Não |
| Farmácias hospitalares | Painel hospitalar separado | Não é adequado ao self-pay ambulatorial |
| Versandapotheken | Painel separado e projeção; compras de consumidores alemães | Não para GLP-1 self-pay nas fontes públicas |
| Prescrições GKV | Dados de faturamento dos centros de processamento | Sim para o segmento GKV agregado nos produtos, mas não como série pública GLP-1 completa |
| Prescrições privadas | Incluídas no produto comercial e estimadas por painel | Não separadas de forma reproduzível nas fontes públicas GLP-1 |
| Pagamento direto integral | Não identificado como série pública específica | Não |
| PKV | Alguns recortes públicos usam a categoria PKV | Não é possível determinar reembolso versus desembolso final |
| Canal ilegal | Fora do mercado legal; BfArM oferece apenas contexto regulatório | Não |
| Importação pessoal/transfronteiriça | Regras oficiais disponíveis | Não quantificada |

- **FATO VERIFICADO:** a amostra declarada para privado/bar nas publicações mais recentes é de aproximadamente 6.500 farmácias, com projeção para o mercado.
- **NÃO CONFIRMADO:** fração exata do universo de farmácias e erro da projeção para cada produto GLP-1/GIP.
- **NÃO CONFIRMADO:** cobertura completa de todos os canais digitais, clínicas privadas, importações individuais ou compras transfronteiriças.
- **LIMITAÇÃO:** resultados projetados do painel não são contagens administrativas integrais.

## 5. Produtos, indicações e nível de detalhe

- **FATO VERIFICADO:** fontes públicas apresentam recortes por classe ATC, substância e, em alguns casos, produto/ranking.
- **FATO VERIFICADO:** a classe A10S0 usada nos materiais públicos é rotulada como GLP-1 antidiabéticos e pode combinar produtos com diferentes marcas e indicações.
- **NÃO IDENTIFICADO:** tabela pública completa por substância, marca, apresentação, PZN, volume, faturamento, pagador e mês.
- **NÃO IDENTIFICADO:** indicação clínica observada na dispensação pública utilizada para os valores de mercado.
- **LIMITAÇÃO:** uma substância pode existir em produtos e indicações distintas. Semaglutida para diabetes e semaglutida para controle de peso não podem ser inferidas apenas pelo princípio ativo.
- **LIMITAÇÃO:** uso off-label não é automaticamente identificável em venda, receita ou dispensação sem diagnóstico/indicação vinculada e metodologia apropriada.

## 6. Métricas e conceitos comerciais

| Conceito | Tratamento nesta avaliação |
|---|---|
| `sales value` | Valor monetário na base de preço declarada; não equivale a volume, custo líquido ou desembolso do paciente |
| `sales volume` | Pacotes, unidades de contagem ou outra unidade declarada; não equivale a pacientes |
| `sell-in` | Compra/entrada na farmácia; não prova dispensação final |
| `sell-out` | Dispensação/venda pela farmácia; não prova consumo ou adesão |
| Prescrição emitida | Não necessariamente dispensada |
| Dispensação | Pacote entregue; não identifica automaticamente indicação ou uso efetivo |
| Faturamento bruto/lista | Pode usar APU/AVP e excluir descontos ou reembolsos |
| Faturamento líquido | Exige descontos, rebates e ajustes documentados; não disponível para o segmento buscado |
| Pacientes | Pessoas únicas; não deriváveis de pacotes sem regime, dose, duração e persistência |
| Mercado total | Pode combinar clínica e farmácia; não equivale ao mercado ambulatorial self-pay |
| Painel projetado | Estimativa estatística do mercado; não registro administrativo completo |
| Crescimento percentual | Não determina tamanho absoluto sem base comparável |

Nenhuma conversão entre essas métricas foi realizada.

## 7. Capacidade de quantificar o mercado autofinanciado

| Pergunta | Classificação | Fundamentação |
|---|---|---|
| Tamanho em euros | `não identificável` | Os valores públicos GLP-1 agregam GKV/PKV ou usam APU; não isolam desembolso integral |
| Número de embalagens | `não identificável` | Há volumes totais/pontuais, mas não série pública isolada de self-pay |
| Prescrições ou dispensações | `disponível apenas comercialmente` para separações detalhadas | O produto comercial mede receitas privadas e outras dispensações; a série não é pública |
| Número de pacientes | `não identificável` | Pacotes/units não identificam pacientes únicos ou duração |
| Evolução temporal | `disponível apenas comercialmente` | Materiais públicos fornecem recortes e crescimento, não série completa reproduzível do self-pay |
| Participação relativa self-pay | `não identificável` | A divisão GKV/PKV publicada não equivale a GKV versus self-pay |
| Diabetes versus obesidade | `não identificável` | ATC, substância, marca ou pagador não substituem indicação observada |
| Segurados GKV pagando privadamente | `não identificável` | Receita privada não revela de forma pública o status de seguro e o pagador final |

**Conclusão quantitativa:** não é possível produzir uma estimativa defensável e reproduzível do mercado alemão autofinanciado de GLP-1/GIP apenas com as fontes públicas identificadas.

## 8. Natureza da evidência

- **`observed market data`:** transações captadas nas farmácias participantes antes da projeção; os microdados não são públicos.
- **`projected panel estimate`:** resultados PharmaScope de receitas privadas, vendas sem receita e Versandhandel extrapolados de painéis; esta é a classificação dos números públicos de mercado quando aplicável.
- **`company-reported figure`:** valores publicados pela própria IQVIA ou fabricantes sem dados subjacentes reutilizáveis; úteis apenas dentro da definição divulgada.
- **`official administrative data`:** regras de G-BA/BMG/BfArM e faturamentos GKV usados como insumo; não constituem, por si, contagem de self-pay.
- **`derived calculation`:** nenhum cálculo foi produzido nesta etapa. Futuras diferenças entre mercado total e GKV só seriam válidas se cobertura, métricas e universos fossem equivalentes.
- **`modelled assumption`:** qualquer estimativa futura da parcela self-pay sem observação direta deverá ser rotulada assim.
- **`anecdotal/contextual evidence`:** relatos de mídia ou redes sociais sobre acesso, custo ou uso; não devem sustentar números centrais.

## 9. Compatibilidade com o projeto

- **Medir diretamente o mercado autofinanciado:** não com o conteúdo público identificado.
- **Fornecer ordem de grandeza:** parcialmente, para o mercado GLP-1 agregado em determinados meses/períodos; não para self-pay isolado.
- **Contextualizar demanda fora do GKV:** sim, combinando os recortes IQVIA com as regras oficiais de exclusão de reembolso, sem quantificar a parcela.
- **Apoiar cenários de uptake:** apenas como contexto ou limite qualitativo. Nenhuma taxa de uptake deve ser calibrada diretamente a esses recortes.
- **Evitar equiparar ausência de reembolso a ausência de consumo:** sim; os painéis reconhecem receitas privadas e as regras oficiais criam um canal legítimo fora do GKV.
- **Complementar WIdO/GKV:** sim, qualitativamente. Não subtrair automaticamente WIdO de IQVIA total, pois métricas, preços, produtos e projeções podem divergir.
- **Reprodução futura em Python/Pandas:** reprodução integral não é possível a partir de PDFs/HTML. Valores pontuais podem ser transcritos com fonte; série estruturada exigiria licença comercial ou outra fonte pública ainda não identificada.

**Papel recomendado:** evidência contextual e valores pontuais claramente rotulados, nunca base quantitativa principal do mercado self-pay.

## 10. Limitações críticas

1. Parte relevante dos dados IQVIA é proprietária e licenciada comercialmente.
2. Séries completas, consultas detalhadas e microdados não estão publicamente acessíveis.
3. Vendas, pacotes ou `Units` não equivalem a pacientes tratados.
4. Prescrições privadas, cobertura PKV e pagamento direto são conceitos diferentes; os recortes públicos não permitem separá-los adequadamente.
5. A indicação clínica pode não estar observada nos dados públicos de mercado.
6. Uso off-label não pode ser identificado automaticamente por substância, marca ou canal.
7. APU, AVP, faturamento e custo efetivo incorporam bases de preço e descontos diferentes.
8. Farmácias, Versandhandel e hospitais usam painéis/metodologias distintos; alguns canais são projetados ou podem estar incompletos.
9. Combinar ou subtrair fontes pode gerar dupla contagem ou diferenças artificiais de universo e métrica.
10. A parcela de segurados GKV que paga privadamente não é identificável nas fontes públicas encontradas.
11. Mercado autofinanciado não equivale à população clínica ou regulatoriamente elegível.
12. Dados de mercado não demonstram efetividade clínica nem economia futura para o GKV.
13. Compras ilegais, falsificações, importações pessoais e compras transfronteiriças não devem ser adicionadas ao mercado legal sem evidência própria.
14. A classificação `PKV` em um gráfico público não prova reembolso pela PKV nem pagamento integral pelo paciente.
15. A exclusão de reembolso para weight management não permite inferir que toda venda privada de GLP-1/GIP se destina à obesidade.

## 11. Decisão

### Classificação geral: `CONTEXTUAL DATASET`

### A. As fontes públicas da IQVIA são adequadas como dataset quantitativo reproduzível?

**`NO-GO`.** Há PDFs, HTML, infográficos e números pontuais, mas não uma série tabular pública com seleção reproduzível, microdados, API ou arquivos CSV/XLSX para GLP-1/GIP por pagador e canal. Os produtos capazes de fornecer maior detalhe são proprietários.

### B. São adequadas como evidência contextual ou para fornecer valores pontuais?

**`GO` para uso contextual e pontual.** Os materiais permitem documentar ordem de grandeza do mercado agregado, esclarecer métricas e mostrar que receitas privadas e canais fora do GKV existem. Cada valor deverá conservar período, ATC/produto, unidade, base de preço, cobertura e natureza de painel projetado.

### C. É possível quantificar defensavelmente o mercado autofinanciado apenas com fontes públicas?

**`NO-GO`.** As fontes públicas não separam de maneira reproduzível pagamento integral, receita privada de segurado GKV, reembolso PKV, indicação, pacientes e canais externos. Não será construída estimativa própria nesta fase.

### D. Qual papel exato essas fontes poderão desempenhar no projeto?

As fontes IQVIA serão usadas como **evidência contextual e, quando indispensável, como fonte de valores pontuais publicados**, demonstrando que ausência de reembolso regular do GKV não significa ausência de consumo. Elas não serão o dataset quantitativo principal, não definirão uptake e não sustentarão uma estimativa central do mercado self-pay. Fontes de G-BA, BMG e BfArM delimitarão regras de reembolso, prescrição e mercado legal; não serão usadas para inventar volumes.

## 12. Pendências e dívida documental

- Aguardar aprovação do usuário para a classificação e o papel proposto.
- Caso a quantificação self-pay seja indispensável posteriormente, decidir explicitamente entre: adquirir dados comerciais, buscar uma nova fonte pública com separação comprovada ou tratar o parâmetro como `modelled assumption` com faixa de sensibilidade.
- Registrar em etapa futura os termos de uso antes de reproduzir qualquer gráfico ou número IQVIA em entregáveis públicos.
- O `TASKS.md` mantém status desatualizados de tarefas já concluídas. Essa inconsistência foi registrada como dívida documental e não foi corrigida, conforme instrução.
- Nenhum dataset ou arquivo comercial foi baixado, nenhum paywall ou cadastro foi contornado, nenhum contato comercial foi realizado, nenhum código foi criado e nenhuma estimativa própria foi calculada.
