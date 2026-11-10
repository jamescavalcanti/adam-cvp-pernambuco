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
