# Data Feasibility Map — RKI Obesity / GEDA

## 1. Identificação e fonte exata

**Data de acesso:** 2026-08-10

**Instituição responsável:** Robert Koch-Institut (RKI), Alemanha.

### Fontes oficiais avaliadas

1. **GEDA 2019/2020-EHIS — Übergewicht und Adipositas bei Erwachsenen in Deutschland**  
   URL: https://edoc.rki.de/handle/176904/10231  
   Publicação oficial com os indicadores de peso corporal da onda GEDA 2019/2020-EHIS.

2. **GEDA Scientific Use Files (FDZ/RKI)**  
   URL: https://www.rki.de/DE/Aktuelles/Publikationen/Forschungsdaten/FDZ/Datenangebot/GEDA/GEDA_inhalt.html  
   Catálogo oficial dos microdados disponibilizados pelo RKI.

3. **Condições de acesso aos Scientific Use Files**  
   URL: https://www.rki.de/DE/Aktuelles/Publikationen/Forschungsdaten/FDZ/Daten-nutzen/Scientific-Use-Files/SUF.html

4. **FAQ do Forschungsdatenzentrum do RKI**  
   URL: https://www.rki.de/SharedDocs/FAQs/DE/FDZ/FAQ-Liste.html

5. **GEDA Dashboard**  
   URL: https://www.rki.de/DE/Themen/Nichtuebertragbare-Krankheiten/Studien-und-Surveillance/Studien/GEDA/GEDA-Dashboard.html

6. **Indicador oficial GBE: Adipositas und Übergewicht**  
   URL: https://www.gbe.rki.de/DE/Themen/EinflussfaktorenAufDieGesundheit/GesundheitsUndRisikoverhalten/Koerpergewicht/AdipositasUndUebergewicht/adipositasUndUebergewicht_node.html

7. **Entwicklung von Adipositas und Rauchen bei Erwachsenen in Deutschland — 2003 bis 2023**  
   URL: https://edoc.rki.de/handle/176904/12455  
   Publicação oficial de 2025 que apresenta estimativas de obesidade até 2023.

8. **DEGS1 Scientific Use File**  
   URL: https://www.rki.de/DE/Aktuelles/Publikationen/Forschungsdaten/FDZ/Datenangebot/DEGS/DEGS_inhalt.html  
   Fonte oficial complementar com medidas antropométricas examinadas em 2008–2011.

### Método de coleta e anos disponíveis

- **FATO VERIFICADO — GEDA 2019/2020-EHIS:** pesquisa transversal nacional por entrevista telefônica assistida por computador (CATI), realizada entre abril de 2019 e setembro de 2020.
- **FATO VERIFICADO — ondas com SUF:** 2009, 2010, 2012, 2014/2015-EHIS e 2019/2020-EHIS.
- **FATO VERIFICADO — evidência mais recente:** a publicação de tendências de 2025 fornece estimativas agregadas separadas para 2022 e 2023. A coleta de peso e altura em GEDA 2021 ocorreu apenas durante três meses e não foi usada na análise de tendência por insuficiência amostral para estratificações precisas.
- **NÃO CONFIRMADO:** disponibilização de Scientific Use Files para GEDA 2022 ou 2023. O catálogo oficial consultado lista SUFs somente até 2019/2020.

## 2. População e cobertura

- **FATO VERIFICADO — população-alvo GEDA 2019/2020:** população de língua alemã residente em domicílios privados na Alemanha, alcançável por telefone fixo ou móvel.
- **FATO VERIFICADO — idade:** a pesquisa geral incluiu pessoas com 15 anos ou mais; a análise de obesidade e o SUF considerado para adultos utilizam participantes com 18 anos ou mais. Não foi identificada idade máxima.
- **FATO VERIFICADO — cobertura:** nacional. O desenho permite análises por estado federal no GEDA 2019/2020, sujeito a tamanho amostral e precisão.
- **FATO VERIFICADO — desenho amostral:** amostra aleatória dual-frame, com números de telefone fixo e móvel segundo o sistema ADM.
- **FATO VERIFICADO — tamanho:** 23.001 participantes na pesquisa GEDA 2019/2020-EHIS; 22.414 adultos com informações válidas de peso e altura na análise publicada. O SUF 2019/2020 lista 22.708 casos e 310 variáveis. As diferenças refletem populações analíticas e preparação do arquivo, não devem ser tratadas como inconsistência sem inspeção adicional.
- **FATO VERIFICADO — resposta:** taxa de resposta 3 da AAPOR de 21,6%.
- **FATO VERIFICADO — inclusão na análise de obesidade:** adultos com valores válidos de altura e peso. Gestantes informaram o peso anterior à gravidez.
- **NÃO CONFIRMADO:** todos os critérios operacionais de exclusão do SUF e das estimativas de 2022/2023, além dos documentados nas publicações consultadas.

