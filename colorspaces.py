# Functions for applyting different colors transformation

import cv2 as cv
import numpy as np

def toGray(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def toHSV(img):
    return cv.cvtColor(img, cv.COLOR_BGR2HSV)

def toLAB(img):
    return cv.cvtColor(img, cv.COLOR_BGR2Lab)

def toRGB(img):
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)