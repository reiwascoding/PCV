import cv2 as cv2
import numpy as np

f = cv2.imread('fotomer.jpg')


panj = 481;
leb =  519;
perkecil = (panj,leb)

lower_bound = np.array([0, 0, 180],dtype="uint8")
upper_bound = np.array([100, 100,255],dtype="uint8")
mask0 = cv2.inRange(f, lower_bound, upper_bound)
mask0 = cv2.bitwise_not(mask0)
masked_image = cv2.bitwise_and(f,f,mask=mask0)

background = cv2.imread('newyork.jpg')
crop = cv2.resize(background,perkecil,interpolation= cv2.INTER_LINEAR)
crop[mask0 != 0] = [0,0,0]

hasil = crop + masked_image

cv2.imshow('asli',f)
cv2.imshow('mask', mask0)
cv2.imshow('hasil mask', masked_image)
cv2.imshow('bg',background)
cv2.imshow('ganti bg',hasil)



ch= cv2.waitKey(0) & 0xFF 
cv2.destroyAllWindows()