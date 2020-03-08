import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\Anaconda3\Tesseract-OCR\tesseract.exe"
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread('test photo/1080p/IMG_1 (14).jpg',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(15,15))
cl1 = clahe.apply(gray)
#cv2.imshow('show',cl1)
#gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
#cv2.imshow('image',img)
gray_blur = cv2.GaussianBlur(gray ,(3,3),0)
#cv2.imshow('gray',gray)
edged = cv2.Canny(gray_blur, 30, 200) #Perform Edge detection

cv2.imshow("edage",edged)
# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
screenCnt = None
counter = 0
left = 0
center = 0
right = 0
license_list = []
# loop over our contours
for c in cnts:
  # approximate the contour
  peri = cv2.arcLength(c, True)
  approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
 # if our approximated contour has four points, then
 # we can assume that we have found our screen
  if len(approx) == 4:
    
    screenCnt = approx
    cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
    x,y,w,h = cv2.boundingRect(c)
    area = w*h
    if area < 2300 or area > 3500:
        continue
    print(w*h)
    license_img = img[y:y+h,x:x+w]
    license_img_gray = cv2.cvtColor(license_img,cv2.COLOR_BGR2GRAY)
    license_img_bw = cv2.adaptiveThreshold(license_img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,1)
    license_list.append(license_img_bw)
    #cv2.imshow("License_Detected :",license_img)
    
    counter +=1
    if 0 < x < 640 and left == 0:
      left += 1
    if 641 < x < 1280 and center == 0:
      center += 1
    if 1281 < x < 1920 and right == 0:
      right += 1
    #result = pytesseract.image_to_string(license_img, lang='tha')
    #print(result)
print("license :",len(license_list))
#for lic in len(license_list):
aray_car = []
if screenCnt is None:
  detected = 0
  print ("No contour detected")
else:
  detected = 1
if left is not None:
  aray_car.append(left)
  #cv2.imshow('left',license_list[0])
if center is not None:
  aray_car.append(center) 
  #cv2.imshow('center',license_list[1])
if right is not None:
  aray_car.append(right)  
  #cv2.imshow('right',license_list[2])
#cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
print(aray_car)
a = 0
#for l in license_list[0]:
  #l = l % 254
  #a += l
#print(a)
#print(license_list[0])
#cv2.imshow('list0',license_list[0])
#plt.plot(a)
#plt.show()
# Masking the part other than the number plate
#mask = np.zeros(gray.shape,np.uint8)
#new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
#new_image = cv2.bitwise_and(img,img,mask=mask)

# Now crop
#(x, y) = np.where(mask == 255)
#(topx, topy) = (np.min(x), np.min(y))
#(bottomx, bottomy) = (np.max(x), np.max(y))
#Cropped = gray[topx:bottomx+1, topy:bottomy+1]

#Read the number plate
#text = pytesseract.image_to_string(Cropped)
#print("Detected Number is:",text)

cv2.imshow('image',img)
#cv2.imshow('Cropped',Cropped)
#Splt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()