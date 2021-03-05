import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lucy.jpg', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 150, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)
#Dilating the image
dilate = cv.dilate(mask, kernal, iterations=2)

#erosion operation
erosion = cv.erode(mask, kernal, iterations=2)

titles = ['Image', 'Mask','Dilation', 'Erosion']
images = [img, mask, dilate, erosion]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()