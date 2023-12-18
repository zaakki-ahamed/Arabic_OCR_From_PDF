# Arabic PDF OCR - Searchable PDF

Perform Optical Character Recognition (OCR) on a scanned PDF file containing Arabic text. I use Tesseract OCR to extract text from each page, generate a searchable PDF, and save the OCR text as a separate text file. Can aid in digitizing Arabic text from PDFs and creating searchable documents.

## Requirements
- pdf2image==1.16.3
- tesseract-ocr==5.0.0-alpha.20210506
- pytesseract @ git+https://github.com/madmaze/pytesseract.git@8463b13fbfdc1b17d33f370354e0cd855a9f82e0
- PyPDF2==3.0.1
- tesseract-ocr-ara==1.1.0
- poppler-utils==21.11.0

## Input / Output
- Input : `filePath` variable points to your input PDF file.
- Output : A new PDF file with searchable text generated from the OCR results and a text file containing the extracted Arabic text for each page.

## Usage
1. Install the required libraries from `requirements.txt`.
2. Modify the `filePath` variable to point to your input PDF file.
3. Set the path to the Tesseract OCR command in the script if needed by modifying the line -
`pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'`
4. Run the script, and the combined PDF and translated text will be saved in the same directory.

**Example:**
```python
# Set the path to the input PDF file
filePath = '/path/to/your/input.pdf'

# Set the path to the Tesseract OCR command
pytesseract.pytesseract.tesseract_cmd = '/path/to/your/tesseract'

# Run the script
python script.py