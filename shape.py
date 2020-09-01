import cv2
import numpy as np
# read the image and convert into grayscale
img=cv2.imread('img.jpg',cv2.IMREAD_GRAYSCALE)
final=cv2.imread('img.jpg')

# apply threshlod to conveert the image into black and white so it will be easy to find the contour from the image
_,threshold=cv2.threshold(img,220,255,cv2.THRESH_BINARY)

# find the contour
contoour,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# apply for loop to to find the lenght of each shapes 
for ctn in contoour:
    # use approximation function to find the nearset points from the shape so it will show accurate output
    epsilon = 0.01 * cv2.arcLength(ctn, True)
    approx = cv2.approxPolyDP(ctn, epsilon, True)
    # now lets draw some color on that detected shape 
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 1)
    # finding the x and y coordinate of the first point of the shape 
    x=approx[0][0][0]
    y=approx[0][0][1]
    
    # now checking the side or length of shape and show the output according to lenght
    if len(approx)==3:
        # this function used to show some text on the output screen 
        cv2.putText(final,"traingle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    if len(approx)==4:
        cv2.putText(final,"rectangle",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
    if len(approx)==5:
        cv2.putText(final,"pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0),1)
    if len(approx)==6:
        cv2.putText(final,"Hexagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.3,(0,0,0),1)
    if len(approx)>10:
        cv2.putText(final,"circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)

# show the output image 
cv2.imshow("output",final)
# use waitkey show that the output will be visisble until input is taken from keyword
cv2.waitKey(0)
