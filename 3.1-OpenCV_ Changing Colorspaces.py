import cv2
import numpy as np

def nothing(x):
    pass

# Create a window
def Trackbars():
    cv2.namedWindow('Trackbars Window')
    cv2.resizeWindow('Trackbars Window', 1350,310)


    # create trackbars for color change
    cv2.createTrackbar('Min Hue','Trackbars Window',0,179,nothing)
    cv2.createTrackbar('Min Sat','Trackbars Window',0,255,nothing)
    cv2.createTrackbar('Min Val','Trackbars Window',0,255,nothing)
    cv2.createTrackbar('Max Hue','Trackbars Window',0,179,nothing)
    cv2.createTrackbar('Max Sat','Trackbars Window',0,255,nothing)
    cv2.createTrackbar('Max Val','Trackbars Window',0,255,nothing)

    # Set default value for MAX HSV trackbars.
    cv2.setTrackbarPos('Max Hue', 'Trackbars Window', 179)
    cv2.setTrackbarPos('Max Sat', 'Trackbars Window', 255)
    cv2.setTrackbarPos('Max Val', 'Trackbars Window', 255)



def TrackColor():
    cap = cv2.VideoCapture(0)

    while True :
        ret, frame = cap.read()

        hMin = cv2.getTrackbarPos('Min Hue','Trackbars Window')
        sMin = cv2.getTrackbarPos('Min Sat','Trackbars Window')
        vMin = cv2.getTrackbarPos('Min Val','Trackbars Window')

        hMax = cv2.getTrackbarPos('Max Hue','Trackbars Window')
        sMax = cv2.getTrackbarPos('Max Sat','Trackbars Window')
        vMax = cv2.getTrackbarPos('Max Val','Trackbars Window')

        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)

        res = cv2.bitwise_and(frame,frame,mask = mask)

        cv2.resizeWindow('frame', 600,400)
        cv2.resizeWindow('res', 600,400)


        cv2.imshow('frame',frame)
        cv2.imshow('res',res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()



def Track2Color():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([20, 150, 150])
        upper_yellow = np.array([35, 255, 255])

        lower_blue = np.array([110, 100, 100])
        upper_blue = np.array([130, 255, 255])

        yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        red_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        mask = yellow_mask + red_mask
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()



def Track1Color():

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([20, 150, 150])
        upper_yellow = np.array([35, 255, 255])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


