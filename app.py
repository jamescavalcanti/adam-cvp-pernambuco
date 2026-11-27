from pathlib import Path
import pandas as pd
import json
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State, callback, dash_table

ROOT=Path(__file__).parent/'data'
def load(name): return pd.read_csv(ROOT/(name+'.csv'),sep=';')
base=load('base_municipio_mes_com_taxa')
base['DATA_MES']=pd.to_datetime(base.DATA_MES)
clusters=load('municipios_clusters_k4')
base=base.merge(clusters[['MUNICIPIO','PERFIL_K4']],on='MUNICIPIO',validate='many_to_one')
models=load('comparacao_especificacoes_A_B')
shap=load('importancia_SHAP_RF_B')
k=load('avaliacao_k_clustering')
app=Dash(__name__); server=app.server
app.title='Aprendizado de máquina | CVP em Pernambuco'
def graph(fig): return dcc.Graph(figure=fig,config={'displaylogo':False})
def table(df): return dash_table.DataTable(data=df.to_dict('records'),columns=[{'name':c,'id':c} for c in df],page_size=12,style_table={'overflowX':'auto'},style_cell={'textAlign':'left','padding':'8px'})
def options(s): return [{'label':str(x),'value':x} for x in sorted(s.unique())]
def card(label,value): return html.Div([html.Small(label),html.H2(value)],className='metric')
app.layout=html.Div([html.Header([html.H1('Uma abordagem de aprendizado de máquina para o agrupamento de municípios e a classificação de estados de risco de crimes violentos contra o patrimônio em Pernambuco',style={'fontSize':'clamp(1.35rem, 2.5vw, 2.1rem)','lineHeight':'1.3'}),html.P('Inteligência territorial • CVP em Pernambuco • 2014–2025 | Pesquisa aplicada UFRPE')]),dcc.Tabs([
 dcc.Tab(label='Exploração territorial',children=[html.Div([html.Div(['Região',dcc.Dropdown(options(base.REGIAO),multi=True,id='region')]),html.Div(['Município',dcc.Dropdown(options(base.MUNICIPIO),multi=True,id='city')]),html.Div(['Perfil histórico K=4',dcc.Dropdown(options(base.PERFIL_K4),multi=True,id='profile')]),html.Div([html.Label('Ano inicial'),dcc.Dropdown(list(range(2014,2026)),2014,id='year-start',clearable=False)]),html.Div([html.Label('Ano final'),dcc.Dropdown(list(range(2014,2026)),2025,id='year-end',clearable=False)])],className='filters'),html.Div(id='metrics',className='metrics'),dcc.Graph(id='map'),dcc.Graph(id='series'),dcc.Graph(id='ranking'),html.Button('Exportar recorte CSV',id='export'),dcc.Download(id='download')]),
 dcc.Tab(label='Agrupamentos',children=[html.P('Perfis históricos fixos; K=4 escolhido por interpretação, não pela maior silhueta.'),graph(px.bar(clusters.groupby('PERFIL_K4',as_index=False).size(),x='PERFIL_K4',y='size',title='Territórios por perfil')),graph(px.line(k,x='K',y='SILHUETA_MEDIA',markers=True,title='Sensibilidade ao número de grupos')),graph(px.line(k,x='K',y='INERCIA',markers=True,title='Método do cotovelo')),table(clusters)]),
 dcc.Tab(label='Modelos de IA',children=[html.P('Resultados exportados da validação temporal 2021–2022; não são previsões em tempo real.'),graph(px.bar(models,x='Modelo',y='F1 Macro',color='Especificação',barmode='group',title='F1 macro (%) — validação')),table(models),html.H3('Teste RF B — métricas por classe'),table(load('metricas_por_classe_RF_B')),html.H3('Desempenho territorial'),table(load('desempenho_territorial_RF_B'))]),
 dcc.Tab(label='Explicabilidade',children=[html.P('Importância global SHAP: associação com a saída do modelo, não causalidade.'),graph(px.bar(shap.sort_values('Importância SHAP média'),x='Importância SHAP média',y='Variável',orientation='h',height=700))]),
 dcc.Tab(label='Metodologia',children=[html.H2('Sobre a pesquisa'),html.P('Fontes: SDS-PE e IBGE. Painel retrospectivo de 184 municípios e Fernando de Noronha. Agrupamento K-Means e classificação do mês seguinte. Resultados históricos exportados do notebook; não houve novo treinamento nesta versão.'),html.P('A taxa agregada mensal é a soma de ocorrências dividida pela soma das populações do mês, multiplicada por 100 mil. Os filtros não recalculam os modelos ou perfis. Zero registrado não comprova ausência de crime.')])])],className='shell')