## 3. Definição de obesidade

- **FATO VERIFICADO:** o RKI calcula BMI/IMC como peso em quilogramas dividido pela altura em metros ao quadrado.
- **FATO VERIFICADO — limites utilizados:**
  - underweight: BMI < 18,5;
  - normal weight: BMI de 18,5 a < 25;
  - overweight, incluindo obesity: BMI >= 25;
  - obesity: BMI >= 30;
  - obesity class I: BMI de 30 a < 35;
  - obesity class II: BMI de 35 a < 40;
  - obesity class III: BMI >= 40.
- **FATO VERIFICADO:** peso e altura no GEDA são autorrelatados, não medidos.
- **FATO VERIFICADO:** a publicação reconhece que peso tende a ser subestimado e altura superestimada, produzindo estimativas de BMI e obesidade inferiores às obtidas por medição.
- **FATO VERIFICADO:** os pesos amostrais corrigem probabilidades de seleção e calibram a amostra à população por características demográficas e educacionais.
- **NÃO CONFIRMADO:** existência de correção antropométrica específica para o viés de peso e altura autorrelatados. A ponderação amostral não equivale a essa correção.
- **LIMITAÇÃO:** a publicação de 2019/2020 define as classes I–III, mas sua tabela principal publica obesidade combinada; a obtenção de prevalências separadas por classe exigiria variáveis adequadas no microdado e cálculo reproduzível.

## 4. Granularidade

| Dimensão | Disponibilidade verificada |
|---|---|
| Ano/onda | Sim: ondas históricas; estimativas agregadas separadas para 2022 e 2023 |
| Sexo | Sim |
| Faixa etária | Sim; a publicação recente usa 18–29, 30–44, 45–64 e 65+ |
| Estado federal | Sim no GEDA 2019/2020 e no respectivo SUF; não confirmado para os agregados de 2022/2023 |
| BMI class | Limites definidos; classes separadas potencialmente deriváveis do microdado, mas não publicadas na tabela principal consultada |
| Condição socioeconômica | Educação disponível nas publicações e ponderação; outras medidas não confirmadas |
| Diabetes/comorbidades | Não confirmado para cruzamento no SUF sem inspeção do dicionário de variáveis |

- **FATO VERIFICADO:** o dashboard GEDA oferece visualizações por sexo, idade e estado federal; a publicação de 2019/2020 também apresenta estratificação educacional.
- **NÃO CONFIRMADO:** combinação simultânea de todas as dimensões, pois células pequenas podem impedir estimativas precisas.
- **LIMITAÇÃO:** o dataset permite estimar a população adulta com obesidade por estratos disponíveis, mas não identifica automaticamente quem possui indicação clínica, contraindicações, cobertura, diagnóstico ou intenção de tratamento.

## 5. Acesso técnico

- **FATO VERIFICADO:** há tabelas, publicações em PDF, páginas de indicadores e dashboard oficial.
- **FATO VERIFICADO:** existem microdados anonimizados GEDA até 2019/2020 como Scientific Use Files.
- **FATO VERIFICADO:** o acesso aos microdados exige solicitação ao FDZ/RKI, interesse científico justificado, descrição do projeto, compromisso de proteção de dados e contrato de uso. Uso comercial é excluído; trabalhos científicos e acadêmicos são elegíveis conforme as condições do RKI.
- **FATO VERIFICADO:** os formatos informados para SUFs são SAS, SPSS e Stata. CSV e XLSX não foram confirmados como formatos nativos.
- **FATO VERIFICADO:** o uso ocorre no âmbito da instituição científica solicitante e a transferência é realizada por servidor seguro.
- **NÃO CONFIRMADO:** API pública ou exportação reutilizável do dashboard em CSV/XLSX.
- **HIPÓTESE TÉCNICA:** arquivos SAS/SPSS/Stata podem ser lidos em Python/Pandas com bibliotecas apropriadas, tornando a reprodução tecnicamente viável após autorização e recebimento. Isso não foi testado e nenhum código foi criado.
- **LIMITAÇÃO:** a reprodução é simples para tabelas agregadas publicadas, mas análises customizadas por classe de BMI, estado ou comorbidade dependem de acesso ao SUF, documentação de variáveis e precisão amostral.

## 6. Natureza da evidência

