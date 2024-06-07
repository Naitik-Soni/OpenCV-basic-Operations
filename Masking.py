# Functions for masking of image

import cv2 as cv
import numpy as np

def circularMask(img, center=None, radius=None):
    blank = np.zeros(img.shape[:2], dtype='uint8')

    if center is None:
        center = (img.shape[1]//2, img.shape[0]//2)
    if radius is None:
        radius = min(img.shape[1]//2, img.shape[0]//2)

    mask = cv.circle(blank, center, radius, 255, -1)

    return cv.bitwise_and(img, img, mask=mask)

def rectMask(img, start=None, stop=None):
    blank = np.zeros(img.shape[:2], dtype='uint8')

    if start is None:
        start = (img.shape[1]//2, img.shape[0]//2)
    if stop is None:
        stop = min(img.shape[1]//2, img.shape[0]//2)

    mask = cv.rectangle(blank, start, stop, 255, -1)

    return cv.bitwise_and(img, img, mask=mask)