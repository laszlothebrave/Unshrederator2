import cv2
import base64

class Piece:
    def __init__(self, image):
        self.image = image
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def show_piece(self):
        print("This is piece")

    def find_letter(self):
        with open(self.image, "rb") as imageFile:
            stri = base64.b64encode(imageFile.read())
        assert isinstance(stri, str)
        return self.find_letter_in_string(stri)

    def find_letter_in_string(self, scinek):
        return set(scinek)

    def find_with_patern_matching(self):
        image = cv2.imread('/resources/tiles/first.png')
        template = cv2.imread('/resources/alphabet/a.png')

        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # resize images
        image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5)
        result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        h, w = templateGray.shape
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 4)

        # Show result
        cv2.imshow("Template", template)
        cv2.imshow("Result", image)

        cv2.moveWindow("Template", 10, 50);
        cv2.moveWindow("Result", 150, 50);

        cv2.waitKey(0)