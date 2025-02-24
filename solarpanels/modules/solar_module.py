import os

import json
import requests
from datetime import datetime as dt

def solar_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # De inhoud van de webpagina is opgeslagen in de 'text'-eigenschap van het response-object
            return subtract_solar(response.text)
        else:
            return f"Fout bij het ophalen van de webpagina. Statuscode: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def subtract_solar(inp):
    if inp[:11] == 'var version':
        inp=inp.split(',')
        soldata = inp[4:10]
        soldata = [int(x) for x in soldata if x]
        dum = soldata.pop(3) 
        soldata[2]/=100
        result=''
        for item in soldata:
            result = result + str(item) + ','
        result=result[:-1]
        return result
    else:
        return 

def add2file(deb):
    file = pad + '/' + today + '_solar.log'
    if os.path.exists(file):
        with open (file, 'r') as f:
            lines = f.readlines()
        lines.insert(0,deb + '\n')
    else:
        lines =deb
    with open (file, 'w') as f:
        f.writelines(lines)


def getSunrise(sunrise,config):
    if not os.path.exists(config):
        found = False
        with open (sunrise, 'r') as f:
            for line in f:
                if today in line:
                    found = True
                    break
        tmp=line.split(',')
        zonop = tmp[4]
        zononder = tmp[5]
        with open (config, 'w') as f:
            f.write(f'zonop={zonop}\n')
            f.write(f'zononder={zononder}\n')
    else:
        with open (config, 'r') as f:
            lines = f.readlines()
        zonop = lines[0].replace('\n', '').split('=')[1]
        zononder = lines[1].replace('\n', '').split('=')[1]
    return [zonop,zononder]

    


