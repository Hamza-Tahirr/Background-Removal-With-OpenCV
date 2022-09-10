from sre_constants import SUCCESS
import cv2
import cvzone
from cv.zone.SelfiSegmentationModule import SelfiSegmentation
import os 

cap =cv2.VideoCapture(0)
cap.set(3,648)
cap.set(4, 488)
segmentor= SelfiSegmentation() #for landscape 1

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img,(255,0,255))

    cv2.imshow("image",img)
    cv2.imshow('Image Out',imgOut)
    cv2.waitKey(1)