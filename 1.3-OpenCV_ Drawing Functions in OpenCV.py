import cv2
import numpy as np

def nothing(x):
    pass

def Trackbars():
    cv2.namedWindow('Trackbars Window')
    cv2.resizeWindow('Trackbars Window', 610,610)


    # create trackbars for color change
    cv2.createTrackbar('Min Hue','Trackbars Window',0,600,nothing)
    cv2.createTrackbar('Min Sat','Trackbars Window',0,600,nothing)
    cv2.createTrackbar('Min Val','Trackbars Window',0,600,nothing)
    cv2.createTrackbar('Max Hue','Trackbars Window',0,600,nothing)
    cv2.createTrackbar('Max Sat','Trackbars Window',0,600,nothing)
    cv2.createTrackbar('Max Val','Trackbars Window',0,600,nothing)

    # Set default value for MAX HSV trackbars.
    cv2.setTrackbarPos('Max Hue', 'Trackbars Window', 179)
    cv2.setTrackbarPos('Max Sat', 'Trackbars Window', 255)
    cv2.setTrackbarPos('Max Val', 'Trackbars Window', 255)


def Drawing():
    cap = cv2.VideoCapture(0)

    while True :
        ret, frame = cap.read()

        hMin = cv2.getTrackbarPos('Min Hue','Trackbars Window')
        sMin = cv2.getTrackbarPos('Min Sat','Trackbars Window')
        vMin = cv2.getTrackbarPos('Min Val','Trackbars Window')
        hMax = cv2.getTrackbarPos('Max Hue','Trackbars Window')
        sMax = cv2.getTrackbarPos('Max Sat','Trackbars Window')
        vMax = cv2.getTrackbarPos('Max Val','Trackbars Window')

        cv2.rectangle(frame,(vMin,vMax),(hMin,hMax),(0,0,255),-1)
        cv2.rectangle(frame,(564,451),(510,398),(0,0,255),-1)
        cv2.circle(frame,(537,348),32,(0,0,255),-1)

        pt1 = (hMin, sMin)
        pt2 = (vMin, hMax)
        pt3 = (sMax, vMax)
        triangle_cnt = np.array([pt1, pt2, pt3])
        cv2.drawContours(frame, [triangle_cnt], 0, (0, 0, 255), -1)

        cv2.imshow('frame',frame)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
Trackbars()
Drawing()