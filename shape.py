import cv2
import numpy as np

img=cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)
final=cv2.imread('img.jpg')
_,threshold=cv2.threshold(img,220,255,cv2.THRESH_BINARY)

contoour,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for ctn in contoour:

    epsilon = 0.01 * cv2.arcLength(ctn, True)
    approx = cv2.approxPolyDP(ctn, epsilon, True)
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 1)
    x=approx[0][0][0]
    y=approx[0][0][1]
    if len(approx)==3:
        cv2.putText(final,"traingle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    if len(approx)==4:
        cv2.putText(final,"rectangle",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    if len(approx)==5:
        cv2.putText(final,"pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0),1)
    if len(approx)==6:
        cv2.putText(final,"Hexagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0),1)
    if len(approx)>10:
        cv2.putText(final,"circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)


cv2.imshow("output",final)
cv2.waitKey(0)