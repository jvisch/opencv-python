import cv2 as cv
import numpy as np

rgb = np.uint8([[[255, 0, 0]]])
hsv = cv.cvtColor(rgb, cv.COLOR_RGB2HSV)

print(f'{rgb} := {hsv}')