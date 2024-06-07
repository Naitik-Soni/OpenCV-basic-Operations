# Function for displaying R,G,B Channel intensity of image

import cv2 as cv
import numpy as np

def displaySplitted(img):
    blank = np.zeros(img.shape[:2], dtype='uint8')

    b,g,r = cv.split(img)

    blue = cv.merge([b, blank, blank])
    green = cv.merge([blank, g, blank])
    red = cv.merge([blank, blank, r])

    # img = cv.merge([b,g,r])

    cv.imshow("RED", red)
    cv.imshow("GREEN", green)
    cv.imshow("BLUE", blue)

    cv.waitKey(0)