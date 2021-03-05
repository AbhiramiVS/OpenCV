import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Paris.jpg')
#cv.imshow('Image', img)

#To convert BGR to GrayScale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#To blur an image
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#Kernel size should be in odd numbers and blurring is directly proportional to the kernel value

# For more blurring
blur_more = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur_More',blur_more)

# Edge cascading
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Image', canny)

edge = cv.Canny(blur,125,175)
#cv.imshow('Edge', edge)


titles = ['Image', 'Edge']
images = [img, edge]
for i in range(3):
    plt.subplot(1,3,i+1), plt.imshow(images[i])
    plt.title(titles[i])

plt.show()

cv.waitKey(0)