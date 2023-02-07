#%%
from pprint import pprint
import requests
import json
import pandas as pd
from time import sleep


#%%
## Get all stations, dump into .json-file

entry_p = 'https://opendata-download-metobs.smhi.se'
url     = entry_p + '/api/version/1.0/parameter/1/station-set/all/period/latest-hour/data.json'

## Find all stations, dump file: stationer.json
def get_stations(url):

    r = requests.get(url)

    with open('stationer.json', 'w') as outfile:
        outfile.write(r.text)
    return r

get_stations(url)


#%%
## Load all stations from .json-file

def sort_stations(filename):
    with open('stationer.json', 'r') as infile:
        data = json.load(infile)
        return data

stationer = sort_stations('stationer.json')


#%%
# import requests
temp = 1
wind = 25
parameter = temp
station   = 52350 # Malmö


stad_dict = {
    'hörby':    53530,
    'Hästveda': 63160,
    'Helsingborg': 62040,
    'Halmstad':  62410,
    'Falsterbo': 52230,
    'Karlshamn': 64130,
    'kalmar':    66420,
    'karlskrona': 65090,    
    'Kristianstad': 64030,
    'Ljungby': 63510,
    'Lund':  53430,
    'malmö': 52350,
    'Malmö-Sturup': 53300,
    'Osby':     63220,
    'Perstorp': 11001,
    'Ronneby-Bredåkra': 65160,
    'Växjö': 64510,
}

def get_smhi_csv(name, station_id, parameter):
    endpoint_entry = 'https://opendata-download-metobs.smhi.se/api/'
    
    url_down = endpoint_entry + \
        f'version/1.0/parameter/{parameter}/' + \
        f'station/{station_id}/period/corrected-archive/data.csv'
    
    re = requests.get(url_down)

    with open(f'{name}_{station_id}_{parameter}.csv', 'w') as out:
        out.write(re.text)

for k,v in stad_dict.items():
    print(k, v)
    get_smhi_csv(k, v, parameter)
    sleep(0.4)

get_smhi_csv(parameter, station)

