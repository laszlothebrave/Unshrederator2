from Unshrederator2.ArrayManipulation import make_image_from_array
from Unshrederator2.LetterReconizer import recognize_letter


class Letter:

    def __init__(self, image):
        self.image = image.copy()
        self.letter = recognize_letter(make_image_from_array(image))


