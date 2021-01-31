import cv2
import numpy as np

#capture = cv2.VideoCapture('video.mp4') #Video
#capture = cv2.VideoCapture(0) # Webcam 0,1,2
capture = cv2.VideoCapture('http://192.168.1.2:5000/') # IP camera

while True:

    ret, frame = capture.read()
    cv2.imshow('Output', frame)
    k = cv2.waitKey(10)&0xFF
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()