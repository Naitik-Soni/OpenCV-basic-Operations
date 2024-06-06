# Functions for applying types of blur filter to smooth the image

import cv2 as cv
import numpy as np

def averageBlue(img, size):
    return cv.blur(img, (size, size))

def gaussBlur(img, size):
    return cv.GaussianBlur(img, (size, size), 0)

def medianBlur(img, size):
    return cv.medianBlur(img, size)