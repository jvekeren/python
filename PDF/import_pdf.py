from pdfquery import PDFQuery

pdf = PDFQuery('0435748394_001000CRC#RASF0_20161230_20160012.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)