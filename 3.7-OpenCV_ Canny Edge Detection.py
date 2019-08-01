import cv2

def nothing(x):
    pass

cv2.namedWindow('Trackbars Window')
cv2.resizeWindow('Trackbars Window', 1350,155)

cv2.createTrackbar('Min TH','Trackbars Window',0,400,nothing)
cv2.createTrackbar('Max TH','Trackbars Window',0,400,nothing)
cv2.createTrackbar('Max T','Trackbars Window',0,400,nothing)


cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()

    Min = cv2.getTrackbarPos('Min TH','Trackbars Window')
    Max = cv2.getTrackbarPos('Max TH','Trackbars Window')

    edges = cv2.Canny(frame,Min,Max)

    cv2.imshow('img',frame)
    cv2.imshow('Canny',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

