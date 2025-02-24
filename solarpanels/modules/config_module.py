import sys
import os
import requests
import netifaces
from datetime import datetime as dt


IP = "192.168.1.166"
def modify_IP(inp):
    global IP
    IP = inp

def modify_solfld(inp):
    global solfld
    solfld = inp
lanhosts = '/home/johan/.lanhostnames'
def modify_lanhosts(inp):
    global lanhosts
    lanhosts = inp

datafld = '/home/johan/'
def modify_datafld(inp):
    global datafld
    datafld = inp

def debugprint(txt1,txt2):
    timestamp=dt.now().strftime('%Y-%m-%d %H:%M:%S')
    today = timestamp[:10]
    debugfile= solfld + today + '-debug.txt'
    debugtxt = timestamp + ',' + txt1 + ' = ' + txt2

    if os.path.exists(debugfile):
        with open(debugfile,'r') as file:
            lines = file.readlines()
    with open(debugfile,'w') as file:
        eol = '' if debugtxt[-1] == '\n' else '\n'
        file.write(debugtxt + eol)
    with open(debugfile,'a') as file:
        file.writelines(lines)

def getSunrise(today, sunrise):
    with open (sunrise, 'r') as f:
        for line in f:
            if today in line:
                found = True
                break
    tmp=line.split(',')
    zonop = tmp[4]
    zononder = tmp[5]
    return [zonop,zononder]

def networkUP(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # De inhoud van de webpagina is opgeslagen in de 'text'-eigenschap van het response-object
#            return subtract_solar(response.text)
            return response.text
        else:
            return f"Fout bij het ophalen van de webpagina. Statuscode: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def getNetaddress(lanhosts,tool):
    lan = os.getcwd()

    with open (lanhosts, 'r') as f:
        for line in f:
            if tool.lower() in line.lower():
                found = True
                break
    tmp = line.split('\t')
    return tmp


os.