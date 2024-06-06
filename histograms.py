# Function for displaying histogram of image

import cv2 as cv
import matplotlib.pyplot as plt

def showHist(image, mask=None):
    histogram = cv.calcHist([image], [0], mask, [256], [0, 256])

    plt.plot(histogram)
    plt.show()