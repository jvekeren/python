from datetime import *
import time
import sys
import os

def nroflinesinfile(inp):
    nrlines = -1
    if os.path.exists(inp):
        nrlines+=1
        with open(inp,'r') as file:
            for line in file:
                nrlines+=1
    return nrlines

def updateCompressedFile(inInp,cmpInp):
    try:
        lstfnd = inInp.index(cmpInp[1])-1
    except ValueError:
        lstfnd=-1
        return "er ging iets mis"
    if lstfnd == 1: return "geen nieuwe data"
    
    nrH1=len(inInp)
    #print (nrH1,lstfnd)
    
    while True:
        H1Stat=inInp[lstfnd].split(",")
        cmpStat=cmpInp[1].split(",")
        if H1Stat[7] == cmpStat[7]:
            if len(cmpInp) == 2:
                cmpInp.insert(1,inInp[lstfnd])
            else:
                cmpPrev=cmpInp[2].split(',')
                if H1Stat[7] == cmpPrev[7]:
                    cmpInp[1]=inInp[lstfnd]
                else:
                    cmpInp.insert(1,inInp[lstfnd])
        else:
            cmpInp.insert(1,inInp[lstfnd])
        lstfnd-=1
        if lstfnd == 1: break
    return "gevonden"

def compressFile(procDay):
#today = date.today()
#today = '2023-09-21'

    infile = f'/mnt/heater/{procDay}_intergas.csv'
    cmpfile = f'/mnt/heater/{procDay}_intergas.cmp'

    with open(infile, "r") as f:
        Inlines = f.readlines()
        
    nrlinescmp = nroflinesinfile(cmpfile)
    if nrlinescmp <= 0:
        with open(cmpfile, "w") as f:
            f.write(Inlines[0])
            f.write(Inlines[-1])

    with open(cmpfile, "r") as f:
        cmpLines = f.readlines()
    cmpStat = updateCompressedFile(Inlines,cmpLines)
    if cmpStat == "gevonden":
        with open(cmpfile, "w") as f:
            f.writelines(cmpLines)

procdate=date.today()
#print (procdate)
start_time = time.time()
procdate='2023-09-22'

compressFile(procdate)

end_time = time.time()
elapsed_time = end_time - start_time
#print (f"Elapsed Time: {elapsed_time} seconds")