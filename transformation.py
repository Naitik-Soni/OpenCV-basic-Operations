# Functions for applying different transformations like rescaling etc. in images

import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def toGrayScale(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def blurImage(img, blur_size = 3):
    return cv.GaussianBlur(img, (blur_size, blur_size), cv.BORDER_DEFAULT)

def detectEdges(img, base, top):
    return cv.Canny(img, base, top)

def dialetAndErode(img, size=5, iterations=3):
    dialeted = cv.dilate(img, (size, size), iterations)
    return cv.erode(dialeted, (size, size), iterations)