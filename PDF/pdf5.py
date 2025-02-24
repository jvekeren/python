import tabula as tb
import pandas as pd
import re

file='0435748394_001000CRC#RASF0_20161230_20160012.pdf'
table = read_pdf(file,pages=2,stream=True)

print (table)


