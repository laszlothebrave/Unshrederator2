class Bin:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def add_books(self, books):
        self.book_list.extend(books)

    def mix(self):
        pass