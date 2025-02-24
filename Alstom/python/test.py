import serial
import sys
import time

addlib='C:\\ABI\\python\\modules'
if addlib not in sys.path:
	sys.path.append('C:\ABI\python\modules')

import vme
import keithley


serial_port = serial.Serial('com4', 9600, timeout=1)

# word = '0x2aaa'
# byte_response = word.strip()

# byte_as_int = int(byte_response, 16)
# print (byte_as_int)


# sys.exit()
vme.set_base_address(0x0c000000)

full_address = 0x0800
vme.ww(full_address,'AAAA',serial_port)
print vme.rw(full_address,serial_port)

serial_port.close()