#%%
import pandas as pd

df = pd.read_csv('raw/malmö_52350_1.csv', delimiter=';', skiprows = 10)
dfc = df[df.columns[:3]]
dfc


#%%

import os
# import pandas as pd

def clean(csv_file:str, skip:int):
    print(f'Processing: { csv_file }')

    df = pd.read_csv('raw/' + 
        f'{ csv_file }',
        delimiter = ';',
        skiprows  = skip,
        index_col = False)
    
    dfc = df[df.columns[:3]]

    return dfc.to_csv('clean/' + f'clean_{ csv_file }', index = False)


#%%
raw_list = os.listdir('raw')

for file in raw_list[1]:

    if file.startswith('Halmstad_62410_1') or \
        file.startswith('Osby_63220_1') or \
            file.startswith('Lund_53430_1'):

        clean(file, 12)

    elif file.startswith('Kristianstad_64030_1'):
        clean(file, 13)

    else:
        clean(file, 9)


#%%
## Gets pretty name from filename
### In order to append to "City" column?

print(raw_list[0].split('_')[0].capitalize())
