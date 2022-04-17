import cv2 as cv2
import numpy as np

f = cv2.imread('tes.jpg')


panj = 720;
leb =  900;
perkecil = (panj,leb)
foto = cv2.resize(f,perkecil,interpolation= cv2.INTER_LINEAR)


mask = np.zeros(foto.shape[:2], dtype="uint8")
cv2.rectangle(mask, (280, 380), (500, 900), 255, -1)
mask0 = cv2.bitwise_and(foto,foto, mask=mask)

background = cv2.imread('newyork.jpg')
crop = cv2.resize(background,perkecil,interpolation= cv2.INTER_LINEAR)
crop[mask != 0] = [0,0,0]

gantibg = mask0 + crop

cv2.imshow('perkecil',foto)
cv2.imshow('mask',mask0)
cv2.imshow('bg',crop)
cv2.imshow('foto',gantibg)


ch= cv2.waitKey(0) & 0xFF 
cv2.destroyAllWindows()