import cv2 as cv
import numpy as np

cv.samples.addSamplesDataSearchPath('images')
img_org = cv.imread(cv.samples.findFile('sudoku.png'))

WINDOW_SETTINGS = 'SETTINGS'
TRACKBAR_CANNY_MIN = 'canny min'
TRACKBAR_CANNY_MAX = 'canny max'
TRACKBAR_CANNY_APERTURE = 'canny aperture'
TRACKBAR_HOUGH_RHO = 'hough rho'
TRACKBAR_HOUGH_THETA = 'hough theta'
TRACKBAR_HOUGH_THRESHOLD = 'hough threshold'

NOTHING = lambda _ : None

cv.namedWindow(WINDOW_SETTINGS)
cv.createTrackbar(TRACKBAR_CANNY_MIN, WINDOW_SETTINGS, 50, 255, NOTHING)
cv.createTrackbar(TRACKBAR_CANNY_MAX, WINDOW_SETTINGS, 150, 255, NOTHING)
cv.createTrackbar(TRACKBAR_CANNY_APERTURE, WINDOW_SETTINGS, 0, 2, NOTHING)
cv.createTrackbar(TRACKBAR_HOUGH_RHO, WINDOW_SETTINGS, 1, 300, NOTHING)
cv.setTrackbarMin(TRACKBAR_HOUGH_RHO, WINDOW_SETTINGS, 1)
cv.createTrackbar(TRACKBAR_HOUGH_THETA, WINDOW_SETTINGS, 180, 360, NOTHING)
cv.setTrackbarMin(TRACKBAR_HOUGH_THETA, WINDOW_SETTINGS, 1)
cv.createTrackbar(TRACKBAR_HOUGH_THRESHOLD, WINDOW_SETTINGS, 100, 255, NOTHING)



while True:
    img = img_org.copy()
    cv.imshow(WINDOW_SETTINGS, img_org)

    canny_min = cv.getTrackbarPos(TRACKBAR_CANNY_MIN, WINDOW_SETTINGS)
    canny_max = cv.getTrackbarPos(TRACKBAR_CANNY_MAX, WINDOW_SETTINGS)
    canny_aperture = cv.getTrackbarPos(TRACKBAR_CANNY_APERTURE, WINDOW_SETTINGS) * 2 + 3

    hough_rho = cv.getTrackbarPos(TRACKBAR_HOUGH_RHO, WINDOW_SETTINGS)  / 10
    hough_theta = cv.getTrackbarPos(TRACKBAR_HOUGH_THETA, WINDOW_SETTINGS)
    hough_threshold = cv.getTrackbarPos(TRACKBAR_HOUGH_THRESHOLD, WINDOW_SETTINGS)
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, canny_min, canny_max, apertureSize=canny_aperture)
    lines = cv.HoughLinesP(edges, hough_rho, np.pi/hough_theta, hough_threshold,minLineLength=100, maxLineGap=10)
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    cv.imshow('gray', gray)
    cv.imshow('edges', edges)
    cv.imshow('result', img)
    
    if cv.pollKey() == 27:
        cv.destroyAllWindows()
        break

