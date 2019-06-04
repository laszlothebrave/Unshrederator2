import operator

import cv2
import numpy as np
from PIL import Image
from PIL.ImageShow import show

from Unshrederator2.AlphabetPrinter import AlphabetPrinter
from Unshrederator2.ArrayManipulation import show_from_array


def recognize_letter(image):


    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    dictionary = {}

    for letter in AlphabetPrinter.images.keys():
        template = AlphabetPrinter.images[letter]
        # template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)
        templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        w, h = templateGray.shape[::-1]
        res = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        threshold = 0.7
        # print(max_val)
        dictionary[letter] = max_val

    return max(dictionary.items(), key=operator.itemgetter(1))[0]
