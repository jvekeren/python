import json
import sys
import http.client
import argparse

def _lsbmsb(lsb, msb):
    return (lsb + msb*256) / 100.0

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
                    self.data['ch_temp_lsb'])
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
            res = json.loads(resp.read())
            h=heater_data(res)
            #node = json.loads(resp.read())['nodenr']
            #print (res)
    #        print (res['nodenr'])
            #print ("Pressure     %s" % _lsbmsb(res['ch_pressure_lsb'],res['ch_pressure_msb']))
            #print ("Heater temp. %s" % _lsbmsb(res['ch_temp_lsb'],res['ch_temp_msb']))
            #print ("Tap temp.    %s" % _lsbmsb(res['tap_temp_lsb'],res['tap_temp_msb']))
            #print ("Display code %s" % res['displ_code'])
            #print ("Room temp.   %s" % _lsbmsb(res['room_temp_1_lsb'],res['room_temp_1_msb']))
            #print ("Setpoint     %s" % _lsbmsb(res['room_temp_set_1_lsb'],res['room_temp_set_1_msb']))
            #print ("Stpt. ovrd.  %s" % _lsbmsb(res['room_set_ovr_1_lsb'],res['room_set_ovr_1_msb']))
            #print()
            #print ('burning:','ON' if bool(res['IO'] & 8) else 'OFF')
            #print ('pumping:','ON' if bool(res['IO'] & 2) else 'OFF')
            #print ('tapping:','ON' if bool(res['IO'] & 4) else 'OFF')
            #print ('error:','ON' if bool(res['IO'] & 1) else 'OFF')
        else:
            print (f"HTTP Error: {resp.status} {resp.reason}")
        conn.close()

    except http.client.HTTPException as e:
        print("An HTTP exception occurred:", e)
    return h

h=intergas_data()

print_summary(h)

