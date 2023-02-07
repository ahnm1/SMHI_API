import requests
import pandas as pd

class HandleSMHI:

    def __init__(self):
        
        '''Handle .csv files from SMHI'''
        pass

    def get_raw_csv(self, name, station_id, parameter):
        ''''Save to "data/raw" folder.'''

        endpoint_entry = \
            'https://opendata-download-metobs.smhi.se/api/'
    
        download_url = endpoint_entry + \
            f'version/1.0/parameter/{parameter}/' + \
            f'station/{station_id}/period/corrected-archive/data.csv'
        
        re = requests.get(download_url)
        
        try:
            with open(f'data/raw/{name}_{station_id}_{parameter}.csv',
                'w', encoding='utf-8-sig') as out:
                    out.write(re.text)
                    return 1
                    
        except:
            return 0

    def clean_csv(self, filename:str):
        '''Clear all unwanted columns and rows
        saves to "data/clean" folder'''

        df = pd.read_csv('data/raw/' + 
            f'{ filename }',
            delimiter = ';',
            skiprows  = 9,
            index_col = False)
    
        dfc = df[df.columns[:3]]

        return dfc.to_csv('data/clean/' + f'clean_{ filename }', index = False)


    def get_data_between(self, start_date, end_date, filename):
        '''Save data between dates into "data/target" folder'''

        df  = pd.read_csv('data/clean/' + filename, index_col = 'Datum')

        dfc = df.loc[start_date:end_date]

        try:
            dfc.to_csv('data/target/' + \
                filename.replace('clean', f'{ start_date }_{ end_date }'))
            return 1
        
        except:
            return 0



if __name__ == '__main__':
    a = HandleSMHI()
    # a.get_raw_csv('Falsterbo_A', 52240, 1)
    # a.clean_csv('Falsterbo_a_52240_1.csv')
    a.get_data_between('2021-11-01', '2022-10-31', 'clean_Falsterbo_a_52240_1.csv')