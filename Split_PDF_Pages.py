from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("merged.pdf") # Source path with file name

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as f:
        writer.write(f)
