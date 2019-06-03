from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

from Unshrederator2.Page import Page


class Book:
    def __init__(self, book_number = 2701):
        self.text = strip_headers(load_etext(book_number))
        # print(list_supported_metadatas())  # prints (u'author', u'formaturi', u'language', ...)
        # print(get_metadata('title', 2701))  # prints frozenset([u'Moby Dick; Or, The Whale'])
        # print(get_metadata('author', 2701))  # prints frozenset([u'Melville, Hermann'])
        # print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'
        self.pages = []
        self.print_book()

    def print_book(self):
        lines = self.text.split('\n')
        tmp = ""
        counter = 0
        for line in lines:
            tmp = tmp + line + "\n"
            counter += 1
            print(counter)
            if counter == 50:
                self.pages.append(self.create_page(tmp))
                tmp = ""
                counter = 0

    def create_page(self, text):
        return Page(text)
