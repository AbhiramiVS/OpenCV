import cv2 as cv

#Defining a function to scale the image/video

cap = cv.VideoCapture('Pose_est.mp4')

def rescale(frame, scale=0.75):
    # This method will work in Image, Video and Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #Work only on Live video
    cap.set(3, width)
    cap.set(4, height)


while True:
    IsTrue, frame = cap.read()
    if not IsTrue:
        print('Show Over!!!!')
        break
    frame_resized = rescale(frame, 0.3)

    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()