#%%
import  os
import plotly.graph_objects as go
import pandas as pd

#%%
final_path = 'data/final/'
clean_list = os.listdir('data/final')

df = pd.read_csv(final_path + clean_list[0], index_col = 'timestamp')
df1 = pd.read_csv(final_path + clean_list[1], index_col = 'timestamp')
df.tail(30)

#%%


df1 = df.reset_index()
# df2 = dfc1.reset_index()

fig = go.Figure()

fig.add_trace(go.Scatter(x = df1['timestamp'],
    y    = df1['wind_avg'],
    name = 'temp',
    line = dict(
        color = 'firebrick',
        width = 2,
        )
    )
)

fig.add_trace(go.Scatter(x = df1['timestamp'],
    y    = df1['temperature'],
    name = 'wind',
    line = dict(
        color = 'royalblue',
        width = 2
        )
    )
)

fig.update_layout(title='Temperature & Wind',
                   xaxis_title='Month',
                   yaxis_title='Value'
                )


# %%
