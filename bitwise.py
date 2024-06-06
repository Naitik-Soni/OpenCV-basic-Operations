# Functions for Bitwise operators between images

import numpy as np
import cv2 as cv


def bitAnd():
    blank = np.zeros((500,500), dtype='uint8')

    rectangle = cv.rectangle(blank.copy(), (50,50), (450,450), 255, -1)
    circle = cv.circle(blank.copy(), (250,250), 250, 255, -1)

    return cv.bitwise_and(rectangle, circle)

def bitOr():
    blank = np.zeros((500,500), dtype='uint8')

    rectangle = cv.rectangle(blank.copy(), (50,50), (450,450), 255, -1)
    circle = cv.circle(blank.copy(), (250,250), 250, 255, -1)

    return cv.bitwise_or(rectangle, circle)

def bitXor():
    blank = np.zeros((500,500), dtype='uint8')

    rectangle = cv.rectangle(blank.copy(), (50,50), (450,450), 255, -1)
    circle = cv.circle(blank.copy(), (250,250), 250, 255, -1)

    return cv.bitwise_xor(rectangle, circle)

def bitNot():
    blank = np.zeros((500,500), dtype='uint8')

    rectangle = cv.rectangle(blank.copy(), (50,50), (450,450), 255, -1)
    circle = cv.circle(blank.copy(), (250,250), 250, 255, -1)

    return cv.bitwise_not(rectangle, circle)