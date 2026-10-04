from dash import Dash, dcc, html, dash_table
import pandas as pd
import plotly.express as px

app = Dash(__name__)
server = app.server
app.title = "CVP Pernambuco | ADAM"

# -----------------------------
# Dados consolidados do estudo
# -----------------------------

perfis = pd.DataFrame({
    "Perfil": ["Perfil 1", "Perfil 2", "Perfil 3", "Perfil 4"],
    "Municípios": [22, 90, 53, 20],
    "Taxa média": [3.64, 13.71, 38.62, 77.91],
    "Coef. variação": [2.21, 0.95, 0.69, 0.56],
    "Tendência": [-0.02, -0.06, -0.25, -0.61],
    "Amplitude sazonal": [6.30, 9.39, 18.40, 23.48],
    "% meses zero": [72.63, 21.40, 3.79, 0.17],
})

validacao = pd.DataFrame({
    "Modelo": [
        "Softmax A", "Softmax B",
        "SVM-RBF A", "SVM-RBF B",
        "Random Forest A", "Random Forest B",
        "XGBoost A", "XGBoost B"
    ],
    "Acurácia": [51.91, 51.46, 51.10, 51.26, 52.16, 52.68, 51.98, 51.44],
    "Acurácia balanceada": [52.89, 52.59, 51.74, 52.09, 52.71, 53.39, 52.78, 52.54],
    "F1 macro": [52.40, 52.14, 51.98, 52.09, 52.82, 53.40, 52.70, 52.32],
})

por_classe = pd.DataFrame({
    "Classe": ["Muito Baixo", "Baixo", "Médio", "Alto", "Muito Alto"],
    "Precisão": [0.6859, 0.4636, 0.4307, 0.5475, 0.6207],
    "Recall": [0.7202, 0.4163, 0.4451, 0.5962, 0.4675],
    "F1-score": [0.7026, 0.4387, 0.4378, 0.5708, 0.5333],
    "Suporte": [2134, 1715, 1411, 1092, 308],
})

territorio = pd.DataFrame({
    "Contexto": ["RMR", "Interior"],
    "Acurácia": [65.67, 54.07],
    "Acurácia balanceada": [51.53, 48.23],
    "F1 macro": [53.44, 49.25],
})

shap = pd.DataFrame({
    "Atributo": [
        "Média móvel de 6 meses",
        "Média móvel de 3 meses",
        "Meses sem registro nos últimos 6 meses",
        "Taxa atual",
        "Taxa defasada em 1 mês",
        "Taxa defasada em 2 meses",
        "Log da densidade demográfica",
        "Urbanização de 2010",
        "Região — Sertão",
        "Desvio-padrão de 6 meses",
        "Log do PIB per capita relativo",
    ],
    "SHAP médio absoluto": [
        0.044406, 0.034264, 0.022202, 0.022195, 0.016656, 0.015003,
        0.010302, 0.006913, 0.006461, 0.005612, 0.004761
    ]
})

# -----------------------------
# Figuras
# -----------------------------

fig_perfis_taxa = px.bar(
    perfis, x="Perfil", y="Taxa média",
    title="Taxa média mensal por perfil"
)
fig_perfis_zero = px.bar(
    perfis, x="Perfil", y="% meses zero",
    title="Esparsidade observada no painel"
)

validacao_long = validacao.melt(
    id_vars="Modelo",
    value_vars=["Acurácia", "Acurácia balanceada", "F1 macro"],
    var_name="Métrica",
    value_name="Valor (%)"
)
fig_validacao = px.bar(
    validacao_long,
    x="Modelo", y="Valor (%)", color="Métrica",
    barmode="group",
    title="Validação temporal 2021–2022"
)
fig_validacao.update_layout(xaxis_tickangle=-35)

