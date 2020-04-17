import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

#Read Image
I = cv2.imread('C:\\Users\\nior\\Documents\\GitHub\\Project_Image\\Test photo\\1080p\\IMG_1 (19).jpg',cv2.IMREAD_COLOR)
#input = I
I = np.array(I)
#I = cv2.resize(I, (1344,1008))
cv2.imshow('1',I)
#I = cv2.process(input)
#Extract Y Component (Convert an Image to Gray)
Igray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
rows = Igray.shape[0]
cols = Igray.shape[1]
cv2.imshow('2',Igray)
##Dilate and Erode Image in order to remove noise
#############################################################
#Idilate = Igray
#i=1
#j=1
#for i in range (rows):
#    for j in range (cols-1):
#       temp = np.maximum(Igray[i][j-1], Igray[i][j])
#        Idilate[i][j] = np.maximum(temp, Igray[i][j+1])
#        break
#    break
#I = Idilate
#############################################################
kernel = np.ones((3,3),np.uint8)
Idilate = cv2.dilate(Igray,kernel,iterations=1)
I = Idilate
#############################################################
cv2.imshow('3:Dilated',Idilate)
cv2.imshow('4',I)
difference=0
sum=0
total_sum=0
##Process edges in horizontal direction
max_horz=0
maximum=0
horz1 = []
for i in range(cols):
    horz1.append(0)
for i in range(1,cols,1):
    sum = 0
    for j in range(1,rows,1):
        if I[j][i] > I[j-1][i]:
            difference = I[j][i]-I[j-1][i]
        else :
            difference = I[j-1][i]-I[j][i]    
        if difference > 20:
            sum = sum+difference
            
    
    horz1[i] = sum
    #Find peak value
    if sum > maximum:
        max_horz = i
        maximum = sum
    total_sum = total_sum+sum
average = total_sum/cols
##Plot the histogram for analysis

plt.subplot(311)
plt.plot(horz1)
plt.xlabel('column Number ->')
plt.ylabel('Differnce ->')
plt.title('Horizontal Edge Processing Histogram')
##Smoothen the Horizontal Histogram by applying low pass filter
sum = 0
horz = horz1
for i in range(20,cols-20,1):
    sum = 0
    for j in range(i-20,i+20,1):
        sum = sum + horz1[j]
    horz[i] = sum/40
plt.subplot(312)
plt.plot(horz)
plt.xlabel('Row Number ->')
plt.ylabel('Difference ->')
plt.title('Histogram after passing through Low Pass Filter')
plt.subplots_adjust(hspace=1)
plt.show()
##Filter out Horizontal Histogram Values by applying Dynamic Threshold
#print("Filter out Horizontal Histogram")
#for i in range(1,cols,1):
#    if horz[i]<average:
#        horz[i] =0
#        for j in range(1,rows,1):
#            I[j][i]=0
#            break
#        break
#    break
#plt.subplot(313)
#plt.plot(horz)
#plt.xlabel('Column Number ->')
#plt.ylabel('Differnce ->')
#plt.title('Histogram after Filtering')
#plt.show()
##Process edges in Vertical Direction
difference=0
total_sum=0
print('Processing Edges Vertically...')
maximum=0
max_vert =0
vertl = []
for i in range(rows):
    vertl.append(0)
for i in range(1,rows,1):
    sum=0
    for j in range(1,cols,1):
        if I[i][j] > I[i][j-1]:
            difference = I[i][j]-I[i][j-1]
            
        if I[i][j] <= I[i][j-1]:
            difference = I[i][j-1]-I[i][j]
            
        if difference>20:
            sum = sum+difference
            
       
    vertl[i] = sum
    ##Find Peak in Vertical Histogram
    if sum>maximum:
        max_vert=i
        maximum = sum
        
    total_sum = total_sum + sum
    
average = total_sum/rows
plt.subplot(311)
plt.plot(vertl)
plt.xlabel('Row Number ->')
plt.ylabel('Differnce ->')
plt.title('Vertical Edge Processing Histogram')
#plt.show()
##Smoothen the Vertical Histogram by applying Low Pass Filter
print('Passing Vertical Histogram through Low Pass Filter')
sum =0
vert = []
vert=vertl
for i in range(20,rows-20,1):
    sum=0
    for j in range(i-20,i+20,1):
        sum = sum + vertl[j]
    vert[i] = sum/41

