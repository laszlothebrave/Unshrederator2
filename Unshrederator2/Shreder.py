from random import shuffle


class Shreder:
    def __init__(self):
        pass

    def shred(self, bin):
        pieces = []
        pieces.extend(bin.get_pieces(self))
        shuffle(pieces)
        return pieces

    def shred_single_page(self, page):
        pieces = []
        pieces.append(page.copy())
        return pieces


