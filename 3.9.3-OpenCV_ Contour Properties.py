import cv2

def contourprop(image):
    img = cv2.imread(image)
    canny = cv2.Canny(img,139,239)
    contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,contours,-1,(0,255,0),1)
    cnt = contours[0]


    x,y,w,h = cv2.boundingRect(cnt)

    aspect_ratio = float(w)/h
    area = cv2.contourArea(cnt)
    rect_area = w*h

    extend = float(area)/rect_area

    (x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

    print(MA,ma)
    print(angle)
    print(extend)
    print(aspect_ratio)

    cv2.imshow('image',img)
    cv2.waitKey(0)



my_image0 = 'Single shape.PNG'
my_image1 = 'Single shape r.png'
contourprop(my_image1)