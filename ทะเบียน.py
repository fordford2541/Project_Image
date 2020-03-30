import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\Anaconda3\Tesseract-OCR\tesseract.exe"
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread('test photo/1080p/IMG_1 (14).jpg',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
clahe = cv2.createCLAHE(clipLimit=-1.0, tileGridSize=(15,15))
cl1 = clahe.apply(gray)
#cv2.imshow('show',cl1)
#gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
#cv2.imshow('image',img)
gray_blur = cv2.GaussianBlur(gray,(3,3),0)
#cv2.imshow('gray',gray_blur)
edged = cv2.Canny(gray_blur, 30, 200) #Perform Edge detection

#cv2.imshow("edage",edged)
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
    
    x,y,w,h = cv2.boundingRect(c)
    area = w*h
    #print(x,y,w,h)
    if w < 70 or w > 100:
      continue
    if h < 30 or h > 50:
      continue
    if area < 2300 or area > 3500:
      continue
    #cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 1)
    #print(w*h)
    license_img = img[y:y+h,x:x+w]
    license_img = cv2.resize(license_img,(w*4,h*4))
    license_img_gray = cv2.cvtColor(license_img,cv2.COLOR_BGR2GRAY)
    license_img_bw = cv2.adaptiveThreshold(license_img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,1)
    #kernel = np.ones((3,3),np.uint8)
    #license_img_dilation = cv2.erode(license_img_bw, kernel, iterations=1)
    license_img_cnts = cv2.findContours(license_img_bw.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    license_img_cnts = imutils.grab_contours(license_img_cnts)
    license_img_cnts = sorted(license_img_cnts, key = cv2.contourArea, reverse = True)[:30]
    cv2.imshow('license_bw',license_img_bw)
    license_charecter = []
    for l in license_img_cnts:
      rect = cv2.boundingRect(l)
      x_lic,y_lic,w_lic,h_lic = rect
      area_lic = w_lic * h_lic
      if h_lic > 55 and h_lic < 300 and w_lic > 10 and w_lic < 100:
        cv2.rectangle(license_img, (x_lic, y_lic), (x_lic+w_lic, y_lic+h_lic),(255, 0, 0),1)
        character = license_img[y_lic:y_lic+h_lic,x_lic:x_lic+w_lic]
        #result = pytesseract.image_to_string(character, lang='tha')
        #if result is not None:
          #print(result)
        license_charecter.append(len(character))
        cv2.imshow('cha',character)
        cv2.imshow('license',license_img)
    
    counter +=1
    if 0 < x < 640 and left == 0:
      left += 1
      license_list.append([left,license_charecter])
    if 641 < x < 1280 and center == 0:
      center += 1
      license_list.append([center,license_charecter])
    if 1281 < x < 1920 and right == 0:
      right += 1
      license_list.append([right,license_charecter])
    #result = pytesseract.image_to_string(license_img, lang='tha')
    #cv2.imshow('result',result)
    #print(result)
print("license :",license_list)
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