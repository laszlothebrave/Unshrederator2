from random import shuffle

import image_slicer
from PIL.ImageShow import show

from Unshrederator2.Piece import Piece


class Shreder:
    def __init__(self, pieces_number = 10):
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
        tiles = image_slicer.slice('page.png', self.pieces_number*self.pieces_number, save=False)
        for tile in tiles:
            pieces.append(Piece(tile.image))
        #show(pieces[int(self.pieces_number*self.pieces_number/2)+2].image)
        print(pieces[int(self.pieces_number * self.pieces_number / 2) + 2].find_with_patern_matching())
        return pieces


