from skimage.measure import compare_ssim
import argparse
import imutils
import cv2 as cv 
import numpy as np


def findContour(image):
    contours, hierarchy = cv.findContours(image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    count = 0
    contoursN = contours
    maxC = 0
    #finding the maximum contour 
    for  i in range(len(contours)):
        print (cv.contourArea(contours[i]))
        if cv.contourArea(contours[i]) > maxC:
            maxC = cv.contourArea(contours[i])
    print (maxC)
    for  i in range(len(contours)):
        if  cv.contourArea(contours[i]) > maxC*0.03:
            contoursN[count] = cv.approxPolyDP(contours[i],15,True)
            count = count + 1
    print("number of contours:", count)
    return contoursN,count



# load input and convert it to gray scale 
imageA = cv.imread("sign_distorted.jpg")
grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
cv.imwrite('grayimage.jpg', grayA)

#thresholding 
ret,thresh1 = cv.threshold(grayA,200,255,cv.THRESH_BINARY_INV)
cv.imwrite('thresh.jpg', thresh1)
cv.imshow("threshold",thresh1)

#Finding Contours of the sign
contoursN, count = findContour(thresh1)
#printing the approximation
for  i in range(0,count):
    print("contour"+str(i)+" size ="+str(len(contoursN[i]))) 

# Triangle Detection
if len(contoursN[0]) == 3:
    hsv = cv.cvtColor(imageA, cv.COLOR_BGR2HSV)
    print("The sign has a shape of a Triangle.")
    lower_green = np.array([50,50,50])
    upper_green = np.array([120,255,255])

    # Threshold the HSV image to get only green colors
    mask = cv.inRange(hsv, lower_green, upper_green)
    cv.imshow("green",mask)
    contoursN1, count1 = findContour(mask)
    if count1 > 0:
                print ("This has a green color.")
                print("traffic lights ahead")
    elif count == 2 or count == 1:
        point1 = contoursN[0][1][0][1]
        point2 = contoursN[0][2][0][1]
        differ = abs(point1 - point2)
        if differ < 11:
            print("dangerous descent.")
        else:
            print("Give Way")
    elif count == 3:
        print("Bumby Road")
# elif count > 4 :
#     if len(contoursN[count - 4]) == 3:
#         if count == 7:
#             print("The sign has a shape of a Triangle.")
#             print("Traffic Lights Ahead.")     
#Circle Detection
elif len(contoursN[0]) > 6:
    print("The sign has a shape of a Circle or Octagon.")
    #print("",len(contoursN)-2)
    if count == 1:
        print("No Parking.")
    elif len(contoursN[count-1]) == 9 & len(contoursN[count-2]) == 9 & len(contoursN[count-3]) == 9  :
        print("Circular.")
    elif len(contoursN[count-1]) > 8 or count == 6:
        print("Stop.")
    elif count == 3:
        print("No Entry.")
    elif count == 5:
        print("End Speed Limit.")
    elif count == 4:
        point1 = contoursN[count-1][0][0][0]
        point2 = contoursN[count-1][0][0][1]
        if len(contoursN[count-1]) == 4:
            print("No Entry.") 
        elif point1 > point2:
            point1 = contoursN[count-1][0][0][0]
            point2 = contoursN[count-1][1][0][0]
            dif = point2 - point1
            if dif > 5:
                print("Go Straight.")
            else:
                print("Give Way")
        elif count == 3:
            print("Bumby Road")
        elif count == 5:
            print("Traffic Lights Ahead.")
            
    #Circle Detection
    elif len(contoursN[0]) > 6:
        print("The sign has a shape of a Circle or Octagon.")
        #print("",len(contoursN)-2)
        if count == 1:
            print("No Parking.")
        elif count == 3:
            print("No Entry.")
        elif len(contoursN[count-1]) > 10 :
            print("Stop.")
        elif count == 5:
            print("End Speed Limit.")
        else:
            point1 = contoursN[count-1][0][0][0]
            point2 = contoursN[count-1][0][0][1]
            if point1 > point2:
                point1 = contoursN[count-1][0][0][0]
                point2 = contoursN[count-1][1][0][0]
                dif = point2 - point1
                if dif > 5:
                    print("Go Straight.")
                else:
                    print("Go Right.")
            elif point1 < point2:
                print("Go Left.")
                
    #Rectangle Detection
    elif len(contoursN[0]) == 4:
        print("The sign has a shape of a Rectangle.")
        hsv = cv.cvtColor(imageA, cv.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([97,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_blue, upper_blue)
        cv.imshow("blue",mask)
        contoursN1, count1 = findContour(mask)
        if count1 > 0:
            print("This has a blue color.")
            print("Freeway Entry.")
        else:
            lower_yellow = np.array([22,50,50])
            upper_yellow = np.array([32,255,255])
            # Threshold the HSV image to get only blyellow colors
            mask = cv.inRange(hsv, lower_yellow, upper_yellow)
            cv.imshow("yellow",mask)
            contoursN1, count1 = findContour(mask)
            if count1 > 0:
                print ("This has a green color.")
                print("Major Road Sign.")
            else:
                print("end of speed limit")
                           
#Pentagon Detection
elif len(contoursN[0]) == 5:
    print("The sign has a shape of a Pentagon.")
    hsv = cv.cvtColor(imageA, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_brown = np.array([0,50,50])
    upper_brown= np.array([30,255,255])
    # Threshold the HSV image to get only brown colors
    mask = cv.inRange(hsv, lower_brown, upper_brown)
    cv.imshow("brown",mask)
    contoursN1, count1 = findContour(mask)
    if count1 > 0:
        print ("this has a brown color.")
        print("Tourist Destination.")
    else:
        print("Local Destination.")

cv.waitKey(0)