# Análise de CVP em Pernambuco com Aprendizado de Máquina

Projeto desenvolvido na disciplina de Aprendizado de Máquina do Programa de Pós-Graduação em Informática Aplicada (PPGIA/UFRPE).

## Sobre o projeto

Este trabalho investiga os Crimes Violentos Contra o Patrimônio (CVP) em Pernambuco por meio de duas abordagens complementares de aprendizado de máquina:

1. agrupamento de municípios pernambucanos segundo características do comportamento histórico dos CVP;
2. classificação do estado de risco de CVP correspondente ao mês seguinte.

Foram utilizados dados oficiais da Secretaria de Defesa Social de Pernambuco (SDS-PE), referentes ao período de 2014 a 2025, integrados a informações do Instituto Brasileiro de Geografia e Estatística (IBGE).

## Perguntas de pesquisa

**PP1:** É possível identificar perfis distintos de municípios pernambucanos quanto ao comportamento dos Crimes Violentos Contra o Patrimônio por meio de técnicas de agrupamento?

**PP2:** Com que desempenho modelos de aprendizado supervisionado conseguem classificar o estado de risco de CVP no mês seguinte a partir do comportamento histórico recente dos municípios?

## Metodologia

O trabalho segue o processo de Knowledge Discovery in Databases (KDD).

Na etapa de agrupamento foi utilizado o algoritmo K-Means, considerando características de:

- intensidade média;
- variabilidade;
- tendência temporal;
- sazonalidade.

Foram analisadas diferentes quantidades de clusters. A solução com K=4 foi adotada como representação descritiva por fornecer maior detalhamento interpretativo, apesar de K=2 ter maior silhueta; K=4 não é a solução ótima pela silhueta.

Na etapa de classificação foram avaliados:

- Regressão Logística Softmax;
- SVM com kernel RBF;
- Random Forest;
- XGBoost.

Também foi utilizada uma regra de persistência como referência.

## Principais resultados

A solução de agrupamento adotada identificou quatro perfis, contendo 22, 90, 53 e 20 unidades territoriais (184 municípios e Fernando de Noronha no total).

Na classificação, o Random Forest com atributos históricos, territoriais e socioeconômicos foi selecionado por meio de validação temporal.

No período de teste de 2023 a 2025, o modelo apresentou:

- Acurácia: **55,17%**
- Acurácia balanceada: **52,91%**
- F1 macro: **53,67%**

A análise de explicabilidade com SHAP indicou predominância das variáveis relacionadas ao histórico recente dos CVP, especialmente médias móveis e taxas recentes.

## Resultados complementares da avaliação científica (protocolo distinto)

A aba **Avaliação científica** apresenta os resultados retrospectivos consolidados do estudo internacional. Não devem ser confundidos com as métricas do Random Forest B da disciplina:

| Experimento | F1 macro (%) |
|---|---:|
| XGBoost A, teste completo (2023–2025) | 53,51 |
| Média móvel de seis meses, teste completo | 52,18 |
| XGBoost, apenas meses com linha original | 46,28 |
| Média móvel, apenas meses com linha original | 48,57 |
| Ablação A: sem perfis | 53,49 |
| Ablação B: com grupos | 53,41 |
| Ablação C: distâncias a centroides | 53,14 |

**Atenção:** 5.368 de 26.640 combinações território-mês não possuíam linha na extração e foram codificadas com zero. Isso não demonstra ausência real de crimes. A avaliação de 2023–2025 é retrospectiva e foi previamente explorada; não equivale a uma validação prospectiva intocada. O SHAP disponível no dashboard explica somente o Random Forest B, e não o XGBoost.

## Implantação no Render

A aplicação existente continua em **Plotly Dash** e usa o mesmo `Procfile` (`web: gunicorn app:server`) e as mesmas dependências. Nenhuma variável de ambiente adicional é exigida por esta alteração. Após revisar as mudanças, execute os testes e então publique na branch conectada ao Render.

## Arquivo principal

O notebook completo da análise está disponível neste repositório:

`ADAM_CVP_Pernambuco.ipynb`

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Matplotlib
- Google Colab

## Autor

**Jamerson Cavalcanti**  
Programa de Pós-Graduação em Informática Aplicada – PPGIA  
Universidade Federal Rural de Pernambuco – UFRPE
