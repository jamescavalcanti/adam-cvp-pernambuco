# Auditoria de reprodutibilidade — ADAM (10/11/2026)

## Materiais conferidos
- Notebook original compartilhado com professores: `ADAM_CVP_Pernambuco.ipynb`, 80 células na `main`.
- Notebook consolidado do Colab: `ADAM_CVP_COLAB_COM_FECHAMENTO_GRAFICOS.ipynb`, 82 células.
- Arquivos de resultados já exportados do Colab: `ADAM_RESULTADOS_RECUPERADOS.zip`.
- Pacote de entrada previamente enviado: `ADAM_CVP_Colab_arquivos(2).zip`.

## Evidências
- Os resultados históricos de silhueta do arquivo exportado são coerentes com os valores arredondados do artigo: K2=0,4549; K3=0,3492; K4=0,3609; K5=0,3675; K6=0,3500.
- A solução K4 possui 185 unidades, com grupos de 22, 90, 53 e 20 (ordem de rótulos pode variar).
- O notebook da revisão preserva o fluxo original e acrescenta a exportação de figuras e CSVs.
- O notebook usa uma célula de upload de ZIP no Colab e define `PROJECT=/content/ADAM_CVP_COLAB` e `DATA=PROJECT/data/processed`.
- O ZIP de entrada disponível contém scripts e dados brutos/validados, **mas não contém** a pasta `data/processed` pronta. A execução integral depende de produzir esses artefatos nas etapas anteriores e/ou de um pacote de dados preparado.
- Uma célula utiliza `!pip -q install xgboost`, comando específico do ambiente Jupyter/Colab; não deve ser interpretado como erro de sintaxe Python do notebook.
- A nova célula foi verificada estruturalmente, **mas não foi reexecutada ponta a ponta** em sessão limpa. Resultados exportados previamente não provam reprodutibilidade independente.

## Critérios para mesclar a PR
1. Confirmar a origem e o preparo de todos os CSVs esperados em `data/processed`.
2. Executar o notebook em Colab novo e registrar versões de dependências, parâmetros e sementes.
3. Comparar CSVs e PNGs com os resultados históricos e com o artigo.
4. Revisar o `app.py` separadamente; o dashboard não faz parte desta PR.

## Escopo da revisão
Esta auditoria não substitui os dados de entrada nem reinterpreta ausência de linha como ausência confirmada de crime. Não altera `app.py` ou o deploy do Render.

## Validação independente do fechamento — concluída
Em ambiente Python independente, com o CSV `perfil_municipios_para_clustering.csv` exportado do Colab, foram executados `StandardScaler`, `KMeans(random_state=42, n_init=50)`, `silhouette_score` e a célula de fechamento do notebook consolidado. Os resultados foram reproduzidos:

| K | Silhueta | Inércia | Menor grupo |
|---|---:|---:|---:|
| 2 | 0,454948 | 417,573909 | 55 |
| 3 | 0,349204 | 315,435275 | 35 |
| 4 | 0,360860 | 246,706192 | 20 |
| 5 | 0,367515 | 200,458901 | 1 |
| 6 | 0,349952 | 165,219102 | 1 |
| 7 | 0,337378 | 143,384341 | 1 |
| 8 | 0,318648 | 121,332249 | 1 |

O teste gerou com sucesso CSVs, PNGs e `ADAM_FECHAMENTO_GRAFICOS_RESULTADOS.zip`. Os tamanhos de K4 foram 53, 20, 22 e 90. Esta validação **não equivale à execução integral do notebook**, que inclui integração populacional, treinamento, avaliação e SHAP. Os dados processados necessários existem no pacote de resultados recuperados, mas não no ZIP original de entrada; não foram adicionados ao repositório público.

## Execução independente adicional — preparação e modelos preliminares
- Foi montado ambiente local com `ADAM_COLAB_PACOTE_COMPLETO_VALIDACAO.zip`, contendo os dados preparados e scripts originais.
- A sintaxe Python de todas as células do notebook consolidado foi validada por AST (ignorando somente a sintaxe de instalação `!pip` específica do Colab): **sem erros**.
- `ETAPA_CLASSIFICACAO_DIAGNOSTICO.py` foi executado com sucesso e confirmou as distribuições de classes e o baseline de persistência.
- `ETAPA_CLASSIFICACAO_MODELOS.py` foi executado com sucesso: Softmax obteve acurácia 0,5341, acurácia balanceada 0,5015 e F1 macro 0,5101; persistência obteve F1 macro 0,4796. **Estes são experimentos preliminares desse script, não o Random Forest B final do artigo.**
- A etapa final RF B / XGBoost / SHAP **ainda não foi reexecutada**; suas métricas permanecem fundamentadas nos arquivos exportados previamente pelo Colab. Não confundir sucesso do script preliminar com validação completa da especificação B.

## Inspeção do dashboard publicado
O arquivo `app.py` usa Plotly Dash e define as tabelas do dashboard como `pd.DataFrame({...})` com valores consolidados **incorporados no próprio código**. Não há leitura automática dos CSVs gerados pelo notebook. Portanto, atualizar o notebook ou o README não atualiza os indicadores exibidos no Render. Isso não é necessariamente um erro: é uma escolha de publicação estática. A atualização do dashboard requer conferência linha a linha dos valores do artigo e dos CSVs antes de modificar `app.py`. Nenhuma alteração foi feita no dashboard.
