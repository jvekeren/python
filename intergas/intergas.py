import json
import sys
import http.client
from  datetime import *
import argparse

def _lsbmsb(lsb, msb):
    return f"{((lsb + msb*256) / 100.0):.2f}"

class heater_data:
    def __init__(self, data):
        self.data=data
    @property
    def pressure(self):
        return _lsbmsb(self.data['ch_pressure_lsb'],
                    self.data['ch_pressure_msb'])
    @property
    def heater_temp(self):
        return _lsbmsb(self.data['ch_temp_lsb'],
                    self.data['ch_temp_msb'])
    @property
    def tap_temp(self):
        return _lsbmsb(self.data['tap_temp_lsb'],
                    self.data['tap_temp_msb'])
    @property
    def room_temp(self):
        return _lsbmsb(self.data['room_temp_1_lsb'],
                    self.data['room_temp_1_msb'])
    @property
    def setpoint(self):
        return _lsbmsb(self.data['room_temp_set_1_lsb'],
                    self.data['room_temp_set_1_msb'])
    @property
    def setpoint_override(self):
        return _lsbmsb(self.data['room_set_ovr_1_lsb'],
                    self.data['room_set_ovr_1_msb'])
    @property
    def display_code(self):
        return {85:  'sensortest',
                170: 'service',
                204: 'tapwater',
                51:  'tapwater int.',
                240: 'boiler int.',
                15:  'boiler ext.',
                153: 'postrun boiler',
                102: 'central heating',
                0:   'opentherm',
                255: 'buffer',
                24:  'frost',
                231: 'postrun ch',
                126: 'standby',
                37:  'central heating rf'
                    }.get(self.data['displ_code'], 'unknown')
    @property
    def burning(self):
        return 'ON' if bool(self.data['IO'] & 8) else 'OFF'
    @property
    def lockout(self):
        return 'ON' if bool(self.data['IO'] & 1) else 'OFF'
    @property
    def pumping(self):
        return 'ON' if bool(self.data['IO'] & 2) else 'OFF'
    @property
    def tapping(self):
        return 'ON' if bool(self.data['IO'] & 4) else 'OFF'  

def print_summary(inp):
        print("Pressure     %s" % inp.pressure)
        print("Heater temp. %s" % inp.heater_temp)
        print("Tap temp.    %s" % inp.tap_temp)
        print("Display code %s" % inp.display_code)
        print("Room temp.   %s" % inp.room_temp)
        print("Setpoint     %s" % inp.setpoint)
        print("Stpt. ovrd.  %s" % inp.setpoint_override)
        print()
        print("Burning?     %s" % inp.burning)
        print("Pumping?     %s" % inp.pumping)
        print("Tapping?     %s" % inp.tapping)
        print("Error?       %s" % inp.lockout)
    
def intergas_data():
    try:
        conn = http.client.HTTPConnection("192.168.1.128")
        conn.request('GET', '/data.json?heater=%s&thermostat=0&setpoint=%s' % (0, 0))
        resp = conn.getresponse()
        if resp.status == 200:
            h=heater_data(json.loads(resp.read()))
        else:
            h=f"HTTP Error: {resp.status} {resp.reason}"
        conn.close()
    except http.client.HTTPException as e:
        print("An HTTP exception occurred:", e)
    return h

def concat_data(heater):
    return f'{heater.pressure},\
{heater.heater_temp},\
{heater.tap_temp},\
{heater.room_temp},\
{heater.setpoint},\
{heater.setpoint_override},\
{heater.display_code},\
{heater.burning},\
{heater.pumping},\
{heater.tapping},\
{heater.lockout}'

today=date.today()
now=datetime.now()
timestamp=now.strftime("%Y-%m-%d %H:%M:%S")

heater=intergas_data()

if not isinstance(heater,heater_data):
    print(heater)
    sys.exit()

print (timestamp +',' + concat_data(heater) + '\n')