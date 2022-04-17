import cv2 as cv2
import numpy as np

f = cv2.imread('bg.jpeg')

dim=f.shape
print(dim)
hsv= np.double(cv2.cvtColor(f, cv2.COLOR_BGR2HSV))

lower_bound = np.array([90, 0, 0],dtype="uint8")
upper_bound = np.array([150, 255, 255],dtype="uint8")
mask0 = cv2.inRange(hsv, lower_bound, upper_bound)
mask0 = cv2.bitwise_not(mask0)
output_img1 = cv2.bitwise_and(f,f,mask=mask0)



cv2.imshow('frames', f)

cv2.imshow('mask', mask0)
cv2.imshow('hasil', output_img1)






ch= cv2.waitKey(0) & 0xFF 
cv2.destroyAllWindows()