from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

from Unshrederator2.Page import Page


class Book:
    def __init__(self, book_number = 27011):
        self.text = strip_headers(load_etext(book_number)).strip()
        # print(list_supported_metadatas())  # prints (u'author', u'formaturi', u'language', ...)
        # print(get_metadata('title', 2701))  # prints frozenset([u'Moby Dick; Or, The Whale'])
        # print(get_metadata('author', 2701))  # prints frozenset([u'Melville, Hermann'])
        # print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'
        self.pages = []
        self.print_book(self.text)

    def print_book(self, text):
        self.pages.append(self.create_page("My first page"))
        # while (len(text)>0)
        #     self.pages.append(self.create_page(text[0:1000]))
        #     text = text[1000:]

    def create_page(self, text):
        return Page(text)
