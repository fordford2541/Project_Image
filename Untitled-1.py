import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image

img = cv2.imread('IMG_0026.jpg',cv2.IMREAD_COLOR)



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
#gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
#cv2.imshow('image',img)
gray = cv2.GaussianBlur(gray,(3,3),0)
#cv2.imshow('gray',gray)
edged = cv2.Canny(gray, 30, 200) #Perform Edge detection

# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
counter = 0
# loop over our contours
for c in cnts:
  # approximate the contour
  peri = cv2.arcLength(c, True)
  approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 
 # if our approximated contour has four points, then
 # we can assume that we have found our screen
  if len(approx) == 4:
    area = cv2.contourArea(c)
    if area < 5000 or area > 25000:
      continue
    screenCnt = approx
    cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
    x,y,w,h = cv2.boundingRect(c)
    license_img = img[y:y+h,x:x+w]
    cv2.imshow("License_Detected :",license_img)
    if license_img is None:
      counter +=0
    else:
      counter +=1

if screenCnt is None:
  detected = 0
  print ("No contour detected")
else:
  detected = 1


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
print(counter)

cv2.waitKey(0)
cv2.destroyAllWindows()