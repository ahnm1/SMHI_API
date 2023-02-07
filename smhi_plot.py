#%%
import  os
import plotly.express as px
import pandas as pd
import numpy as np

#%%
clean_list = os.listdir('clean')

df = pd.read_csv('clean/' + clean_list[0], index_col = 'Datum')
df1 = pd.read_csv('clean/' + clean_list[1], index_col = 'Datum')
df.tail(30)
#%%
# df = pd.DataFrame(np.random.random((200,3)))
# df['Datum'] = pd.date_range('2021-11-1', periods=365*2, freq='D')
# df = df.set_index(['Datum'])
df.loc['2021-11-1':'2022-10-31']

#%%
dfc = df.loc['2021-11-1':'2022-10-31']
dfc1 = df1.loc['2021-11-1':'2022-10-31']


#%%
import plotly.graph_objects as go

df1 = dfc.reset_index()
df2 = dfc1.reset_index()

fig = go.Figure()

fig.add_trace(go.Scatter(x = df1['Datum'],
    y    = df1['Lufttemperatur'],
    name = '',
    line = dict(color='firebrick',
    width = 4)))

fig.add_trace(go.Scatter(x = df2['Datum'],
    y    = df1['Lufttemperatur'],
    name = '',
    line = dict(color='royalblue',
    width = 4)))

fig.update_layout(title='Temperatures',
                   xaxis_title='Month',
                   yaxis_title='Temperature (degrees C)')

