
import cv2
import numpy as np
import math
import serial
import time
boole=True
myser = serial.Serial('COM6', 9600)
if(boole==True):
    myser.write(b'F')
    time.sleep(6)
    boole=True
myser.close()
# Calculate distance between two points
def distance(x0,y0,x1,y1):
    dist = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    return dist

def score(points):
        # Get center coordinates of big black center circle and his radius
        # These are now references for calculating score
        
        print("points ",points)
        x0=256
        y0=252
        r0 = 90
        
        # Score variable
        score = np.array([])
        # Victor with radius of target levels
        t_dis = [r0-24*3,r0-24*2,r0-24,r0,r0+24,r0+24*2,r0+24*3,r0+24*4,r0+24*5,r0+24*6]
        # If do not have any shot
        if (False):
            score = []
            sum_score = 0
        else:
            # For each detected shot calculate distance and compare to target level
            for j in points:
                if distance(x0,y0,j[0],j[1]) < t_dis[0]:
                    score = np.append(score,10)
                elif distance(x0,y0,j[0],j[1]) < t_dis[1]:
                    score = np.append(score,9)
                elif distance(x0,y0,j[0],j[1]) < t_dis[2]:
                    score = np.append(score,8)
                elif distance(x0,y0,j[0],j[1]) < t_dis[3]:
                    score = np.append(score,7)
                elif distance(x0,y0,j[0],j[1]) < t_dis[4]:
                    score = np.append(score,6)
                elif distance(x0,y0,j[0],j[1]) < t_dis[5]:
                    score = np.append(score,5)
                elif distance(x0,y0,j[0],j[1]) < t_dis[6]:
                    score = np.append(score,4)
                elif distance(x0,y0,j[0],j[1]) < t_dis[7]:
                    score = np.append(score,3)
                elif distance(x0,y0,j[0],j[1]) < t_dis[8]:
                    score = np.append(score,2)
                elif distance(x0,y0,j[0],j[1]) < t_dis[9]:
                    score = np.append(score,1)
                else:
                    score = np.append(score,0)
                
        # Sum score
        sum_score = sum(score)
        # Print score vector
        print('Your score is: ',score)
        # Print sum score
        print('Your sum score is: ',sum_score)
        




videoCaptureObject = cv2.VideoCapture(0)
videoCaptureObject.set(3, 1920)
videoCaptureObject.set(4, 1080)
a=int(input("Capture"))
result=True
while(result):
    if(a==1):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("ProImage.jpg",frame)
        result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
# read image as grayscale
print()
imga = cv2.imread('ProImage.jpg')
print(imga.shape)
cv2.imshow("Before Crop",imga)
cv2.imwrite("BeforeCrop.jpg",imga)
print(imga.shape)
#       dow top  lef rig
img= imga[120:245, 910:1035]
cv2.imshow("After Crop",img)
size = (512,509)
    
img = cv2.resize(img,size)

hh, ww = img.shape[:2]



# shave off white region on right side
img = img[0:hh, 0:ww-2]

# convert to gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# median filter
median = cv2.medianBlur(gray, 3)

# do canny edge detection
canny = cv2.Canny(median, 100, 200)

# get canny points
# numpy points are (y,x)
points = np.argwhere(canny>0)
arr=[points[0]]

#print(len(points))


for i in range(0,len(points)-1):
    if(abs(points[i][0]-points[i+1][0])>5):
        arr.append(points[i+1])

for j in arr:
    print(j[0])
score(arr)
print("Hello...")
print(arr)


rimg = cv2.imread('sample.jpg')
red = [0, 0, 255]
for i in range(0,len(arr)):
    cv2.circle(rimg, (arr[i][1],arr[i][0]+5), 9, red, -1)

cv2.imshow('rimg', rimg)
cv2.imshow('img', img)


cv2.waitKey(0)
