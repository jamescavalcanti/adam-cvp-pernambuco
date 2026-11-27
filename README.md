<div align="center">

# Crimes Violentos contra o Patrimônio em Pernambuco

**Agrupamento territorial e classificação de estados de risco com aprendizado de máquina**

PPGIA · Universidade Federal Rural de Pernambuco

[**▶ Acessar dashboard**](https://adam-cvp-pernambuco.onrender.com/)　·　[**📓 Abrir notebook no Colab**](https://colab.research.google.com/github/jamescavalcanti/adam-cvp-pernambuco/blob/main/ADAM_CVP_Pernambuco.ipynb)

<br>

| 2014–2025 | 185 | 26.640 | 834.398 |
|:---:|:---:|:---:|:---:|
| Período | Territórios | Observações | Ocorrências |

*SDS-PE · IBGE*

</div>

## Resultados

| Agrupamento | Classificação | Explicabilidade |
|:---:|:---:|:---:|
| **4 perfis** | **53,67% F1 macro** | **SHAP** |
| K-Means | Random Forest B · teste temporal | Importância dos atributos |

## Materiais da pesquisa

📓 [**Notebook científico**](ADAM_CVP_Pernambuco.ipynb) — metodologia, experimentos e gráficos

📊 [**Bases e resultados**](data/) — dados agregados e malha territorial

🖥️ [**Aplicação Dash**](app.py) · [Interface](assets/) · [Testes](tests/)

📄 [**Auditoria científica**](AUDITORIA_REPRODUTIBILIDADE.md) · [Histórico de atualizações](NOTAS_ATUALIZACAO.md)

<details>
<summary>Execução local e detalhes técnicos</summary>

Python 3.11 ou superior:

```bash
pip install -r requirements.txt
python app.py
```

Acesse http://127.0.0.1:8050. Testes: `python -m tests.smoke`.

A malha territorial pode ser atualizada com `prepare_map.py`.

</details>

<details>
<summary>Limitações científicas</summary>

K=4 é uma escolha interpretativa, não o máximo da silhueta. O painel apresenta resultados retrospectivos, não previsões em tempo real. Os filtros não recalculam modelos. As classes são analíticas, não classificações oficiais. Ausência de registro não comprova ausência de crime. SHAP não estabelece causalidade. A reprodução integral dos experimentos tem limitações descritas na auditoria.

</details>

---

<div align="center">

Python · Plotly Dash · Pandas · Scikit-learn

</div>