plt.subplot(312)
plt.plot(vert)
plt.xlabel('Row Number ->')
plt.ylabel('Differnce ->')
plt.title('Histogram after passing through Low Pass Filter')
#plt.show()
##Filter out Vertical Histogram Values by applying Dynamic Threshold
print('Filter out Vertical Histogram...')
for i in range(rows):   
    if vert[i] < average:
        vert[i] = 0
        for j in range(cols):
            I[i][j] = 0   

plt.subplot(313)
plt.plot(vert)
plt.xlabel('rows Number ->')
plt.ylabel('Differnce ->')
plt.title('Histogram after Filtering')
plt.subplots_adjust(hspace=1)
plt.show()
cv2.imshow("I",I)
cv2.waitKey(0)
##Find probable candidates for number plate

##Region of interest extraction
cv2.imshow('1',I)
Isc = I
Igray = I
rows = Igray.shape[0]
cols = Igray.shape[1]
##Dilate and Erode Image in order to remove noise
Idilate = Igray

kernel = np.ones((3,3),np.uint8)
Idilate = cv2.dilate(Igray,kernel,iterations=1)
imerode = cv2.erode(Idilate,kernel,iterations=1)
I = imerode

cv2.imshow('2',Igray)
cv2.imshow('3 Dilated Image',Idilate)
cv2.imshow('4',I)
difference=0
sum=0
total_sum=0
##Process edge in horizontal direction
print('Processing Edges Horizontally...')
max_horz=0
maximum=0
horz1 = []
for i in range(cols):
    horz1.append(0)
for i in range(1,cols,1):
    sum = 0
    for j in range(1,rows,1):
        if I[j][i] > I[j-1][i]:
            difference = I[j][i]-I[j-1][i]
        else:
            difference = I[j-1][i]-I[j][i]
            
        if difference >20:
            sum = sum + difference
            
        
    horz1[i] = sum
    ##Find peak value
    if sum>maximum:
        max_horz = i
        maximum = sum
        
    total_sum = total_sum +sum
    
average = total_sum / cols
##Plot the histogram for analysis
plt.subplot(414)
plt.plot(horz1)
plt.xlabel('Column Number ->')
plt.ylabel('Difference ->')
plt.title('Horizontal Edge Processing Histogram')
#plt.show()
##Smoothen the Horizontal Histogram by applying Low Pass Filter
horz.clear()
sum = 0
horz = horz1
for i in range(20,cols-20,1):
    sum = 0
    for j in range(i-20,i+20,1):
        sum = sum + horz1[j]
        
    horz[i] = sum/41
    
plt.subplot(312)
plt.plot(horz)
plt.xlabel('Column Number ->')
plt.ylabel('Difference ->')
plt.title('Histogram after passing through Low Pass Filter')
#plt.show()
##Filter out Horizontal Histogram Values by applying Dynamic Threshold
print('Filter out Horizontal Histogram...')
for i in range(1,cols,1):
    if horz[i] < average:
        horz[i] = 0
        for j in range(1,rows,1):
            I[j][i] = 0
            
        
    
plt.subplot(313)
plt.plot(horz)
plt.xlabel('Column Number ->')
plt.ylabel('Difference ->')
plt.title('Histogram after Filtering')
plt.subplots_adjust(hspace=1)
plt.show()
## Smoothing Data by apply moving average filter
print('Smoothing data...')
modes = ['full','same','valid']
for m in modes:
    N=150
    horz = np.convolve(horz, np.ones((N,))/N, mode=m)
    plt.plot(horz)
    
plt.legend(modes)
plt.title('Horz Graph')
plt.show()
##Find peaks
print('Detecting peak point...')
peaks, _=find_peaks(horz,prominence=1)

plt.plot(peaks, horz[peaks], "vg"); plt.plot(horz)
plt.title('Peak spot')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()