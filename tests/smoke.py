from app import app,base,filtered,update
assert len(base)==26640
assert base.TOTAL_CVP.sum()==834398
assert base.COD_IBGE.nunique()==185
assert len(filtered(None,None,None,[2014,2014]))==2220
assert len(update(None,None,None,2014,2025))==4
assert app.server.test_client().get('/').status_code==200
assert app.server.test_client().get('/_dash-layout').status_code==200
print('Smoke test OK')
from app import make_map
fig = make_map(base)
assert len(fig.data[0].locations) == 185
assert len(make_map(filtered(None,[base.MUNICIPIO.iloc[0]],None,[2014,2014])).data[0].locations)==1
