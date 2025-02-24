import sys
import os
#import argparse

# Add the parent directory of my_module to sys.path
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'intergas.py'))
sys.path.append(module_path)
from intergas import *

# Your code here...
ip='192.168.1.128'
h=intergas_data(ip)

if not isinstance(h,heater_data):
    print(h)
    sys.exit()

print_summary (h)