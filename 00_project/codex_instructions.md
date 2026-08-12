# Instruções permanentes do projeto

Este documento define as regras permanentes que devem orientar todo o trabalho realizado neste projeto.

## Comunicação

- Conversar com o usuário sempre em português do Brasil.
- Apresentar todas as respostas em um único bloco, para facilitar copiar e colar.
- Antes de escrever qualquer código, explicar rapidamente o plano.
- Sempre informar em qual arquivo pretende trabalhar antes de criá-lo ou alterá-lo.
- Nunca alterar arquivos importantes sem avisar previamente o usuário.
- Sempre perguntar ao usuário quando faltar alguma informação necessária.
- Sempre sugerir primeiro a solução mais simples que atenda corretamente ao objetivo.

## Código e nomenclatura

- Escrever todo o código em inglês.
- Escrever todos os comentários do código em inglês.
- Usar inglês nos nomes de variáveis, funções, classes, arquivos e pastas.
- Sempre utilizar boas práticas de engenharia de software e Data Analytics.
- Sempre manter o projeto reproduzível.

## Dados

- Nunca modificar ou sobrescrever arquivos RAW.
- Sempre preservar os dados originais.
- Nunca inventar dados.
- Manter os arquivos originais em `01_raw_data` de forma íntegra e imutável.
- Realizar limpezas, transformações e enriquecimentos somente em arquivos derivados, fora da camada RAW.

## Transparência analítica

- Sempre diferenciar explicitamente:
  - **FATO VERIFICADO:** informação confirmada por dados ou por uma fonte identificável.
  - **HIPÓTESE:** suposição ou proposição que ainda precisa ser testada.
  - **LIMITAÇÃO:** restrição dos dados, do método, da fonte ou da interpretação.
  - **PRÓXIMO PASSO:** ação recomendada para avançar o projeto.
- Sempre documentar decisões importantes, incluindo justificativas, premissas e impactos relevantes.
- Não apresentar correlação como evidência suficiente de causalidade.

## Organização e acompanhamento

- Sempre manter o projeto organizado.
- Manter uma separação clara entre dados RAW, dados processados, código, notebooks, fontes e resultados.
- Atualizar o arquivo `PROJECT_STATUS.md` ao finalizar uma tarefa importante.
- Registrar fontes, versões, datas de acesso, premissas e etapas de processamento necessárias para reproduzir a análise.
- Evitar alterações fora do escopo da tarefa atual.

