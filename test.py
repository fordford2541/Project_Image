from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\Anaconda3\Tesseract-OCR\tesseract.exe"
import cv2
img = cv2.imread('thai.png')
#img = Image.open('thai.png')
result = pytesseract.image_to_string(img, lang='tha')
print(result)