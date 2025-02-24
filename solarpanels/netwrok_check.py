import random
import os
import socket
import subprocess
 
def getInternetStatusByDnsServers():
    r = '1'
    li = ["8.8.8.8",\
    "8.8.4.4",\
    "209.244.0.3",\
    "209.244.0.4",\
    "208.67.222.222",\
    "37.235.1.174",\
    "91.239.100.100"\
    ]
 
    random.shuffle(li)
    for i in range(len(li)):
       try :
           hostname = li[i]
           p = subprocess.Popen(["/bin/ping", "-c1", "-W1", hostname], stdout=subprocess.PIPE).stdout.read()
           for item in str(p).split("\n"):
               if "0% packet loss" in item:
                   return '1'
        except Exception as inst:
            print(type(inst))
            print(inst.args)
            print(inst)
    return r