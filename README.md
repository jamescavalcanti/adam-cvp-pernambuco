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

Foram analisadas diferentes quantidades de clusters. A solução com K=4 foi adotada como principal por fornecer maior detalhamento interpretativo dos perfis municipais.

Na etapa de classificação foram avaliados:

- Regressão Logística Softmax;
- SVM com kernel RBF;
- Random Forest;
- XGBoost.

Também foi utilizada uma regra de persistência como referência.

## Principais resultados

A solução de agrupamento adotada identificou quatro perfis, contendo 22, 90, 53 e 20 municípios.

Na classificação, o Random Forest com atributos históricos, territoriais e socioeconômicos foi selecionado por meio de validação temporal.

No período de teste de 2023 a 2025, o modelo apresentou:

- Acurácia: **55,17%**
- Acurácia balanceada: **52,91%**
- F1 macro: **53,67%**

A análise de explicabilidade com SHAP indicou predominância das variáveis relacionadas ao histórico recente dos CVP, especialmente médias móveis e taxas recentes.

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
