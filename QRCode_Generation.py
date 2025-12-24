#pip install qrcode

import qrcode

img = qrcode.make("https://example.com") # URL to generate the QR code
img.save("qrcode.png") # path to save the QR code
