from random import shuffle

import image_slicer
from PIL.ImageShow import show


class Shreder:
    def __init__(self, pieces_number = 25):
        self.pieces_number = pieces_number

    def shred(self, bin):
        pieces = []
        for book in bin.books:
            for page in book.pages:
                pieces.extend(self.shred_single_page(page))
        shuffle(pieces)
        return pieces

    def shred_single_page(self, page):
        pieces = []
        pieces.extend(image_slicer.slice('page.png', self.pieces_number, save=False))
        show(pieces[20].image)
        return pieces