classe_long = por_classe.melt(
    id_vars=["Classe", "Suporte"],
    value_vars=["Precisão", "Recall", "F1-score"],
    var_name="Métrica",
    value_name="Valor"
)
fig_classes = px.bar(
    classe_long,
    x="Classe", y="Valor", color="Métrica",
    barmode="group",
    title="Desempenho por classe — teste 2023–2025"
)
fig_classes.update_yaxes(range=[0, 1])

territorio_long = territorio.melt(
    id_vars="Contexto",
    value_vars=["Acurácia", "Acurácia balanceada", "F1 macro"],
    var_name="Métrica",
    value_name="Valor (%)"
)
fig_territorio = px.bar(
    territorio_long,
    x="Contexto", y="Valor (%)", color="Métrica",
    barmode="group",
    title="Desempenho por contexto territorial"
)

fig_shap = px.bar(
    shap.sort_values("SHAP médio absoluto"),
    x="SHAP médio absoluto", y="Atributo",
    orientation="h",
    title="Importância global dos atributos — SHAP"
)

# -----------------------------
# Componentes
# -----------------------------

CARD_STYLE = {
    "padding": "18px",
    "border": "1px solid #dfe3e8",
    "borderRadius": "12px",
    "backgroundColor": "white",
    "boxShadow": "0 1px 4px rgba(0,0,0,0.06)",
}

def metric_card(titulo, valor, subtitulo=""):
    return html.Div([
        html.Div(titulo, style={"fontSize": "14px", "color": "#5f6b7a"}),
        html.Div(valor, style={"fontSize": "28px", "fontWeight": "700", "marginTop": "6px"}),
        html.Div(subtitulo, style={"fontSize": "12px", "color": "#6b7280", "marginTop": "4px"}),
    ], style=CARD_STYLE)

