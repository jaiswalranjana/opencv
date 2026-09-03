import cv2 as cv
import numpy as np


# blank=np.zeros((500,500),dtype='uint8')

blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
# img=cv.imread('images/1.jpeg')
# cv.imshow('Cat',img)

#paint the image a certain color
# blank[:]=0,255,0
# blank[200:300,300:400]=0,0,255
# cv.imshow('Green',blank)

#draw a rectangle
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=2)
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED)
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
# cv.rectangle(blank,(0,0),(blank.shape[1]//2 , blank.shape[0]//2),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)

#draw a circle 
# cv.circle(blank,(blank.shape[1]//2 , blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)

#draw a line 
# cv.line(blank,(0,0),(blank.shape[1]//2 , blank.shape[0]//2),(255,255,255),thickness=3)
# cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
# cv.imshow('Line',blank)

#write a text
# cv.putText(blank,"Hello, Ranjana Here . I m just dealing with life stuff ",(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.putText(blank,"Hello, Ranjana Here . I m just dealing with life stuff ",(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow("Text",blank)
#overflow?????????of text
cv.waitKey(0)