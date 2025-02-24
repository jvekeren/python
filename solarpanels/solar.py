import os
import sys
import datetime as dt

#module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules'))
scrptpath = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.dirname(os.path.abspath(__file__)) + '/modules'
if not module_path in sys.path: sys.path.append(module_path)

import solar_module as sol

sol.init(scrptpath)

print (sol.today)
print (sol.time)
print (sol.timestamp)
print (sol.zonop)
print (sol.zononder)

print (sol.solfile)
print (sol.zipfile)
print (sol.sunrise)
print (sol.config)

print (f'{sol.time},{sol.solar_data(sol.url)}')

sys.exit()



txt = sol.timestamp + ',' + 'eerst fout regel'
sol.add2file(txt)

sys.exit()




response = sol.solar_data(sol.url)
print (response)
if type(response) == list:
    if len(response) == 0:
        sol.add2logfile(response)

sol.add2logfile('eerst fout regel')
