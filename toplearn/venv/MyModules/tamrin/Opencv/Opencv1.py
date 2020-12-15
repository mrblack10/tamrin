import cv2
import numpy as np
from matplotlib import pyplot

img = cv2.imread('D:\Ax Armin\image.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)

pyplot.imshow(img,cmap='gray',interpolation='bicubic')
pyplot.plot([100,200],[200,200],'r',linewidth = 5)
pyplot.show()
# cv2.imwrite('imgout.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
