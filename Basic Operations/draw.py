import cv2 as cv
import numpy as np

blank = np.zeros((500, 500,3), dtype='uint8')
blank.fill(255)
cv.imshow('Blank', blank)

# To paint a certain colour
blank[:] = 127,127,127
cv.imshow('Colour_image', blank)

# Paint a portion of image
blank[200:500, 0:300] = 100,0,0
cv.imshow('Colour',blank)

#Drawing Rectangle
cv.rectangle(blank, (0,0),(250,250),(0,255,0),thickness=2)
cv.imshow('Rectangle', blank)

#To fill the rectangle with a color

cv.rectangle(blank, (0,0),(250,500),(0,100,0), thickness=cv.FILLED)
#you can use 'thickness=-1' also
cv.imshow('Rectangle', blank)

#Drawing a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 60,(0,255,0),thickness=2)
cv.imshow('Circle',blank)

#To fill the circle with a color
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 60, (0,255,0), thickness=-1)
cv.imshow('Circle', blank)

#Drawing a line
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0),thickness=3)
cv.imshow('Line', blank)

cv.waitKey(0)