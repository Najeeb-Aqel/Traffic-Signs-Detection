from skimage.measure import compare_ssim
import argparse
import imutils
import cv2 as cv 
import numpy as np




# load input and convert it to gray scale 
imageA = cv.imread("up.jpg")
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
    if len(contours[i]) > 15:
        contoursN[count] = cv.approxPolyDP(contours[i],10,True)
        count = count + 1
#print("number of contours:", count)


#printing the approximation
# for  i in range(0,count):
#        print("contour"+str(i)+" size ="+str(len(contoursN[i]))) 
        
# Triangle Detection
if len(contoursN[0]) == 3:
    if count == 2:
        point1 = contoursN[0][1][0][1]
        point2 = contoursN[0][2][0][1]

        differ = abs(point1 - point2)
        if differ < 11:
            print("dangerous descent")
        else:
            print("give way")
    elif count == 3:
        print("bumby road")
    elif count == 5:
        print("traffic lights ahead")
#Circle Detection
elif len(contoursN[0]) > 6:
    #print("",len(contoursN)-2)
    if count == 1:
        print("No Parking")
    if count == 3:
        print("No Entry")
    elif count == 2 :
        print("Stop")
    elif count == 5:
        print("end speed limit")
    elif count == 4:
        print("right")
    elif count == 9:
        if len(contoursN[2]) == 2:
            print("left")
        elif len(contoursN[2]) == 4:
            print("up")
#Rectangle Detection
elif len(contoursN[0]) == 4:
    if count == 21:
        print("major road sign")
    elif count == 6:
        print("freeway entry")
    elif count == 13:
        print("exit")
#othershapes Detection
elif len(contoursN[0]) == 5:
    if count == 18:
        print("local destination")
    elif count == 23:
        print("tourist destination")



    
cv.waitKey(0)