app.layout = html.Div([
    html.Div([
        html.H1("Crimes Violentos Contra o Patrimônio em Pernambuco"),
        html.P(
            "Agrupamento de municípios e classificação de estados de risco com aprendizado de máquina."
        ),
        html.P(
            "Projeto acadêmico — PPGIA/UFRPE | Dados de 2014 a 2025",
            style={"color": "#5f6b7a"}
        ),
    ], style={"marginBottom": "20px"}),

    dcc.Tabs([
        dcc.Tab(label="Visão geral", children=[
            html.Div([
                metric_card("Painel analítico", "26.640", "observações município-mês"),
                metric_card("Municípios", "185"),
                metric_card("Ocorrências de CVP", "834.398", "2014–2025"),
                metric_card("Modelo final", "Random Forest B"),
            ], style={
                "display": "grid",
                "gridTemplateColumns": "repeat(auto-fit, minmax(180px, 1fr))",
                "gap": "12px",
                "marginTop": "20px",
                "marginBottom": "22px",
            }),

            html.Div([
                html.H3("Perguntas de pesquisa"),
                html.P([
                    html.Strong("PP1: "),
                    "É possível identificar perfis distintos de municípios pernambucanos quanto ao comportamento dos Crimes Violentos Contra o Patrimônio por meio de técnicas de agrupamento?"
                ]),
                html.P([
                    html.Strong("PP2: "),
                    "Com que desempenho modelos de aprendizado supervisionado conseguem classificar o estado de risco de CVP no mês seguinte a partir do comportamento histórico recente dos municípios?"
                ]),
            ], style=CARD_STYLE),

            html.Div([
                html.H3("Síntese dos resultados"),
                html.P(
                    "Na etapa não supervisionada, K=4 foi adotado como solução principal por oferecer maior resolução interpretativa, "
                    "apesar de K=2 apresentar a maior silhueta média. Na etapa supervisionada, o Random Forest enriquecido com variáveis "
                    "contextuais foi selecionado por validação temporal."
                ),
            ], style={**CARD_STYLE, "marginTop": "16px"}),
        ]),

        dcc.Tab(label="PP1 — Agrupamento", children=[
            html.Div([
                html.Div(dcc.Graph(figure=fig_perfis_taxa)),
                html.Div(dcc.Graph(figure=fig_perfis_zero)),
            ], style={
                "display": "grid",
                "gridTemplateColumns": "repeat(auto-fit, minmax(380px, 1fr))",
                "gap": "12px",
                "marginTop": "20px",
            }),

            html.H3("Perfis municipais"),
            dash_table.DataTable(
                data=perfis.to_dict("records"),
                columns=[{"name": c, "id": c} for c in perfis.columns],
                page_size=10,
                style_table={"overflowX": "auto"},
                style_cell={"padding": "8px", "textAlign": "center"},
                style_header={"fontWeight": "bold"},
            ),

            html.Div([
                html.P(
                    "A solução K=4 possui grupos com 22, 90, 53 e 20 municípios e silhueta média de 0,3609. "
                    "K=2 apresentou maior silhueta média (0,4549), mas mostrou-se mais agregador. "
                    "A interpretação considera também esparsidade, tamanho dos grupos e utilidade analítica."
                ),
                html.P(
                    "O Perfil 1 apresenta forte esparsidade no painel e não deve ser interpretado automaticamente como um grupo de municípios seguros."
                )
            ], style={**CARD_STYLE, "marginTop": "18px"}),
        ]),

        dcc.Tab(label="PP2 — Classificação", children=[
            html.Div([
                metric_card("Acurácia final", "55,17%"),
                metric_card("Acurácia balanceada", "52,91%"),
                metric_card("F1 macro", "53,67%"),
                metric_card("F1 macro — persistência", "47,96%"),
            ], style={
                "display": "grid",
                "gridTemplateColumns": "repeat(auto-fit, minmax(180px, 1fr))",
                "gap": "12px",
                "marginTop": "20px",
            }),

            dcc.Graph(figure=fig_validacao),
            dcc.Graph(figure=fig_classes),
            dcc.Graph(figure=fig_territorio),

            html.Div([
                html.H3("Interpretação"),
                html.P(
                    "O Random Forest B foi selecionado com base na validação temporal de 2021–2022. "
                    "As variáveis socioeconômicas melhoraram o desempenho do Random Forest na validação, "
                    "mas o ganho não se mostrou robusto no teste final de 2023–2025."
                ),
                html.P(
                    "As classes intermediárias, Baixo e Médio, apresentaram maior dificuldade de classificação. "
                    "O desempenho também variou entre RMR e Interior; essa diferença é descritiva e não implica causalidade."
                ),
            ], style=CARD_STYLE),
        ]),

        dcc.Tab(label="Explicabilidade", children=[
            dcc.Graph(figure=fig_shap),
            html.Div([
                html.H3("Leitura do SHAP"),
                html.P(
                    "As médias móveis de 6 e 3 meses foram os atributos mais relevantes globalmente. "
                    "Meses sem registro, taxa atual e taxas defasadas também tiveram contribuição importante."
                ),
                html.P(
                    "Densidade demográfica, urbanização e PIB per capita relativo aparecem com contribuição adicional, "
                    "mas menor que a dinâmica temporal recente."
                ),
                html.P(
                    "Os valores apresentados são importâncias médias absolutas. Eles não indicam causalidade nem a direção do efeito."
                ),
            ], style=CARD_STYLE),
        ]),
    ]),

    html.Hr(style={"marginTop": "28px"}),
    html.P(
        "Fonte: microdados da SDS-PE e informações do IBGE. Estados de risco e perfis são construções analíticas deste estudo.",
        style={"fontSize": "12px", "color": "#6b7280"}
    ),
], style={
    "maxWidth": "1200px",
    "margin": "0 auto",
    "padding": "24px",
    "fontFamily": "Arial, sans-serif",
    "backgroundColor": "#f8fafc",
    "minHeight": "100vh",
})

if __name__ == "__main__":
    app.run(debug=True)
