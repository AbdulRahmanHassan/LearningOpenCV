import cv2
import numpy as np

def Moment(img):
    img = cv2.imread(img)
    Canny = cv2.Canny(img,179,239)
    contours, hierarchy = cv2.findContours(Canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,contours,-1,(0,0,255),2)
    cnt = contours[0]
    moment = cv2.moments(cnt)
    print(moment)
    Cx = moment['m10']/moment['m00']
    Cy = moment['m01']/moment['m00']
    cv2.circle(img,(int(Cx),int(Cy)),1,(0,0,255))
    print ('Cg = ({},{})'.format(Cx,Cy))
    cv2.imshow('Canny',Canny)
    cv2.imshow('img',img)
    cv2.waitKey(0) & 0xFF


def ContourArea(img):
    img = cv2.imread(img)
    Canny = cv2.Canny(img,179,239)
    contours, hierarchy = cv2.findContours(Canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img,contours,-1,(0,0,255),2)
    cnt = contours[0]
    moment = cv2.moments(cnt)
    Cx = moment['m10']/moment['m00']
    Cy = moment['m01']/moment['m00']
    Area = cv2.contourArea(cnt)
    cv2.putText(img,'Area = {}'.format(Area),(int(Cx)-60,int(Cy)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.imshow('Canny',Canny)
    cv2.imshow('img',img)
    cv2.waitKey(0) & 0xFF


def Perimeter(img):
    im = cv2.imread(img)
    edges = cv2.Canny(im,130,200)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    perimeter = cv2.arcLength(cnt,True)
    return perimeter


def Approx(img):
    im = cv2.imread(img)
    edges = cv2.Canny(im,130,200)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    epsilon = 0.03*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    return len(approx)


def Convex(img):
    im = cv2.imread(img)
    edges = cv2.Canny(im,130,200)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    print(cv2.isContourConvex(cnt))
    hull = cv2.convexHull(cnt,returnPoints=False)
    print(hull)

my_images0= 'Shapes.PNG'
my_images1= 'Single shape.PNG'
my_images2= 'Single shape 2.PNG'
my_images3= 'Single shape 3.png'

Convex(my_images2)

