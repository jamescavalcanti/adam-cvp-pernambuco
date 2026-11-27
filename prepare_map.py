import json
from pathlib import Path
from urllib.request import urlopen
import pandas as pd
root=Path(__file__).parent/'data'
url='https://servicodados.ibge.gov.br/api/v3/malhas/estados/26?formato=application/vnd.geo+json&qualidade=intermediaria&intrarregiao=municipio'
with urlopen(url,timeout=90) as response: geo=json.load(response)
expected=set(pd.read_csv(root/'base_municipio_mes_com_taxa.csv',sep=';').COD_IBGE.astype(str))
actual=set()
for feature in geo['features']:
    code=str(feature['properties']['codarea']); feature['properties']['codarea']=code; actual.add(code)
if expected!=actual or len(geo['features'])!=len(expected): raise ValueError(f'Malha incompatível: faltam {expected-actual}; extras {actual-expected}')
(root/'pernambuco.geojson').write_text(json.dumps(geo,ensure_ascii=False),encoding='utf-8')
print('Malha validada:',len(actual),'territórios')
