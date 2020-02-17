import cv2
import numpy as np

camera = cv2.imread("C:/Users/Admin/Desktop/Project_Image/test photo/720p/IMG_20200217_10.jpg")

car_cascade = cv2.CascadeClassifier('C:/Users/Admin/Desktop/Project_Image/myhaar.xml')

grayvideo = cv2.cvtColor(camera,cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(grayvideo, 1.1, 1)
for (x,y,w,h) in cars:
    cv2.rectangle(camera,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("video",camera)
cv2.waitKey(0)
camera.release()
cv2.destroyAllWindows()