from PyPDF2 import PdfReader

reader = PdfReader("input.pdf") # Source path with file name
text = ""

for page in reader.pages:
    text += page.extract_text()

print(text)
