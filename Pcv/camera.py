# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:16:20 2022

@author: Eko Mulyanto
"""


import cv2 as cv
import numpy as np
import random
import math as mt 



cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
#    cv.imshow('frame2', diff2)
    cv.imshow('frame3', frame)
  
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
