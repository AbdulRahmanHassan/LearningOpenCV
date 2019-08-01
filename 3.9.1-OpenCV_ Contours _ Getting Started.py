import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Trackbars Window')
cv2.resizeWindow('Trackbars Window', 600,155)

cv2.createTrackbar('Min TH','Trackbars Window',0,400,nothing)
cv2.createTrackbar('Max TH','Trackbars Window',0,400,nothing)

cv2.setTrackbarPos('Min TH', 'Trackbars Window', 130)
cv2.setTrackbarPos('Max TH', 'Trackbars Window', 200)

cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()

    Min = cv2.getTrackbarPos('Min TH','Trackbars Window')
    Max = cv2.getTrackbarPos('Max TH','Trackbars Window')

    edges = cv2.Canny(frame,Min,Max)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 0, 255), 1)

    cv2.imshow('img',frame)
    cv2.imshow('Canny',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

