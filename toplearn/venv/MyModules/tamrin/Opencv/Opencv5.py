import cv2
import numpy as np

img1 = cv2.imread(r'D:\Ax Armin\image.jpg')
img2 = cv2.imread(r'D:\Ax Armin\image 2.jpg')

# add = img1 + img2
# add = cv2.add(img1,img2)
add = cv2.addWeighted(img1,0.7,img2,0.4,0)

cv2.imshow('image 1',img1)
cv2.imshow('image 2',img2)
cv2.imshow('add', add)

cv2.waitKey(0)
cv2.destroyAllWindows()
