import numpy as np
import cv2 as cv

# im = cv.imread('test.jpg')
# assert im is not None, "file could not be read, check with os.path.exists()"

camera = cv.VideoCapture(0)
while True:
    found, im = camera.read()
    if found:
        im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        cv.imshow('gray', im)
        ret, thresh = cv.threshold(im, 127, 255, 0)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        im = cv.drawContours(im, contours, -1, (255,0,0), 3)
        cv.imshow('contours', im)
        cv.waitKey(1000)
    else:
        print('No capture')
        import time
        time.sleep(.2)