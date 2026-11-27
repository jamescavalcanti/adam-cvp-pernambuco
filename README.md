# ADAM 2.0 — protótipo
Execute pip install -r requirements.txt e python app.py. Dados agregados do ZIP recuperado. Validação de sintaxe e integração das bases realizada; execução Dash ainda pendente. Mapa geográfico não incluído nesta etapa.

## Mapa municipal e teste
Execute `python prepare_map.py` para baixar a malha do IBGE e validar os 185 códigos. Sem a malha, o painel informa a indisponibilidade do mapa. Execute `python -m tests.smoke` após instalar as dependências. A taxa municipal no mapa usa ocorrências divididas pela soma das populações mensais do recorte, vezes 100 mil.
