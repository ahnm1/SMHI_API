#%%
import  os
import plotly.graph_objects as go
import pandas as pd

# CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
cdir = os.getcwd()
print("Current Directory: ", cdir)
print("Parent Directory: ", os.path.dirname(cdir))

#%%
final_path = os.path.dirname(cdir) + '/data/final/'
clean_list = os.listdir(final_path)

print(final_path)
print(clean_list)

#%%
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
