import cv2 as cv

img =cv.imread('images/3.jpeg')
cv.imshow('Dog',img)

#converting to grayscale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur 
# blur=cv.GaussianBlur(img , (3,3),cv.BORDER_DEFAULT)
blur=cv.GaussianBlur(img , (11,11),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascade
# canny =cv.Canny(img,125,175)
canny =cv.Canny(blur,125,175) 
cv.imshow('Canny Edges',canny)

# dilating the image
# dilated=cv.dilate(canny,(3,3),iterations=1)
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated', dilated)

#eroding
# eroded=cv.erode(dilated,(3,3),iterations=1)
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#resize 
# resized=cv.resize(img,(500,500))
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#cropping 
cropped=img[50:200,200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)

# 44