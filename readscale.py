import cv2 as cv

img=cv.imread('images/2.jpeg')
cv.imshow('Dog',img)

def rescaleFrame(frame , scale=0.75):
    # images,videos and live videos
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimesions=(width,height)

    return cv.resize(frame,dimesions,interpolation=cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Image',resized_image)

def changeRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)

# #reading videos
capture=cv.VideoCapture('videos/huhh.mp4')
while True:
    isTrue, frame=capture.read()

    frame_resized=rescaleFrame(frame, scale=.2)
    cv.imshow('video', frame)
    cv.imshow('Video resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
