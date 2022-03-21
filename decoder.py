import cv2
# read the QRCODE image
img = cv2.imread("myCode.png")
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)
print("QRCode Data: ", data)
