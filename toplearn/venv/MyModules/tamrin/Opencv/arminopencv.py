import cv2
import numpy as np

img1 = cv2.imread(r'D:\Ax Armin\image 3.jpg')
# cv2.imshow('src1',img1)
img2 = cv2.imread(r'D:\Ax Armin\thunderbolt logo\thunderbolt 12.jpg')
# cv2.imshow('src2',img2)

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img2gray',img2gray)

ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)
# cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
# cv2.imshow('mask_inv', mask_inv)

rows1, cols1, channels1 = img1.shape
rows2, cols2, channels2 = img2.shape
roi = img1[0:rows2, cols1 - cols2: cols1]
# cv2.imshow('roi', roi)

img_bg = cv2.bitwise_and(roi, roi, mask=mask)
# cv2.imshow('img_bg', img_bg)

img_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
# cv2.imshow('img_fg', img_fg)

dst = cv2.add(img_bg,img_fg)
# cv2.imshow('dst', dst)

img1[0:rows2, cols1 - cols2: cols1] = dst
cv2.imshow('img1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
