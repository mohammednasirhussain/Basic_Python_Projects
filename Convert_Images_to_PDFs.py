
#pip install pillow

from PIL import Image

img = Image.open("ean13_barcode.png") # Source path of image with image name
img.convert("RGB").save("output.pdf") #Destination path to pdf with file name
