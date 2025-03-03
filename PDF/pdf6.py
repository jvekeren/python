
import sys
#print(sys.executable)
#sys.exit()

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""
    
    # Iterate through each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text("text")
    
    return text

def print_text_in_columns(text, num_columns=3):
    lines = text.split('\n')
    max_lines = len(lines)
    column_height = max_lines // num_columns + (max_lines % num_columns > 0)
    
    columns = [lines[i * column_height:(i + 1) * column_height] for i in range(num_columns)]
    
    for row in zip(*columns):
        print(" | ".join(row))

if __name__ == "__main__":
    pdf_path = "pdf\\0435748394_001000CRC#RASF0_20161230_20160012.pdf"  # Replace with your PDF file path
    text = extract_text_from_pdf(pdf_path)
    print_text_in_columns(text)
    open('pdf\\pdf6.txt', 'w').write(text)