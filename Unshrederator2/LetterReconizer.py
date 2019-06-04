import cv2
import numpy as np
from Unshrederator2.AlphabetPrinter import AlphabetPrinter


def recognize_letter(image):


    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



    for letter in AlphabetPrinter.images.keys():
        template = AlphabetPrinter.images[letter]
        template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)
        templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        w, h = templateGray.shape[::-1]
        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        if res > threshold:
            return letter
