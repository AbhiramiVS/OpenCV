import cv2 as cv

img = cv.imread('lucy.jpg')
cv.imshow('Image', img)

#Resize the image
#To reduce the size of image interpolation can be set to INTER_AREA
#To increase the size interpolation should be set to INTER_LINEAR or INTER_CUBIC

resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

#Cropping an image

cropped = img[50:800, 200:800]
cv.imshow('Cropped', cropped)

cv.waitKey(0)