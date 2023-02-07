#%%
import os
import pandas as pd


#%%

def clean(csv_file:str, skip:int):
    print(f'Processing: { csv_file }')

    df = pd.read_csv('data/raw/' + 
        f'{ csv_file }',
        delimiter = ';',
        skiprows  = skip,
        index_col = False)
    
    dfc = df[df.columns[:3]]

    return dfc.to_csv('data/clean/' + f'clean_{ csv_file }', index = False)


#%%
raw_list = os.listdir('data/raw')#'data/raw')

print(raw_list)
for file in raw_list:
    print(file)
    if file.startswith('Halmstad') or \
        file.startswith('Osby') or \
            file.startswith('Lund'):

        clean(file, 12)

    elif file.startswith('Kristianstad'):
        clean(file, 13)

    else:
        clean(file, 9)



#%%
## Gets pretty name from filename
### In order to append to "City" column?

print(raw_list[0].split('_')[0].capitalize())
