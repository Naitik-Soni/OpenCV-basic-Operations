# Functions for applying different code in images

import cv2 as cv
import numpy as np

def simpleThresh(img, low=150, high=255):
    return cv.threshold(img, low, high, cv.THRESH_BINARY)[1]

def simpleThreshInv(img, low=150, high=255):
    return cv.threshold(img, low, high, cv.THRESH_BINARY_INV)[1]

def adaptiveThresh(img, c=3, bsize=7):
    return cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, bsize, c)