from datetime import *
import os
import time
import sys

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'intergas.py'))
sys.path.append(module_path)
from cmpModule import *


today = date.today()
print (today)
yesterday = today - timedelta(days=1)
print (yesterday)

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

start_time = time.time()
procdate='2023-09-25'

compressFile(procdate)

end_time = time.time()
elapsed_time = end_time - start_time
print (f"Elapsed Time: {elapsed_time} seconds")

elapse = f'/mnt/heater/{today}_elapse-time.csv'
with open(elapse,"a") as f:
    elTime = f"Elapsed Time {timestamp}: {elapsed_time} seconds\n"
    f.write(elTime)