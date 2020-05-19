import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread('test photo/1080p/IMG_1 (1).jpg',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
clahe = cv2.createCLAHE(clipLimit=-1.0, tileGridSize=(15,15))
cl1 = clahe.apply(gray)
gray_blur = cv2.GaussianBlur(gray,(3,3),0)
edged = cv2.Canny(gray_blur, 30, 200) #Perform Edge detection

# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
img_show = img.copy()
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
    if w < 70 or w > 200:
      continue
    if h < 30 or h > 50:
      continue
    cv2.rectangle(img_show, (x,y), (x+w,y+h), (0, 255, 0), 2)
    license_img = img[y:y+h,x:x+w]
    license_show = img[y:y+h,x:x+w]
    license_show = cv2.resize(license_show,(w*4,h*4))
    license_img = cv2.resize(license_img,(w*4,h*4))
    license_img_gray = cv2.cvtColor(license_img,cv2.COLOR_BGR2GRAY)
    license_img_bw = cv2.adaptiveThreshold(license_img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,1)
    license_img_cnts = cv2.findContours(license_img_bw.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    license_img_cnts = imutils.grab_contours(license_img_cnts)
    license_img_cnts = sorted(license_img_cnts, key = cv2.contourArea, reverse = True)[:30]
    license_charecter = []
    for l in license_img_cnts:
      rect = cv2.boundingRect(l)
      x_lic,y_lic,w_lic,h_lic = rect
      area_lic = w_lic * h_lic
      if h_lic > 55 and h_lic < 100 and w_lic > 10 and w_lic < 70:
        cv2.rectangle(license_img, (x_lic, y_lic), (x_lic+w_lic, y_lic+h_lic),(255, 0, 0),1)
        character = license_img[y_lic:y_lic+h_lic,x_lic:x_lic+w_lic]
        license_charecter.append(len(character))
    
    counter +=1
    if 0 < x < 640 and left == 0:
      left += 1
      license_list.append([left,'left',len(license_charecter)])
      cv2.imshow('left',license_img)
    if 641 < x < 1280 and center == 0:
      center += 1
      license_list.append([center,'center',len(license_charecter)])
      cv2.imshow('center',license_img)
    if 1281 < x < 1920 and right == 0:
      right += 1
      license_list.append([right,'right',len(license_charecter)])
      cv2.imshow('right',license_img)
print("License list   :",license_list)
array_car = []
if screenCnt is None:
  detected = 0
  print ("No contour detected")
else:
  detected = 1
if left is not None:
  array_car.append(left)
if center is not None:
  array_car.append(center) 
if right is not None:
  array_car.append(right)
sum_array = array_car[0]+array_car[1]+array_car[2]
print('Car position   :',array_car)
print('Number of cars :',sum_array)


cv2.imshow('image show',img_show)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()