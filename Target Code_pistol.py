import cv2
import numpy as np
import math
import serial
import time
from tkinter import *
from tkinter import messagebox
import os


win = Tk()
win.geometry('720x520')
win.title('Pistol Target')

#motor controll
def motor_run():
    boole=True
    try:
        myser = serial.Serial('COM7', 9600)
        boole=True
        if(boole==True):
            myser.write(b'A')
            time.sleep(6)
        boole=True
        myser.close()
    except:
        print('Serial Error!')

# Calculate distance between two points
def distance(x0,y0,x1,y1):
    dist = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    return dist

def score(points):
        # Get center coordinates of big black center circle and his radius
        # These are now references for calculating score
        
        print("points ",points)
        x0 = 251
        y0 = 251
        r0 = 85
        
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
        for s in score:
            round_score.append(s)
        '''label_score = Label(win, text=score,font=('Arial', 14), anchor='w')
        label_score.place(relx=0.6, rely=0.4, anchor=CENTER)'''
        #messagebox.showinfo('Your score is: '+score)
        #messagebox.showinfo('Your sum score is: ',sum_score)

if __name__ == '__main__':
    round_count=0
    image_arr=[]
    round_score=[]

    while round_count<1: 
        #Motor run will be activated when testing in real time
        motor_run()

        time.sleep(5) #delay time
        '''
        videoCaptureObject = cv2.VideoCapture(1)
        videoCaptureObject.set(3, 1920)
        videoCaptureObject.set(4, 1080)
        a=1
        #a=int(input("Capture"))
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
        imga = cv2.imread('ProImage.jpg')'''
        if round_count==0:
            imga = cv2.imread(r'D:\Python Codes\Target_pistol\1.jpg')
        elif round_count==1:
            imga = cv2.imread(r'D:\Python Codes\Target_pistol\3.jpg') #image without hit
        else:
            imga = cv2.imread(r'D:\Python Codes\Target_pistol\2.jpg')
        
        #cv2.imshow('title', imga)
        #print(imga.shape)
        #cv2.imshow("Before Crop",imga)
        #cv2.imwrite("BeforeCrop.jpg",imga)
        #print(imga.shape)
        #dow top  lef rig
        #img= imga[22:770, 37:765]
        #cv2.imshow("After Crop",img)
        
        size = (512,512)            
        img = cv2.resize(imga,size)
        #cv2.imshow('Processing Image', img)
        hh, ww = img.shape[:2]

        # shave off white region on right side
        img = img[0:hh, 0:ww-2]

        # convert to gray
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # median filter
        median = cv2.medianBlur(gray, 3)

        # do canny edge detection
        try:
            canny = cv2.Canny(median, 100, 200)
            #cv2.imshow('Edges', canny)
            # get canny points
            # numpy points are (y,x)
            points = np.argwhere(canny>0)
            arr=[points[0]]  #coordinated of hit detected
            #print(points)
            #print(len(points))

            for i in range(0,len(points)-1):
                if(abs(points[i][0]-points[i+1][0])>5):
                    arr.append(points[i+1])

            for j in arr:
                print(j[0])
            score(arr)
            #print("Hello...")
            image_arr+=arr
            print('X: ',arr[0][0])
            print('Y: ',arr[0][1])
        except:
            print('No Hit Found')
            #messagebox.showerror('No Hit found')
        round_count+=1

    
    rimg = cv2.imread('D:\Python Codes\Target_pistol\display_image.png')
    red = [0, 0, 255]
    print('img_arr', image_arr)
    for i in range(0,len(image_arr)):
        cv2.circle(rimg, (image_arr[i][1]+5,image_arr[i][0]), 4, red, 2)

    #cv2.imshow('rimg', rimg)
    cv2.imwrite('score_img.png', rimg)
    #cv2.imshow('img', img)

    target_img = PhotoImage(file = 'score_img.png')
    img_label = Label(image = target_img)
    img_label.place(relx=0.02,rely=0.02,anchor=CENTER)
    img_label.pack()
    print('------------------------------------')
    round_score = list(map(int,round_score))
    print('Round Score:',round_score)
    print('Round Total:',sum(round_score))
    '''
    scores_ = Text(win)
    scores_.grid(row=0,column=2)
    scores_.pack()
    for mark in score:
        scores_.insert(END, mark+' ')'''
    cv2.waitKey(0)
    win.mainloop()
