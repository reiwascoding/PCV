from configparser import Interpolation
import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.resize(frame, (1280, 720),
                         interpolation = cv2.INTER_LINEAR)
    cv2.imshow('frame',frame)
    
    batasbaw = np.array([100,100,100],dtype = "uint8")
    batasat = np.array([255,255,255],dtype = "uint8")
    mask = cv2.inRange(frame,batasbaw,batasat)
    mask = cv2.bitwise_not(mask)
    masked_vid = cv2.bitwise_and(frame,frame,mask=mask)
    
    bg = cv2.imread('panggung.png')
    bg[mask != 0] = [0,0,0]

    hasil = bg + masked_vid

    cv2.imshow('hasil video',hasil)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break





cap.release()
cv2.destroyAllwindows() 