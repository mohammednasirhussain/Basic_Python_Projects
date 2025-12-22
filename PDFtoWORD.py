#pip install pdf2docx module

from pdf2docx import Converter
pdf_file = 'Path for PDF file'
docx_file = 'Path for Word file'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()