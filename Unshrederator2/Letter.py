from Unshrederator2.LetterReconizer import recognize_letter


class Letter:

    def __init__(self, image):
        self.image = image
        self.letter = recognize_letter(image)


