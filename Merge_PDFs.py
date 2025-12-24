#pip install PyPDF2

from PyPDF2 import PdfMerger

merger = PdfMerger()
files = ["River_Valley_Maths_Paper_for_Class_4.pdf", "output.pdf"]# ,"3.pdf"] # Source input files

for pdf in files:
    merger.append(pdf)

merger.write("merged_Result.pdf") #Destination path to save merged pdf with file name
merger.close()
