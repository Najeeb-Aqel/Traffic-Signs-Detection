import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('free.jpg',0)

# Initiate STAR detector
orb = cv2.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)

# compute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location,not size and orientation
img2 = cv2.drawMarker(img,kp,(0,255,0))
plt.imshow(img2),plt.show()