import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

bg = cv2.imread("panggung.png");


while True:
    success, img = cap.read()
    hasil = segmentor.removeBG(img,bg,threshold=0.8)
    cv2.imshow("Image", hasil)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()