import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def do_nothing(value):
    pass


WINDOW_ORIGINAL = 'original'
WINDOW_EDGES = 'canny edges'

TRACKBAR_MIN = 'tresh hold min'
TRACKBAR_MAX = 'tresh hold max'

cv.namedWindow(WINDOW_ORIGINAL)

cv.createTrackbar(TRACKBAR_MIN, WINDOW_ORIGINAL, 100, 255, do_nothing)
cv.createTrackbar(TRACKBAR_MAX, WINDOW_ORIGINAL, 200, 255, do_nothing)

camera = cv.VideoCapture(0)
while True:
    found, frame = camera.read()
    if found:
        cv.imshow(WINDOW_ORIGINAL, frame)

        min = cv.getTrackbarPos(TRACKBAR_MIN, WINDOW_ORIGINAL)
        max = cv.getTrackbarPos(TRACKBAR_MAX, WINDOW_ORIGINAL)
        canny = cv.Canny(frame, min, max)
        cv.imshow(WINDOW_EDGES, canny)

        k = cv.pollKey()
        if k == 27:  # ESC
            cv.destroyAllWindows()
            break
    else:
        print("no frame")
        import time
        time.sleep(0.2)


cv.waitKey()