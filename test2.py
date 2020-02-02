import cv2

carCascade = cv2.CascadeClassifier('myhaar.xml')

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
    coords=[]
    print(coords)
    for(x,y,w,h) in features:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
    return img

def detect(img,carCascade):
    img = draw_boundary(img,carCascade,1.1,10,(255,0,0),'car')
    return img

img = cv2.imread('IMG_0032.jpg')


image2 = detect(img,carCascade)
image2 = cv2.resize(image2,(1600,1200))
cv2.imshow('image',image2)

cv2.waitKey() 