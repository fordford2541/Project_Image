import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Admin\Anaconda3\Tesseract-OCR\tesseract.exe"
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread('test photo/raw/IMG_0029.jpg',cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(15,15))
cl1 = clahe.apply(gray)
cl2 = cv2.resize(cl1,(1344,1008))
cv2.imshow('show',cl2)
#gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
#cv2.imshow('image',img)
gray_blur = cv2.GaussianBlur(cl1 ,(3,3),0)
#cv2.imshow('gray',gray)
edged = cv2.Canny(gray_blur, 30, 200) #Perform Edge detection
dilation = cv2.dilate(edged,np.ones((3,3),np.uint8),iterations=1)
erosion = cv2.erode(dilation,np.ones((3,3),np.uint8),iterations=1)

cv2.imshow("edage",cv2.resize(erosion,(1344,1008)))
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
    area = cv2.contourArea(c)
    if area < 10000 or area > 90000:
        continue
    screenCnt = approx
    cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
    x,y,w,h = cv2.boundingRect(c)
    license_img = img[y:y+h,x:x+w]
    license_list.append(license_img)
    #cv2.imshow("License_Detected :",license_img)
    
    counter +=1
    if 0 < x < 1344 and left == 0:
      left += 1
    if 1345 < x < 2688 and center == 0:
      center += 1
    if 2689 < x < 4032 and right == 0:
      right += 1
    result = pytesseract.image_to_string(license_img, lang='tha')
    print(result)
    
#for lic in len(license_list):
if screenCnt is None:
  detected = 0
  print ("No contour detected")
else:
  detected = 1
if left is not None:
  print(left)
  #cv2.imshow('left',license_list[0])
if center is not None:
  print(center)
  #cv2.imshow('center',license_list[1])
if right is not None:
  print(right)
  #cv2.imshow('right',license_list[2])
#cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

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

img = cv2.resize(img, (1344,1008) )
cv2.imshow('image',img)
#cv2.imshow('Cropped',Cropped)
#Splt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()