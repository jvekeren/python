import sys
import os

addir='C:\\ABI\\python\\modules'
if addir not in sys.path:
    sys.path.append('C:\ABI\python\modules')

import filehandling as fh

cwd = 'C:\ABI\XE-TEST'
os.chdir(cwd)

fh.definepcb()
fh.Modify_global_logfile(fh.pcb)

print fh.pcb
print fh.logfile

print fh.startlogging(fh.logfile)

sys.exit()

#ser_mpr6 = serial.Serial('com4', 9600, timeout=1)

try:
    ser_mpr6 = serial.Serial('com3', 9600, timeout=1)
except:
    print 'port already open'
    
try:
    ser_k1 = serial.Serial('com3', 9600, timeout=1)
except:
    print 'k1 fail'

try:
    ser_k2 = serial.Serial('com5', 9600, timeout=1)
except:
        print 'k2 fail' 

sys.exit()
