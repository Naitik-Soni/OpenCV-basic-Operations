# Functions for detecting faces in image

import cv2 as cv

def detectFaces(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier("haar_cascade_face.xml")

    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    print(len(faces))

    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

    return img