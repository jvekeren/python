import sys
import os
from datetime import *

#import argparse

# Add the parent directory of my_module to sys.path
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'intergas.py'))
sys.path.append(module_path)
from intergas import *
from cmpModule import *

# Your code here...
ip='192.168.1.128'
heater=intergas_data(ip)

if not isinstance(heater,heater_data):
    print(heater)
    sys.exit()

#print_summary (heater)

today = date.today()
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")


outfile = f'/mnt/heater/{today}_intergas.csv'
#print (outfile)
if not os.path.exists(outfile):
    fstLine=f"Date,Pressure,Heater temp.,Tap temp.,Room temp.,Setpoint,Stpt. ovrd.,Display code,Burning?,Pumping?,Tapping?,Error?"
    with open(outfile, 'w') as f:
        f.write(fstLine + '\n')
        f.close()

with open(outfile, "r") as f:
    lines = f.readlines()
lines.insert(1,timestamp + ',' + concat_data(heater) + '\n')
with open(outfile, "w") as f:
    f.writelines(lines)

start_time = time.time()

compressFile(today)

end_time = time.time()
elapsed_time = end_time - start_time

#elapse = f'/mnt/heater/{today}_elapse-time.csv'
#with open(elapse,"a") as f:
#    elTime = f"Elapsed Time {timestamp}: {elapsed_time} seconds\n"
#    f.write(elTime)
#print (f"Elapsed Time: {elapsed_time} seconds")