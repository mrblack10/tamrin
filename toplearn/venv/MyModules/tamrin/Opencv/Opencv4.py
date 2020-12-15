import cv2
import numpy as np

img = cv2.imread('D:\Ax Armin\image.jpg',cv2.IMREAD_COLOR)

# px = img[200,200] # moshakhasat rang on pixel
# print(px)

# img[100:200,100:200] = [255,255,255] # sefid krdn on tike
# img[200:300,100:200] = [0,0,0]       # siah krdn on tike
# img[300:400,100:200] = img[200:300,200:300]



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


