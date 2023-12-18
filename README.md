# Arabic PDF OCR - Searchable PDF

## Description
This Python script allows you to perform Optical Character Recognition (OCR) on a PDF file containing Arabic text. The script uses Tesseract OCR to extract text from each page, generates a searchable PDF, and also saves the OCR text as a separate text file. It is useful for digitizing Arabic text from PDFs and creating searchable documents.

## Requirements
- pdf2image
- tesseract-ocr
- pytesseract
- PyPDF2
- tesseract-ocr-ara
- poppler-utils

## Input
- `filePath`: Path to the input PDF file. Modify this variable to point to your input PDF file.

## Output
- Combined PDF: A new PDF file with searchable text generated from the OCR results.
- Translated Text: A text file containing the extracted Arabic text for each page.

## Usage
1. Install the required libraries using the provided commands.
2. Modify the `filePath` variable to point to your input PDF file.
3. Run the script, and the combined PDF and translated text will be saved in the same directory.

**Example:**
```python
# Set the path to the input PDF file
filePath = '/path/to/your/input.pdf'

# Run the script
python script.py