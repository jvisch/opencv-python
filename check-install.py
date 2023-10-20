import cv2 as cv

# file = r"C:\Users\owwwt\OneDrive - HAN\Pictures\aapnootmies.jpg"
file = r"C:\temp\opencv-python\images\ballenbak.png"
img = cv.imread(file)

cv.imshow("Display window", img)
k = cv.waitKey(0)  # Wait for a keystroke in the window

b, g, r = cv.split(img)

x = b + g + r
x = x//3

img = cv.merge((x, x, x))
cv.imshow("knutsel", img)

cv.waitKey(0)
