from skimage.measure import compare_ssim
import argparse
import imutils
import cv2 as cv 
import numpy as np

erosion_size = 0
max_elem = 2
max_kernel_size = 21
title_trackbar_element_type = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse'
title_trackbar_kernel_size = 'Kernel size:\n 2n +1'
title_erosion_window = 'Erosion Demo'
title_dilatation_window = 'Dilation Demo'

def erosion(val,image):
    erosion_size = 0
    erosion_type = 0
    val_type = val
    if val_type == 0:
        erosion_type = cv.MORPH_RECT
    elif val_type == 1:
        erosion_type = cv.MORPH_CROSS
    elif val_type == 2:
        erosion_type = cv.MORPH_ELLIPSE
    element = cv.getStructuringElement(erosion_type, (2*erosion_size + 1, 2*erosion_size+1), (erosion_size, erosion_size))
    erosion_dst = cv.erode(image, element)
    return erosion_dst

# load input and convert it to gray scale 
imageA = cv.imread("image3.jpg")
grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
cv.imwrite('grayimage.jpg', grayA)

#cv2.imshow("gray image", grayA)

#thresholding 
ret,thresh1 = cv.threshold(grayA,200,255,cv.THRESH_BINARY_INV)
cv.imwrite('thresh.jpg', thresh1)
cv.imshow("threshold",thresh1)

contours, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(thresh1, contours, -1, (0,255,0), 3)
print("The length of list is: ", len(contours))
cv.imshow("threshold",thresh1)

#Erosion 
kernel = np.ones((5,5),np.uint8)
er = erosion(1,thresh1) 
cv.imwrite('erosion.jpg', er)
#cv2.imshow("erosion", erosion)


cv.waitKey(0)
