import cv2
import numpy as np
import tesserorc as tr
from tesserocr import PyTessBaseAPI
from PIL import Image
import pytesseract 

img = Image.open('test photo/1080p/IMG_1 (14).jpg','r')
cv_img = cv2.imread('test photo/1080p/IMG_1 (14).jpg')

pil_img = Image.fromarray(cv2.cvtColor(cv_img,cv2.COLOR_BGR2RGB))

# print(pil_img)
  #initialize app
api = tr.PyTessBaseAPI()
try:
    api.SetImage(pil_img)
    boxes = api.GetComponentImages(tr.RIL.WORD,True) #point each word(แบ่งเป็นคำๆ)
    # get text
    img_2_text = pytesseract.image_to_string(img)#change img to string (เปลี่ยนจากรูปเป็นตัวหนังสือ)
    ass = img_2_text.split()
    for line in ass: #cut '‘'(ตัดตัวหนังสือจาก array ข้อมูลที่ได้มา)
        if(line == '‘'):
            ass.remove('‘')
    
    font= cv2.FONT_HERSHEY_SIMPLEX #font charecter (เป็นตัวบอกว่าจะใช้ ฟอนต์ อะไร)
    for i,(im,box,_,_) in enumerate (boxes): #loop
      x,y,w,h = box['x'],box['y'],box['w'],box['h']
      cv2.putText(cv_img,ass[i], (x-3,y-3), font,0.5,(0,0,255),1, cv2.LINE_AA) #echo position font of img (บอกว่าตัวอักษรจะมีสีอะไรและอยู่ที่ตำแหน่งไหนของรูป)
      cv2.rectangle(cv_img, (x,y), (x+w,y+h), color=(0,255,0))#Create rectangle of img (สร้างสี่เหลี่ยมให้กับรูปที่ตรวจจับได้)
finally:
    api.End()

print(ass)
cv2.imshow('output', cv_img) #show img
cv2.imwrite('/Users/lelalomos/Desktop/train/AI/translate/test.jpg',cv_img,) #Save image
print('Save Suscess')
cv2.waitKey(0)
cv2.destroyAllWindows()