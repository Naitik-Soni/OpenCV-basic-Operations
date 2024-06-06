# Functions for detecting edges in image

import cv2 as cv
import numpy as np

def laplacian(img):
    lap = cv.Laplacian(img, cv.CV_64F)

    return np.unit8(np.absolute(lap))

def sobel(img):
    sx = cv.Sobel(img, cv.CV_64F, 1, 0)
    sy = cv.Sobel(img, cv.CV_64F, 0, 1)

    return (sx, sy)

def canny(img, low=150, high=255):
    return cv.Canny(img, low, high)