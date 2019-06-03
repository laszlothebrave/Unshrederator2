from random import shuffle


class Shreder:
    def __init__(self):
        pass

    def shred(self, bin):
        pieces = []
        for book in bin.books:
            for page in book.pages:
                pieces.extend(self.shred_single_page(page))
        shuffle(pieces)
        return pieces

    def shred_single_page(self, page):
        pieces = []
        pieces.append(page)
        return pieces


