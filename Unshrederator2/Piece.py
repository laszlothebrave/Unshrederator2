import cv2
import base64
import numpy as np

from Unshrederator2.ArrayManipulation import show_from_array
from Unshrederator2.Letter import Letter


class Piece:
    def __init__(self, image):
        self.image = image
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.letters = []

    def show_piece(self):
        print("This is piece")

    def find_letter(self):
        with open(self.image, "rb") as imageFile:
            stri = base64.b64encode(imageFile.read())
        assert isinstance(stri, str)
        return self.find_letter_in_string(stri)

    def find_letter_in_string(self, scinek):
        return set(scinek)

    def recognize_consecutive_letters(self):
        # image = cv2.imread('resources/tiles/first.png')
        # template = cv2.imread('resources/alphabet/a.png')
        #
        #
        #
        # # resize images
        # image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        # template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)
        #
        # imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        #
        # result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF)
        # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # top_left = max_loc
        # h, w = templateGray.shape
        # bottom_right = (top_left[0] + w, top_left[1] + h)
        # cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 4)
        #
        # # Show result
        # cv2.imshow("Template", template)
        # cv2.imshow("Result", image)
        #
        # print (h, w)
        #
        # cv2.waitKey(0)
        image = cv2.imread('resources/tiles/first.png')
        template = cv2.imread('resources/alphabet/97.png')

        image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)

        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        w, h = templateGray.shape[::-1]

        res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0, 0, 0), 2)

        cv2.imwrite('res.png', image)

    def letters_pieces(self):
        image = cv2.imread('resources/tiles/first.png')
        #img2 = np.pad(image.copy(), ((200, 200), (200, 200), (0, 0)), 'edge')
        # call openCV with img2, it will set all the border pixels in our new pad with 0
        # now get rid of our border
        imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        imgray = cv2.bitwise_not(imgray)

        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cnt = contours[4]

        #image = img2[200:-200, 200:-200, :]

        for cont in contours:
            x, y, w, h = cv2.boundingRect(cont)
            if y > 10 & y < 50:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 1)
                self.letters.append(Letter(image[x:x + w, y:y + h]))

                show_from_array(image[y:y + h, x:x + w])
                # cv2.drawContours(image, [cnt], 0, (0, 255, 0), 3)
                print(self.letters[-1].letter)

                # cv2.drawContours(image, [cont], 0, (0, 255, 0), 3)
        cv2.imwrite('resources/tiles/first.png', image)
