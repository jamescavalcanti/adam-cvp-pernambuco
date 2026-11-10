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

## Estado da revisão científica (novembro de 2026)

O artigo da disciplina foi revisado para aderência à estrutura do modelo docente (resumo e abstract, introdução, objetivos, referencial teórico, trabalhos relacionados, método, análise exploratória, resultados, discussão e considerações finais). A seção de aplicativo Flutter do modelo não integra o escopo desta pesquisa. A declaração de uso de IA está no artigo, antes das referências.

**Limites de interpretação:** os dados de urbanização de 2010 foram utilizados como covariáveis estruturais fixas; 5.368 combinações território-mês sem linha na extração foram codificadas operacionalmente como zero, sem confirmação de ausência real de crime; os resultados de 2023–2025 são retrospectivos e esse período já foi examinado exploratoriamente. A escolha de K=4 foi interpretativa, não a melhor solução segundo a silhueta média.

## Principais resultados

A solução de agrupamento adotada identificou quatro perfis, contendo 22, 90, 53 e 20 unidades territoriais (184 municípios e Fernando de Noronha no total).

Na classificação, o Random Forest com atributos históricos, territoriais e socioeconômicos foi selecionado por meio de validação temporal.

No período de teste de 2023 a 2025, o modelo apresentou:

- Acurácia: **55,17%**
- Acurácia balanceada: **52,91%**
- F1 macro: **53,67%**

No treinamento final, o F1 macro foi **58,03%**; a diferença calculada com os valores arredondados é **4,36 pontos percentuais**. A diferença não prova isoladamente sobreajuste. O conjunto de teste contém **6.660 observações**.

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

## Dashboard de leitura dos resultados

O arquivo `app.py` é um painel demonstrativo em Plotly Dash, com resultados consolidados **incorporados diretamente no código**. Ele não lê automaticamente os CSVs do Colab e não produz predições em tempo real. A aba de classificação separa o desempenho final do Random Forest B (treino F1 macro 58,03%; teste 53,67%) do baseline de persistência calculado em experimento preliminar distinto. A aba de agrupamento mostra a curva de silhuetas K=2..8 reproduzida a partir dos dados exportados. SHAP refere-se exclusivamente ao RF B.

A branch `revisao-adam-colab-graficos-2026` contém melhorias propostas para o notebook e o painel, submetidas à revisão #1. Não confundir a branch de revisão com a implantação da `main`.

## Implantação no Render

A aplicação existente continua em **Plotly Dash** e usa o mesmo `Procfile` (`web: gunicorn app:server`) e as mesmas dependências. Nenhuma variável de ambiente adicional é exigida por esta alteração. Após revisar as mudanças, execute os testes e então publique na branch conectada ao Render.

## Organização e reprodutibilidade

O notebook contém as etapas experimentais; os resultados do artigo devem ser reproduzidos respeitando o protocolo temporal e as diferenças entre execuções complementares. A inércia e algumas silhuetas de execuções distintas não devem ser combinadas sem conferência das configurações. O SHAP apresentado se refere exclusivamente ao Random Forest B.

A documentação científica não deve ser interpretada como ferramenta operacional de previsão ou classificação prospectiva validada para decisões de segurança pública.

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
