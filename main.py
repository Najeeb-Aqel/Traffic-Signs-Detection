from skimage.measure import compare_ssim
import argparse
import imutils
import cv2 as cv 
import numpy as np




# load input and convert it to gray scale 
imageA = cv.imread("Bump.jpg")
grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
cv.imwrite('grayimage.jpg', grayA)


#thresholding 
ret,thresh1 = cv.threshold(grayA,200,255,cv.THRESH_BINARY_INV)
cv.imwrite('thresh.jpg', thresh1)
cv.imshow("threshold",thresh1)


#finding contours 
contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
count = 0 

contoursN = contours
for  i in range(len(contours)):
    if len(contours[i]) > 50:
        contoursN[count] = cv.approxPolyDP(contours[i],10,True)
        count = count + 1
print("number of contours:", count)


#printing the approximation
for  i in range(0,count):
       print("contour"+str(i)+" size ="+str(len(contoursN[i]))) 
        

cv.waitKey(0)
