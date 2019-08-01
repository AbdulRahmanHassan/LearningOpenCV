import cv2
import numpy as np

def imread():
    img = cv2.imread('36980951_1882465672054837_1814836167477035008_n.jpg',0)
    cv2.imwrite('Gray.PNG',img)
    cv2.imshow('image',img)

    cv2.waitKey(0)


def viread():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def Drawing():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def Future():
    img = cv2.imread('Single shape.PNG')
    canny = cv2.Canny(img,140,240)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,contours,0,(0,0,255),2)
    moment = cv2.moments(contours[0])
    Cx = int(moment['m10']/moment['m00'])
    Cy = int(moment['m01']/moment['m00'])
    cv2.circle(img,(Cx,Cy),1,(0,0,255),-1)
    print(moment)
    cv2.imwrite('Gray.PNG',img)
    cv2.imshow('image',img)

    cv2.waitKey(0)


Future()