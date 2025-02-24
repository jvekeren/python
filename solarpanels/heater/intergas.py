import json
import http.client

def _lsbmsb(lsb, msb):
    return (lsb + msb*256) / 100.0

def sort_file(infile):
    with open(infile, "r") as f:
        lines = f.readlines()
        
    sorted_lines = sorted(lines,reverse=True)
    with open(infile, "w") as f:
        f.writelines(sorted_lines)

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
                37:  'central heating rf',
                61:  'ERROR'
                    }.get(self.data['displ_code'], f"unknown {self.data['displ_code']}")
    @property
    def burning(self):
        return 'ON' if bool(self.data['IO'] & 8) else 'OFF'
    @property
    def lockout(self):
        return self.data['displ_code'] if bool(self.data['IO'] & 1) else 'OK'
    @property
    def pumping(self):
        return 'ON' if bool(self.data['IO'] & 2) else 'OFF'
    @property
    def tapping(self):
        return 'ON' if bool(self.data['IO'] & 4) else 'OFF'  

def print_summary(heater):
    print("Pressure     %s" % heater.pressure)
    print("Heater temp. %s" % heater.heater_temp)
    print("Tap temp.    %s" % heater.tap_temp)
    print("Display code %s" % heater.display_code)
    print("Room temp.   %s" % heater.room_temp)
    print("Setpoint     %s" % heater.setpoint)
    print("Stpt. ovrd.  %s" % heater.setpoint_override)
    print()
    print("Burning?     %s" % heater.burning)
    print("Pumping?     %s" % heater.pumping)
    print("Tapping?     %s" % heater.tapping)
    print("Error?       %s" % heater.lockout)

def concat_data(heater):
    return f'{heater.pressure:.2f},\
{heater.heater_temp:.2f},\
{heater.tap_temp:.2f},\
{heater.room_temp:.2f},\
{heater.setpoint:.1f},\
{heater.setpoint_override:.1f},\
{heater.display_code},\
{heater.burning},\
{heater.pumping},\
{heater.tapping},\
{heater.lockout}'

def intergas_data(ipaddress):
    #print (ipaddress)
    try:
        conn = http.client.HTTPConnection(ipaddress)
        conn.request('GET', '/data.json?heater=%s&thermostat=0&setpoint=%s' % (0, 0))
        resp = conn.getresponse()
        if resp.status == 200:
            return heater_data(json.loads(resp.read()))
        else:
            return f"HTTP Error: {resp.status} {resp.reason}"
        conn.close()
    except http.client.HTTPException as e:
        return f"An HTTP exception occurred: {str(e)}e"
    
