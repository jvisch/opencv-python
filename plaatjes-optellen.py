import cv2 as cv

img1 = cv.imread('./ml.png')
img2 = cv.imread('./opencv-logo.png')
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
cv.imshow("img1", img1)
cv.imshow("img2", img2)
cv.waitKey(0)

# height = img1.rows
# width = img1.cols
height, width = img1.shape[:2]
a = img1.shape
dim = (width, height)
  
# resize image
img2 = cv.resize(img2, dim, interpolation = cv.INTER_AREA)

dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.imshow("opgeteld", cv.add(img1, img2))
cv.imshow("+", img1 + img2)
cv.waitKey(0)

cv.destroyAllWindows()
