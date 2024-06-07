# Functions made for advance transformations like rotating, translating and flipping the image

import cv2 as cv
import numpy as np

def translate(img, x, y):
    transmat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)

def rotate(img, angle, point=None):
    (height, width) = img.shape[:2]

    if point is None:
        point = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

def flip(img, by="h"):
    to = 1

    if by=="h":
        to=1
    elif by=="v":
        to=0
    elif by=="b":
        to=-1

    return cv.flip(img, to)