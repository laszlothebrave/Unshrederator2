from PIL import Image, ImageFont, ImageDraw
from cv2.cv2 import imread


class AlphabetPrinter:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                '.', ':', ',', ';', '\'', '"', '(', '!', '?', ')', '+', '-', '*', '/', '=']
    images = {}

    def print_letter_to_file(letter):
        img = Image.new('RGBA', (80, 80), color=(255, 255, 255, 255))
        font = ImageFont.truetype('resources/LibreBaskerville-Regular.ttf', 50)
        d = ImageDraw.Draw(img)
        d.multiline_text((15, 15), letter, font=font, fill=(0, 0, 0), spacing=10)
        img.save('resources/alphabet/' + str(ord(letter)) + '.png')

    def print_alphabet_to_files():
        for letter in AlphabetPrinter.alphabet:
            AlphabetPrinter.print_letter_to_file(letter)

    def read_alphabet_from_files():
        for letter in AlphabetPrinter.alphabet:
            AlphabetPrinter.images[letter] = imread('resources/alphabet/' + str(ord(letter)) + '.png')

    def get_letter_image(letter):
        return imread('resources/alphabet/' + str(ord(letter)) + '.png')
