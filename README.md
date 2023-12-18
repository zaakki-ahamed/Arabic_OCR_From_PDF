# Arabic PDF OCR - Searchable PDF

## Description
This Python script allows you to perform Optical Character Recognition (OCR) on a scanned PDF file containing Arabic text. The script uses Tesseract OCR to extract text from each page, generates a searchable PDF, and also saves the OCR text as a separate text file. It is useful for digitizing Arabic text from PDFs and creating searchable documents.

## Requirements
- pdf2image==1.16.3
- tesseract-ocr==5.0.0-alpha.20210506
- pytesseract @ git+https://github.com/madmaze/pytesseract.git@8463b13fbfdc1b17d33f370354e0cd855a9f82e0
- PyPDF2==3.0.1
- tesseract-ocr-ara==1.1.0
- poppler-utils==21.11.0
  
## Note
Before running the script, make sure to set the path to the Tesseract OCR command in the script. Locate the following line:

`pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'`

and modify the path according to the setup of your machine.

## Input
- `filePath`: Path to the input PDF file. Modify this variable to point to your input PDF file.

## Output
- PDF File: A new PDF file with searchable text generated from the OCR results.
- Text file: A text file containing the extracted Arabic text for each page.

## Usage
1. Install the required libraries from `requirements.txt`.
2. Modify the `filePath` variable to point to your input PDF file.
3. Set the path to the Tesseract OCR command in the script if needed.
4. Run the script, and the combined PDF and translated text will be saved in the same directory.

**Example:**
```python
# Set the path to the input PDF file
filePath = '/path/to/your/input.pdf'

# Run the script
python script.py