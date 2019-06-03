from random import shuffle


class Bin:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_pieces(self):
        pieces = []
        for book in self.books:
            pieces.extend(book.get_pieces())
        shuffle(pieces)
        return pieces