| Elemento | Classificação | Interpretação |
|---|---|---|
| Respostas individuais sobre altura e peso | `observed survey data` | Observadas na pesquisa, mas autorrelatadas |
| Prevalências publicadas pelo RKI | `weighted estimate` | Estimativas ponderadas, com intervalos de confiança; não são contagens censitárias |
| Padronização por idade nas tendências | `weighted estimate` | Ajuste estatístico oficial para comparação temporal |
| Correção do viés de autorrelato | `external assumption` | Não confirmada no GEDA; qualquer ajuste futuro exigirá fonte e documentação próprias |
| Projeção de 2019/2020 ou 2023 para 2026 | `modelled estimate` | Não é resultado diretamente observado pelo RKI |
| População potencialmente elegível para GLP-1/GIP | `modelled estimate` | Exige critérios clínicos/regulatórios e parâmetros adicionais |
| Uptake, tratamento e custos evitáveis | `external assumption` ou `modelled estimate` | Fora do escopo desta avaliação e não definidos |

## 7. Compatibilidade com o projeto

- **Estimar prevalência nacional de obesidade:** sim, por estimativas oficiais ponderadas.
- **Segmentar por idade e sexo:** sim.
- **Distinguir graus de obesidade:** condicionalmente. Os limites são definidos e podem ser derivados de BMI no microdado, mas a disponibilidade e precisão das classes separadas precisam ser confirmadas após acesso.
- **Aproximar população potencialmente elegível para GLP-1/GIP:** apenas como ponto de partida para cenários modelados. Obesidade prevalente não equivale a elegibilidade clínica ou regulatória.
- **Combinar com outras fontes:** possível apenas de forma agregada e após harmonização de período, idade, sexo, geografia e definição:
  - RKI Diabetes: contexto epidemiológico, sem ligação individual;
  - WIdO: utilização ambulatorial reembolsada pelo GKV, sem atribuir indicação a prescrições;
  - Destatis Disease Costs: baseline econômico oficial nacional, sem equivalência automática com custos do GKV.
- **LIMITAÇÃO:** não há chave ou desenho que permita ligação pessoa a pessoa entre essas fontes.

## 8. Limitações críticas

1. **Peso e altura autorrelatados:** tendem a subestimar BMI e prevalência de obesidade; a ponderação populacional não corrige automaticamente esse erro de medida.
2. **Prevalência populacional versus obesidade diagnosticada:** GEDA estima obesidade pela informação antropométrica autorrelatada; isso não comprova diagnóstico registrado no sistema de saúde.
3. **Obesidade versus elegibilidade para GLP-1/GIP:** BMI isolado não incorpora todas as indicações regulatórias, comorbidades, contraindicações, avaliação médica ou condições de reembolso.
4. **Diferenças metodológicas entre ondas:** amostragem, modo de coleta e formulação das perguntas mudaram. Comparações temporais devem usar os ajustes oficiais e reconhecer comparabilidade limitada.
5. **Extrapolação para 2026:** mesmo o dado agregado mais recente confirmado é de 2023. Projetá-lo para 2026 constituirá estimativa modelada, com incerteza explícita.
6. **Cobertura pelo GKV:** a população residencial pesquisada não é uma coorte do GKV; não é possível inferir automaticamente seguro, reembolso ou cobertura pelo GKV.
7. **Baixa taxa de resposta e células pequenas:** a ponderação reduz, mas não elimina, risco de viés de não resposta; estratificações múltiplas podem perder precisão.
8. **DEGS1 como comparação:** possui altura e peso medidos, mas é antigo (2008–2011), abrange 18–79 anos e não deve substituir uma estimativa atual.

## 9. Decisão

### `CONDITIONAL GO`

**Justificativa:** o RKI/GEDA é adequado como fonte oficial primária para estimar a prevalência nacional de obesidade em adultos e segmentá-la por idade, sexo e, conforme a onda, educação e estado federal. A evidência agregada chega a 2023, enquanto o SUF disponível confirmado chega a 2019/2020. O uso para classes de obesidade e segmentações customizadas depende de acesso ao microdado, confirmação das variáveis e avaliação da precisão.

**Papel exato no projeto:** fornecer o baseline epidemiológico populacional oficial de obesidade na Alemanha. As estimativas GEDA não serão tratadas como obesidade diagnosticada, população do GKV ou população automaticamente elegível para GLP-1/GIP. Qualquer passagem da prevalência à elegibilidade em 2026 será um cenário modelado, separado dos dados observados e acompanhado de fontes, pressupostos e análise de sensibilidade.

## 10. Pendências antes do uso analítico

- Obter aprovação do usuário para esta avaliação.
- Em etapa futura autorizada, verificar o dicionário do SUF 2019/2020 para BMI contínuo, diabetes, comorbidades e variáveis socioeconômicas.
- Confirmar precisão amostral das classes de obesidade nos estratos necessários.
- Definir, com evidência clínica/regulatória própria, os critérios de elegibilidade; não derivá-los automaticamente da prevalência.
- Não foram realizados download, criação de código ou análise de dados nesta tarefa.
