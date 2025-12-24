#Barcode generation

from barcode import EAN13
from barcode.writer import ImageWriter

code = EAN13("5901234123457", writer = ImageWriter())
filename = code.save("ean13_barcode")