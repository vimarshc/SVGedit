import cv2
import numpy as np
from scipy import misc as s
import os
def forsvg(filename):
    i = cv2.imread(filename)
    im = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(i,175,255,cv2.THRESH_BINARY)
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.erode(thresh,kernel,iterations = 2)
    bit = cv2.bitwise_not(dilation)
    bits = cv2.resize(bit,(222, 222), interpolation = cv2.INTER_CUBIC)
    threshs = cv2.resize(dilation,(222, 222), interpolation = cv2.INTER_CUBIC)


    s.imsave("bit.jpg", bits)
    s.imsave("thresh.jpg", dilation)

    os.system('convert bit.jpg bit.bmp')
    os.system('convert thresh.jpg thresh.bmp')
    os.system('potrace -s bit.bmp')
    os.system('potrace -s thresh.bmp')
