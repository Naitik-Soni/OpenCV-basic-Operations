# Function for detecting countours

import cv2 as cv
import numpy as np

def findCounters(img, threshold):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    blank = np.zeros(img.shape, dtype='uint8')

    # We can use canny with blur image instead of using threshold
    ret, thresh = cv.threshold(gray, threshold[0], threshold[1], cv.THRESH_BINARY)

    counters, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)   

    cv.drawContours(blank, counters, -1, (0,0,255), 2)

    return blank