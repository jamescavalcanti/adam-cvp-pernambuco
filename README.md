# Aprendizado de máquina aplicado aos CVP em Pernambuco

**Pesquisa aplicada · PPGIA / Universidade Federal Rural de Pernambuco (UFRPE)**

Uma abordagem de aprendizado de máquina para o agrupamento de municípios e a classificação de estados de risco de crimes violentos contra o patrimônio em Pernambuco.

[Dashboard público](https://adam-cvp-pernambuco.onrender.com/) · [Notebook científico](ADAM_CVP_Pernambuco.ipynb) · [Auditoria de reprodutibilidade](AUDITORIA_REPRODUTIBILIDADE.md) · [Testes automatizados](https://github.com/jamescavalcanti/adam-cvp-pernambuco/actions)

## Objetivos

- PP1: identificar perfis territoriais históricos de CVP por agrupamento K-Means.
- PP2: avaliar a classificação do estado relativo de CVP no mês seguinte.

## Dados e resultados

| Indicador | Valor |
|---|---:|
| Período | 2014–2025 |
| Unidades territoriais | 185 (184 municípios e Fernando de Noronha) |
| Observações território-mês | 26.640 |
| Ocorrências registradas | 834.398 |
| Perfis históricos | 4 |
| F1 macro do Random Forest B no teste | 53,67% |

Fontes: SDS-PE e IBGE. K=4 é uma escolha interpretativa, não o máximo da silhueta. Os estados de risco são classes analíticas, não classificações oficiais. Ausência de registro não comprova ausência de crime.

## Dashboard

Aplicação Python desenvolvida com **Plotly Dash**, Pandas e Plotly, com filtros territoriais e temporais, mapa GeoJSON, indicadores, gráficos e exportação CSV. Os resultados de classificação e SHAP são históricos, exportados do estudo; o painel não treina modelos nem realiza previsões em tempo real.

## Organização do repositório

| Caminho | Finalidade |
|---|---|
| `app.py` | Aplicação Dash |
| `data/` | Bases agregadas, resultados científicos e malha geográfica |
| `assets/` | Estilos da interface |
| `tests/` | Testes de integridade e funcionamento |
| `ADAM_CVP_Pernambuco.ipynb` | Notebook científico |
| `AUDITORIA_REPRODUTIBILIDADE.md` | Evidências e limites de reprodução |
| `NOTAS_ATUALIZACAO.md` | Histórico de atualização |
| `prepare_map.py` | Preparação da malha IBGE |
| `requirements.txt`, `Procfile` | Dependências e hospedagem |

## Execução local

Com Python 3.11 ou superior:

```bash
pip install -r requirements.txt
python app.py
```

Abra http://127.0.0.1:8050. Para executar a validação automatizada:

```bash
python -m tests.smoke
```

A malha já está incluída no repositório. O script de preparação é opcional para sua atualização.

## Limitações e reprodutibilidade

O painel apresenta resultados retrospectivos. Os filtros não recalculam os agrupamentos nem os modelos. SHAP descreve a importância dos atributos no Random Forest B, sem estabelecer causalidade. Consulte a auditoria para distinguir resultados recuperados de experimentos efetivamente reproduzidos. Os testes do dashboard não equivalem à reprodução integral dos experimentos científicos.
