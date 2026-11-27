# CVP em Pernambuco | Aprendizado de Máquina

**PPGIA · UFRPE · Disciplina de Aprendizado de Máquina**

Uma abordagem de aprendizado de máquina para o agrupamento de municípios e a classificação de estados de risco de crimes violentos contra o patrimônio em Pernambuco.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Plotly Dash](https://img.shields.io/badge/Plotly-Dash-119DFF) ![Google Colab](https://img.shields.io/badge/Google-Colab-F9AB00)

[**Acessar dashboard**](https://adam-cvp-pernambuco.onrender.com/) · [**Abrir notebook no Colab**](https://colab.research.google.com/github/jamescavalcanti/adam-cvp-pernambuco/blob/main/ADAM_CVP_Pernambuco.ipynb)

## A pesquisa em números

| Período | Territórios | Observações | Registros de CVP |
|:---:|:---:|:---:|:---:|
| 2014–2025 | 185 | 26.640 | 834.398 |

**Fontes:** SDS-PE e IBGE.

## Principais resultados

- **Agrupamento:** quatro perfis históricos com K-Means (escolha interpretativa).
- **Classificação:** Random Forest B com F1 macro de 53,67% no teste temporal.
- **Explicabilidade:** análise SHAP dos atributos do Random Forest B.

## Explore o projeto

| Material | Conteúdo |
|---|---|
| [Notebook](ADAM_CVP_Pernambuco.ipynb) | Metodologia, experimentos e gráficos |
| [Dados](data/) | Bases, resultados e malha geográfica |
| [Aplicação](app.py) | Dashboard interativo em Plotly Dash |
| [Interface](assets/) | Estilos visuais |
| [Testes](tests/) | Validação automatizada |
| [Auditoria](AUDITORIA_REPRODUTIBILIDADE.md) | Evidências e limites de reprodução |
| [Histórico](NOTAS_ATUALIZACAO.md) | Evolução do projeto |

## Execute localmente

Python 3.11:

```bash
pip install -r requirements.txt
python app.py
```

Acesse http://127.0.0.1:8050. Testes: `python -m tests.smoke`.

> O painel apresenta resultados retrospectivos, não previsões em tempo real. Os perfis e classes são analíticos, não classificações oficiais. Ausência de registro não comprova ausência de crime. A reprodução integral dos experimentos tem limitações descritas na auditoria.
