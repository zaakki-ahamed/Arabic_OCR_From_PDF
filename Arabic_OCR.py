import os
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from PyPDF2 import PdfWriter, PdfReader
import io

# Path to the input PDF file. Modify at as needed
filePath = '/content/i5.pdf'

# Convert PDF to images
doc = convert_from_path(filePath)

# Extract file information
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)

# Set Tesseract OCR command path
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Initialize PDF writer
pdf_writer = PdfWriter()

# List to store OCR text for each page
ocr_text_list = []

# Iterate through each page in the PDF
for page_number, page_data in enumerate(doc):
    print("Processing page number - ", page_number)

    # Perform OCR for Arabic language
    arabic_text = pytesseract.image_to_string(page_data, lang="ara")
    arabic_text = arabic_text.replace("\n", " ")
    ocr_text_list.append(arabic_text)

    # Get a searchable PDF from the OCR result
    pdf = pytesseract.image_to_pdf_or_hocr(page_data, extension='pdf', lang="ara")

    # Append the page to the output PDF
    page = PdfReader(io.BytesIO(pdf)).pages[0]
    pdf_writer.add_page(page)

# Write the combined PDF to a file
output_pdf_path = '{}_OCR_combined.pdf'.format(fileBaseName)
with open(output_pdf_path, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

# Write the extracted OCR text to a text file
output_text_path = '{}_Arabic.txt'.format(fileBaseName)
with open(output_text_path, 'w', encoding='utf-8') as output_text_file:
    for page_number, arabic_text in enumerate(ocr_text_list):
        output_text_file.write(f"Page {page_number + 1}:\n{arabic_text}\n\n")

# Print output file paths
print(f"Combined PDF saved at: {output_pdf_path}")
print(f"Translated text saved at: {output_text_path}")