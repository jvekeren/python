class MyClass:
    # Class attributes
    class_variable = 10
    
    # Constructor (__init__ method)
    def __init__(self,data,pressure,heater_tmp,tap_tmp,display_code):
        self.data = data
        self.pressure = pressure
        self.heater_tmp = heater_tmp
        self.tap_tmp = tap_tmp
        self.display_code = display_code
    
    # Instance methods
    def method1(self):
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
                    }.get(self.data['display_code'], 'unknown')
    
    def method2(self, value):
        self.tap_tmp = value

# Creating instances of the class
obj1 = MyClass(15,1, 2, 3, 15)
obj2 = MyClass(25,10, 15, 20, 126)

# Accessing attributes and methods
print(obj1.display_code)  # Output: 5
print(obj1.method1())   # Output: 20
print(obj2.method1())   # Output: standby

obj1.method2(25)
print(obj1.tap_tmp)  # Output: 25
