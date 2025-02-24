import os
import sys
from datetime import datetime as dt
import platform

config_path = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.dirname(os.path.abspath(__file__)) + '/modules'
if not module_path in sys.path: sys.path.append(module_path)
import solar_module as sol
import config_module as cfg

cwd = os.getcwd()


if platform.system() == 'Windows':
    configlfd = cwd + '\\solarpanels\\'
    solfld = cwd + '\\solarpanels\\solar\\'
    sunfld = cwd + '\\solarpanels\\data\\'
    lanfld = cwd + '\\solarpanels\\data\\'
    debugfld = cwd + '\\solarpanels\\data\\'
else:
    configlfd =  "/mnt/solar/"
    solfld = "/mnt/solar/"
    lanfld = '/home/johan/'
    sunfld = '/home/johan/bin/refdata/'
    debugfld = '/tmp/'

solfolder = cfg.solfld

timestamp = dt.now().strftime('%Y-%m-%d %H:%M:%S')
year = timestamp[:4]
today = timestamp[:10]
time = timestamp[11:]
debug = True

sunrise = datafld + 'sunrissunsetComp.csv'
solfile = solfld + today + '-solar.csv'
sumfile = solfld + year + '-solar.csv'
zipfile = solfld + year + '-solar.zip'
debugfile = datafld + 'debug-solar.txt'
config = config_path + '/' + today + '-config'
lanhosts = lanfld + '.lanhostnames'

print (cfg.datafld)

zon = cfg.getSunrise(today,sunrise)
zonop = zon[0]
zononder = zon[1]

if debug: cfg.debugprint ('solfile',solfile)
if debug: cfg.debugprint ('sumfile',sumfile)
if debug: cfg.debugprint ('zipfile',zipfile)
if debug: cfg.debugprint ('sunrise',sunrise)
if debug: cfg.debugprint ('timestamp',timestamp)
if debug: cfg.debugprint ('today',today)
if debug: cfg.debugprint ('time',time)
if debug: cfg.debugprint ('zonop',zonop)
if debug: cfg.debugprint ('zononder',zononder)
if debug: cfg.debugprint ('IP address',', '.join(cfg.getNetaddress('solar')))




IP = cfg.getNetaddress(lanhosts,'solar')[0]
url = 'http://'+IP + '/js/status.js'
if debug: cfg.debugprint ('url',url)
solar=cfg.networkUP(url)
if debug: cfg.debugprint ('solar response',solar)

