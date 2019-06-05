from PIL import Image
from cv2.cv2 import imwrite, imread

from Unshrederator2.AlphabetPrinter import AlphabetPrinter
from Unshrederator2.ArrayManipulation import show_from_array
from Unshrederator2.LetterReconizer import recognize_letter


def compare():
    dictionary = {}
    for letter in AlphabetPrinter.alphabet:
        img = AlphabetPrinter.get_letter_image(letter)
        for i in range(80):
            img_croped = img[0:80, 0:80-i]
            result = recognize_letter(img_croped)
            print(i, result)
            if letter != result:
                show_from_array(img_croped)
                dictionary [letter] = 80-i-14
                break


