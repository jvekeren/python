from datetime import *
import sys
import os

def select_only_at_the_hour (f2,outfile):
    with open(outfile, "w") as f2:
        for line in lines:
            tmp = line[11:19]
            mn = tmp[6:7]
            if mn == '0':
                f2.write(line)

def debug_file(lines):
    nrLines=len(lines)-1
    t1=t2=0

    for i in range(2,nrLines):
        l1=lines[i][20:]
        l2=lines[i+1][20:]
        if l1 != l2:
            t1=t1+1
            print (l1)
            print (l2)
        else:
            t2=t2+1
            print ('hetzelfde',l1)
    print (t1,t2)


today = date.today()
yesterday = today - timedelta(days=1)

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

cmpfile = f'/mnt/heater/{today}_intergas.cmp1'

if not os.path.exists(cmpfile):
    with open (cmpfile, "w") as fnew:
        fnew.write("")
        today=yesterday
        print (cmpfile,' bestaat niet')

#today="2023-09-04"
infile = f'/mnt/heater/{today}_intergas.csv'
cmpfile = f'/mnt/heater/{today}_intergas.cmp1'

with open(infile, "r") as f:
    lines = f.readlines()

lines.sort()
lst=len(lines)

# alleen data wegschrijven als de watertemperatuur hoger is dan de
# vorige waarde, dan is de brander aangeweest. Ook wegschrijven als
# er iets aan of uit is gegaan. Dan zou je ook nog vaker kunnen
# uitlezen.

#with open(cmpfile, "r") as fcmp:
#    cmplines=fcmp.readlines()
#cmplst=len(cmplines)
#print (cmplines[cmplst-1])


with open(cmpfile, "w") as f:

    f.write(lines[lst-1])
    f.write(lines[0])
    j=0
    for i in range(0,lst-2):
        l1=lines[i].split(",")
        l2=lines[i+1].split(",")
        if l1[7] != l2[7]:
            if j != i:
                f.write(lines[i])
                j=i
            f.write(lines[i+1])

f.close()
sys.exit()
