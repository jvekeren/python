from pdfquery  import PDFQuery

# Create a PDFQuery object and open the PDF file
pdf = PDFQuery('0435748394_001000CRC#RASF0_20161230_20160012.pdf')

# Load the PDF content
pdf.load()

# Define the XPath query to select the text you want
# For example, to select all text within the first page, you can use 'page[0]//text()'

#query = 'page[0]//text()'
text_elements = pdf.pq('LTTextLineHorizontal')

# Execute the query and extract the text
#results = pdf.extract(query)
text = [t.text for t in text_elements]

# Iterate through the extracted text
for line in text:
    print(line)
