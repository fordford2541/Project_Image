import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\Anaconda3\Tesseract-OCR\tesseract.exe"
import matplotlib.pyplot as plt

def conventImage(Image):
    gray = cv2.cvtColor(Image,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(3,3),0)
    canny = cv2.Canny(blur,100,200)
    #canny = cv2.morphologyEx(canny,cv2.MORPH_OPEN,(3,3))
    #canny = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,(3,3))
    #canny = cv2.dilate(canny,(3,3),iterations = 1)
    #canny = cv2.erode(canny,(3,3),iterations = 1)
    #canny = cv2.Laplacian(canny,cv2.CV_64FC4)
    return canny

img = cv2.imread("test photo/raw/IMG_0029.jpg")
img = cv2.resize(img,(1344,1008))
#img = img[1512:2016,1344:2688]
#cv2.imshow('show',img)
processed_img = conventImage(img)
original_img = img.copy()

contour_img = processed_img.copy()

im, contours, hierarchy = cv2.findContours(contour_img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
contours = sorted(contours,key=cv2.contourArea,reverse=True)[:50]

for contour in contours:
    p = cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,0.2*p,True)
    
    if len(approx) == 4:
        x,y,w,h = cv2.boundingRect(contour)
        license_img = original_img[y:y+h,x:x+w]
        area = cv2.contourArea(contour)
        #print(x,y,w,h)
        if area < 2220 or area > 30000:
            continue
        cv2.imshow("License_Detected :",license_img)
        cv2.drawContours(img,contours,-1,(0,0,255),2)
        gray_license = cv2.cvtColor(license_img,cv2.COLOR_BGR2GRAY)
        th_license = cv2.adaptiveThreshold(gray_license,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
        result = pytesseract.image_to_string(license_img, lang='tha')
        print(result)

cv2.imshow("test",processed_img)
cv2.imshow("Image",img)
cv2.waitKey(0)

