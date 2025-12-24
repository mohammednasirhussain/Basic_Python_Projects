from PIL import Image

img = Image.open("qrcode.png") # Source path with file name
img = img.resize((1800, 1600))
img.save("resizd.png") # Destination path with file name
