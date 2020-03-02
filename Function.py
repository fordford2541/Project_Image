import cv2
import imutils
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("test photo/1080p/IMG_00 (1).jpg")
gray = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(15,15))
cl1 = clahe.apply(gray)
gray_blur = cv2.GaussianBlur(cl1,(15,15),0)
thresh = cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1)
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(thresh, kernel, iterations=1) 
closing = cv2.morphologyEx(erosion,cv2.MORPH_CLOSE,kernel,iterations=3)
result_img = closing.copy()
cnts = cv2.findContours(result_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
counter = 0
for cnt in cnts:
    area = cv2.contourArea(cnt)
    if area < 5000 or area > 55000:
        continue
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(image,ellipse,(0,255,0),2)
    counter+=1
cv2.putText(image,str(counter),(10,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),2,cv2.LINE_AA)
thresh = cv2.resize(closing,(1344,1008))
cv2.imshow("Show",thresh)
cv2.waitKey(0)