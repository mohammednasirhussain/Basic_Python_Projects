#pip install python-barcode pillow

#Barcode generation

from barcode import EAN13
from barcode.writer import ImageWriter

code = EAN13("5901234123457", writer = ImageWriter())

filename = code.save("ean13_barcode")



#Method 2
import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):
    code = barcode.get("code128", data, writer=ImageWriter())
    code.save(filename)

generate_barcode("1234567890", "barcode")
