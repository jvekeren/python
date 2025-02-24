import random
import subprocess

def getInternetStatusByDnsServers(hostname):
    try:
        p = subprocess.Popen(["ping","-n","1", hostname], stdout=subprocess.PIPE).stdout.read()
        items= str(p).split(" ")
        for item in items:
            print (item)
            if "(100%" in item:
                print (hostname + ' not found')
                return False,'0.0.0.0'
        ip=items[2][1:-1]
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        return False
    return True,ip

domain= "jvekeren.synology.me"
if  getInternetStatusByDnsServers(domain)[0]:
    print (domain +' = ' + getInternetStatusByDnsServers(domain)[1] + ' found')
else:
    print (domain + ' not found')
           