def filtered(regions,cities,profiles,years):
 d=base[base.ANO.between(*years)]
 for col,values in [('REGIAO',regions),('MUNICIPIO',cities),('PERFIL_K4',profiles)]:
  if values: d=d[d[col].isin(values)]
 return d
def make_map(d):
 path=ROOT/'pernambuco.geojson'
 if not path.exists():
  fig=go.Figure(); fig.add_annotation(text='Malha municipal IBGE ainda não instalada.',showarrow=False); fig.update_layout(xaxis_visible=False,yaxis_visible=False,height=300); return fig
 geo=json.loads(path.read_text(encoding='utf-8'))
 agg=d.groupby(['COD_IBGE','MUNICIPIO'],as_index=False).agg(CVP=('TOTAL_CVP','sum'),pop=('POPULACAO_ANO','sum'))
 agg['Taxa média mensal']=agg.CVP/agg['pop']*100000
 agg['codigo']=agg.COD_IBGE.astype(str)
 fig=px.choropleth(agg,geojson=geo,locations='codigo',featureidkey='properties.codarea',color='Taxa média mensal',hover_name='MUNICIPIO',hover_data=['CVP'],title='Taxa mensal por 100 mil habitantes no recorte',color_continuous_scale='Blues')
 fig.update_geos(fitbounds='locations',visible=False); fig.update_layout(height=500,margin=dict(l=10,r=10,t=60,b=10)); return fig

@callback(Output('metrics','children'),Output('series','figure'),Output('ranking','figure'),Output('map','figure'),Input('region','value'),Input('city','value'),Input('profile','value'),Input('year-start','value'),Input('year-end','value'))
def update(r,c,p,start,end):
 y=sorted([start,end])
 d=filtered(r,c,p,y); monthly=d.groupby('DATA_MES',as_index=False).agg(CVP=('TOTAL_CVP','sum'),Pop=('POPULACAO_ANO','sum')); monthly['Taxa por 100 mil']=monthly.CVP/monthly.Pop*100000
 rank=d.groupby('MUNICIPIO',as_index=False).TOTAL_CVP.sum().nlargest(15,'TOTAL_CVP').sort_values('TOTAL_CVP')
 return [card('Ocorrências',f'{d.TOTAL_CVP.sum():,}'.replace(',','.')),card('Territórios',d.MUNICIPIO.nunique()),card('Observações',len(d))],px.line(monthly,x='DATA_MES',y='Taxa por 100 mil',title='Taxa mensal agregada por 100 mil habitantes'),px.bar(rank,x='TOTAL_CVP',y='MUNICIPIO',orientation='h',title='15 territórios com mais registros no recorte'),make_map(d)
@callback(Output('download','data'),Input('export','n_clicks'),State('region','value'),State('city','value'),State('profile','value'),State('year-start','value'),State('year-end','value'),prevent_initial_call=True)
def download(n,r,c,p,start,end): return dcc.send_data_frame(filtered(r,c,p,sorted([start,end])).to_csv,'adam_recorte.csv',index=False,sep=';')
if __name__=='__main__': app.run(debug=False)
