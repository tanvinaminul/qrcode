import pyqrcode
from PIL import Image

# generate QR code
text= input("Enter the Text To Make QR Code: ")
qr = pyqrcode.create(text)
qr.png("myCode.png", scale=8)