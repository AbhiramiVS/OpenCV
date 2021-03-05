import cv2 as cv

#Reading Images
img = cv.imread('5.jpg')

cv.imshow('Tractor', img)

cv.waitKey(0)

#Reading Video

cap = cv.VideoCapture('Pose_est.mp4')

while True:
    IsTrue, frame = cap.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyWindow('Video')
