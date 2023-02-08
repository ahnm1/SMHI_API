import os
import pandas as pd


class MergerSMHI:
    '''Merge smaller files.     \n    
    ----------                     
    Methods:                       
    ----------                  
        merge_dfs(targets : list)      
        concat_date_time(targets : list)
    '''
    
    def __init__(self):    
        pass
    
    def merge_dfs(self, targets:list):
        '''Will search in folder: data/target/  \n
        Saves merged file to: data/merged/      \n                
        Parameters:                           
        ----------                            
            target : list   
        ----------                             
        Example : os.listdir('data/target') '''       
            

        targets.sort()
        target_path = 'data/target/'

        for i in range(len(targets)):
            try:

                # try changing '100' to 'len(targets)'
                if i in range(0, 200, 2):

                    print('Merging:\n1:', targets[i], '\n2:', targets[i+1])

                    df1 = pd.read_csv(target_path + targets[i])
                    df2 = pd.read_csv(target_path + targets[i+1])


                    new_name = 'data/merged/' + \
                        targets[i].split('_')[2] + '_' + \
                            targets[i].split('_')[3]

                    df = df1.merge(df2, on = ['Datum', 'Tid (UTC)'], how = 'outer')

                    df.to_csv(f'{new_name}.csv', index = False)

            except (ValueError, KeyError):
                print(f'Error merging { targets[i] } and { targets[i+1]}')
                return f'Error merging { targets[i] } and { targets[i+1]}'


    def concat_date_time(self, targets:list):
        '''Searches in folder: data/merged/.                \n
        Concatenates 'Date' and 'Time' into 'timestamp'.    \n
        Adds 'f_' to beginning of filename.                 \n
        Saves merget file to: data/final/.                  \n                               
        Parameters:                                   
        ----------                                    
            target : list
        ----------     
        Example : os.listdir('data/merged') '''

        targets.sort
        for i in range(len(targets)):
            print(f'Concatenating: {targets[i]}')

            df = pd.read_csv('data/merged/' + targets[i])
            df['timestamp'] = df['Datum'] + ' ' + df['Tid (UTC)']

            dfc = df.drop(['Datum', 'Tid (UTC)'], axis = 1)
            dfc.columns = ['temperature', 'wind_avg', 'timestamp']
            dfc         = dfc[['timestamp', 'temperature', 'wind_avg']]

            # dfcc = dfc.reinde
            dfc.to_csv('data/final/f_' + targets[i], index = False)

        

if __name__ == '__main__':
    t_targets = os.listdir('data/target')[:2]
    m_targets = os.listdir('data/merged')[:1]
    merger  = MergerSMHI()

    merger.merge_dfs(t_targets)
    merger.concat_date_time(m_targets)


