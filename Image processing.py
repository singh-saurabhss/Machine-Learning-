import numpy
import cv2
h=cv2.imread('C:\\Users\Saurabh singh\\Downloads\\WhatsApp Image 2019-09-18 at 10.31.16 AM.jpeg')
D=cv2.imread('C:\\Users\\Saurabh singh\\Downloads\\WhatsApp Image 2019-09-18 at 10.46.23 AM.jpeg')
cv2.imshow('hazy',h)
cv2.imshow('depth',D)
hsb=cv2.cvtColor(h,cv2.COLOR_BGR2HSV)
cv2.imshow('image',hsb)
hue=hsb[:,:,0]
sat=hsb[:,:,1]
bright=hsb[:,:,2]
cv2.imshow('hue',hue)
cv2.imshow('sat',sat)
cv2.imshow('bright',bright)
cv2.waitKey(0)
cv2.destroyAllWindows()
sumdepth=0
sumbright=0
sumsat=0
for i in range(11):
    h=cv2.imread('C:\\Users\Saurabh singh\\Downloads\\WhatsApp Image 2019-09-18 at 10.31.16 AM.jpeg')
    D=cv2.imread('C:\\Users\\Saurabh singh\\Downloads\\WhatsApp Image 2019-09-18 at 10.46.23 AM.jpeg')
    hsb=cv2.cvtColor(h,cv2.COLOR_BGR2HSV)
    sumdepth=sumdepth+D
    sumbright=sumbright+hsb[:,:,2]
    sumsat=sumsat+hsb[:,:1]
cv2.imshow("sumdepth",sumdepth)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(sumdepth) 
import cv2
import math
import numpy as np
h=cv2.imread('C:\\Users\Saurabh singh\\Downloads\\WhatsApp Image 2019-09-18 at 10.31.16 AM.jpeg')
D=cv2.imread('C:\\Users\\Saurabh singh\\Downloads\\WhatsApp Image 2019-09-18 at 10.46.23 AM.jpeg')
hsb=cv2.cvtColor(h,cv2.COLOR_BGR2HSV)
d=(0.959710 * hsb[:,:,2]-0.780245 * hsb[:,:,1]+0.121779)/255
t=np.exp(-d)
#hf=(h-0.5)/t+0.5;
#cv2.imshow('hazefreeimage',hf)
cv2.imshow('transmission image',t)
cv2.imshow("depth Actual",D)
cv2.imshow('depth estimate',d)
cv2.waitKey(0)
cv2.destroyAllWindows(0)             
             
             







