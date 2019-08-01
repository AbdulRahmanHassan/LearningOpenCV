import cv2
import numpy as np


img = cv2.imread('median.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
box = cv2.boxFilter(img,-5,(3,3))
median = cv2.medianBlur(img,21)
cv2.imshow('dst',dst)
cv2.imshow('blur',blur)
cv2.imshow('bl2ur',box)
cv2.imshow('img',img)
cv2.imshow('median',median)


cv2.waitKey(0)
cv2.destroyAllWindows()