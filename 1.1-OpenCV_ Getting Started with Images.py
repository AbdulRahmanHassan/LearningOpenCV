import cv2
from matplotlib import pyplot as plt

def imread(image):
    img =cv2.imread(image,cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imwrite(image):
    img = cv2.imread(image, 0)
    cv2.imshow('image', img)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'):  # wait for 's' key to save and exit
        cv2.imwrite('messigray.png', img)
        cv2.destroyAllWindows()

def Matplotlip(image):
    img = cv2.imread(image, 0)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

my_image = '16114722_936647449799246_7088051333553256518_n.jpg'
imread(my_image)