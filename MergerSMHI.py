import os
import pandas as pd


class MergerSMHI:
    def __init__(self):
        '''Merge smaller files'''
        pass
    
    def merge_dfs(self, targets:list):
        targets.sort()
        for i in range(len(targets)):
            try:
                if i in range(0, 100, 2):

                    print('Processing:\n1:', targets[i], '\n2:', targets[i+1])

                    df1 = pd.read_csv('data/target/' + targets[i])  #, parse_dates = ['Datum', 'Tid (UTC)'])
                    df2 = pd.read_csv('data/target/' + targets[i+1])
                    df2 = df2.drop('Datum', axis = 1)

                    new_name = 'data/merged/' + \
                        targets[i].split('_')[2] + '_' + \
                            targets[i].split('_')[3]

                    # print(new_name)

                    df = pd.concat([df1, df2.drop('Tid (UTC)', axis = 1)], axis=1, join = 'inner')
                    # print(df)
                    
                    df.to_csv(f'{new_name}.csv', index = False)

            except (ValueError, KeyError):
                print(f'Error merging { targets[i] } and { targets[i+1]}')
                return f'Error merging { targets[i] } and { targets[i+1]}'


    def concat_date_time(self, targets:list):
        targets.sort
        for i in range(len(targets)):
            print('Processing:', targets[i])

            df = pd.read_csv('data/merged/' + targets[i])#, parse_dates=['Datum', 'Tid (UTC)'])
            df['timestamp'] = df['Datum'] + ' ' + df['Tid (UTC)']# + df['Lufttemperatur'] + df['Max av MedelVindhastighet']

            dfc = df.drop(['Datum', 'Tid (UTC)'], axis = 1)
            dfc.columns = ['temperature', 'wind_avg', 'timestamp']

            dfc.to_csv('data/final/m_' + targets[i], index = False)

        



if __name__ == '__main__':
    t_targets = os.listdir('data/target')
    m_targets = os.listdir('data/merged')
    merger  = MergerSMHI()

    # merger.merge_dfs(t_targets)
    merger.concat_date_time(m_targets)


