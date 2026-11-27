# Catálogo dos dados do dashboard

Arquivos CSV separados por ponto e vírgula. São insumos do painel, não um pacote integral de reprodução do notebook.

| Arquivo | Finalidade |
|---|---|
| `base_municipio_mes_com_taxa.csv` | Painel territorial mensal com ocorrências, população e taxas |
| `avaliacao_k_clustering.csv` | Sensibilidade ao número de grupos: silhueta e inércia |
| `municipios_clusters_k4.csv` | Atribuição territorial aos quatro perfis históricos |
| `perfil_clusters_k4.csv` | Resumo dos quatro perfis históricos |
| `comparacao_especificacoes_A_B.csv` | Comparação de classificadores A/B |
| `metricas_por_classe_RF_B.csv` | Métricas por classe do Random Forest B |
| `desempenho_territorial_RF_B.csv` | Avaliação territorial do Random Forest B |
| `importancia_SHAP_RF_B.csv` | Importância global dos atributos segundo SHAP |
| `pernambuco.geojson` | Malha territorial IBGE, associada por código territorial |

Os filtros não recalculam os modelos. Consulte a [auditoria](../AUDITORIA_REPRODUTIBILIDADE.md) e o [script da malha](../prepare_map.py).
