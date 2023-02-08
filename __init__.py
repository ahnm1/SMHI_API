import os
import pandas as pd
from HandleSMHI import HandleSMHI
from MergerSMHI import MergerSMHI

def get_raw(parameter = 'temperature'):
    '''Works only with "temperature" and "wind" parameter   \n
    Iterates over 'data/station_keys.csv' '''
    
    handler       = HandleSMHI()
    weather_value = 0

    if parameter == 'wind':
        weather_value = 25

    elif parameter == 'temperature':
        weather_value = 1

    with open('data/station_keys.csv', 'r', encoding = 'utf-8-sig') as station_keys:

        for line in station_keys.readlines()[1:]:
            city    = line.split(',')[0].capitalize().replace(' ', '_')
            city_id = line.split(',')[1].replace('\n', '')

            print(f"Getting .csv for:\n{ city }\nID: { city_id }")

            handler.get_raw_csv(name = city, station_id = city_id, parameter = weather_value)


def clean_raw():
    raw_list = os.listdir('data/raw')
    handler  = HandleSMHI()

    for file in raw_list:
        print(f'Cleaning:', '\ndata/raw/' + file)
        handler.clean_csv(file)


def save_samples(start_date, end_date):
    clean_list = os.listdir('data/clean')
    handler    = HandleSMHI()

    for file in clean_list:
        handler.get_data_between(start_date, end_date, file)


def merge_samples():
    targets = os.listdir('data/target')
    merger  = MergerSMHI()

    merger.merge_dfs(targets)
    merger.concat_date_time(os.listdir('data/merged'))

if __name__ == '__main__':
    get_raw()
    get_raw('wind')
    clean_raw()
    save_samples('2021-10-01', '2022-09-30')
    merge_samples()
    pass
