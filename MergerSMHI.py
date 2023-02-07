import os
import pandas as pd


class MergerSMHI:
    def __init__(self):
        '''Merge smaller files'''
        pass
    
    def merge_dfs(self, targets:list):

        for i in range(len(targets)):
            try:
                if i in range(0, 100, 2):

                    print('Processing:\n1:', targets[i], '\n2:', targets[i+1])

                    df1 = pd.read_csv('data/target/' + targets[i])  #, parse_dates = ['Datum', 'Tid (UTC)'])
                    df2 = pd.read_csv('data/target/' + targets[i+1])

                    # df1 = df1.drop('Datum', axis = 1)
                    df2 = df2.drop('Datum', axis = 1)

                    new_name = 'data/merged/' + \
                        targets[i].split('_')[2] + '_' + \
                            targets[i].split('_')[3] + '.csv'
                    
                    df = pd.concat([df1, df2.drop('Tid (UTC)', axis = 1)], axis=1, join = 'inner')
                    print(df)


                    # Something is messed up above
                    
                    

                    # dfc.columns = ['timestamp', 'temperature', 'wind_avg']
                    # print(dfc)
                    # df.to_csv(new_name, index = False)

                    return f'Wrote: {new_name}'

            except:
                print('NOPE')
                return f'Error merging { targets[i] } and { targets[i+1]}'
        pass



if __name__ == '__main__':
    targets = os.listdir('data/target')[:2]
    merger  = MergerSMHI()

    merger.merge_dfs(targets)


