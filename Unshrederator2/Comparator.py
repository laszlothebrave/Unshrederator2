from PIL import Image
from cv2.cv2 import imwrite, imread

from Unshrederator2.LetterReconizer import recognize_letter


def compare():
    img = imread('resources/alphabet/74.png')
    for i in range(80):
        img_croped = img[0:80-i, 0:80]
        print(recognize_letter(img_croped))

