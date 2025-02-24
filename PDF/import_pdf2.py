import pdfquery
import pandas as pd

pdf = pdfquery.PDFQuery('0435748394_001000CRC#RASF0_20161230_20160012.pdf')
pdf.load()

#convert the pdf to XML
pdf.tree.write('customers.xml', pretty_print = True)
pdf

boekdatum = pdf.pq('LTTextLineHorizontal:contains("Boekdatum")')
lc_boek = float(boekdatum.attr('x0'))
bc_boek = float(boekdatum.attr('y0'))
print (lc_boek,bc_boek)

name = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (27.9, 127.9, 69.0, 667.2)).text()

omschrijving = pdf.pq('LTTextLineHorizontal:contains("Omschrijving")')
bedragaf = pdf.pq('LTTextLineHorizontal:contains("bedragaf")')
bedragbij = pdf.pq('LTTextLineHorizontal:contains("bedragbij")')

print (boekdatum)

print (name)



# access the data using coordinates
startH= 208.2
startB= 508.2
while startH > 160:
    customer_name = pdf.pq(f'LTTextLineHorizontal:in_bbox("87.9, {startH}, 279.9, {startB}")',).text()
    #print (f'box("87.9, {startH}, 279.9, {startB}"')
    print(customer_name)
    startH -= 8.4
    startB -= 8.4


# customer_name = pdf.pq(f'LTTextLineHorizontal:in_bbox("87.9, {startH}, 279.9, {startB}")',).text()
# print(customer_name)
# startH-= 8.4
# startB-= 8.4
# customer_name = pdf.pq(f'LTTextLineHorizontal:in_bbox("87.9, {startH}, 279.9, {startB}")',).text()
# print(customer_name)
# startH-= 8.4
# startB-= 8.4
# customer_name = pdf.pq(f'LTTextLineHorizontal:in_bbox("87.9, {startH}, 279.9, {startB}")',).text()
# print(customer_name)
#output: Brandon James
