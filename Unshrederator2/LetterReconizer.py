import operator

import cv2
import numpy as np
from PIL import Image
from PIL.ImageShow import show

from Unshrederator2.AlphabetPrinter import AlphabetPrinter
from Unshrederator2.ArrayManipulation import show_from_array


def recognize_letter(image):

    #image = Image.fromarray(image, 'RGB')
    #cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    #imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    dictionary = {}

    for letter in AlphabetPrinter.images.keys():
        template = AlphabetPrinter.images[letter]
        #template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)
        templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        w, h = templateGray.shape[::-1]
        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.85
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 2)
        cv2.imwrite('res.png', image)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        dictionary[letter] = max_val

    return max(zip(dictionary.values(), dictionary.keys()))[1]
