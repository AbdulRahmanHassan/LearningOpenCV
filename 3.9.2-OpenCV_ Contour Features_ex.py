import cv2
import numpy as np

pt1 = (539, 215)
pt2 = (569, 270)
pt3 = (508, 270)
triangle_cnt = np.array( [pt1, pt2, pt3] )




def DetectShape(img):
    counter = {"TRI":0, "Circ":0, "Sqr":0, "Rec":0}

    img =cv2.imread(img)
    canny = cv2.Canny(img,179,239)
    contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,contours,-1,(0,255,0),1)
    for i in range (len(contours)):
        cnt = contours[i]
        moment = cv2.moments(cnt)
        Cx = moment['m10'] / moment['m00']
        Cy = moment['m01'] / moment['m00']
        epsilon = 0.03 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        if len(approx)==2:
            cv2.putText(img,'Rectangular',(int(Cx),int(Cy)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            counter["Rec"] += 1

        elif len(approx)==3:
            cv2.putText(img,'Tringle',(int(Cx),int(Cy)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            counter["TRI"] += 1

        elif len(approx)==4:
            cv2.putText(img,'Square',(int(Cx),int(Cy)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            counter["Sqr"] += 1

        else:
            cv2.putText(img,'Circle',(int(Cx),int(Cy)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            counter["Circ"] += 1

    cir = int(counter["Circ"] * 0.5)
    sqr = int(counter["Sqr"] * 0.5)
    rec = int(counter["Rec"] * 0.5)
    tri = int(counter["TRI"] * 0.5)

    cv2.rectangle(img,(509,298),(567,291),(0,0,255),-1)
    cv2.rectangle(img,(564,451),(510,398),(0,0,255),-1)
    cv2.circle(img,(537,348),32,(0,0,255),-1)
    cv2.drawContours(img, [triangle_cnt], 0, (0,0,255), -1)

    cv2.putText(img,'{}'.format(cir),(587,368), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(img,'{}'.format(sqr),(587,443), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(img,'{}'.format(rec),(587,303), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(img,'{}'.format(tri),(587,253), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('image',img)
    cv2.waitKey(0) & 0xFF


my_image = 'Shapes2.PNG'
my_image2 = 'Two Shapes.PNG'
DetectShape(my_image)

