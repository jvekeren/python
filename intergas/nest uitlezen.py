# nest uitlezen

from nest import Nest

napi = Nest('jvekeren@gmail.com', 'jhnadlj02')

print (napi.thermostats)

target = napi.devices[0].target
print('Target (F): ' + str(nest.utils.c_to_f(target)))

for structure in napi.structures:
    for device in structure.devices:
        if device.device_type == 'thermostat':
            print('Current temperature: {} degrees Celsius'.format(device.temperature))