import pypdf
from tabula import read_pdf
file='0435748394_001000CRC#RASF0_20161230_20160012.pdf'

# Get the number of pages in the file
pdf_reader = pypdf.PdfReader(file)
n_pages = len(pdf_reader.pages)

# For each page the table can be read with the following code
table_pdf = read_pdf(
    pdf_file,
    guess=False,
    pages=1,
    stream=True,
    encoding="utf-8",
    area=(96, 24, 558, 750),
    columns=(24, 127, 220, 274, 298, 325, 343, 364, 459, 545, 591, 748),
)
print table_pdf