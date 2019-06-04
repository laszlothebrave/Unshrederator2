from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

from Unshrederator2.Page import Page


class Book:
    def __init__(self, book_number=2701, first_page = 20, last_page=20):
        self.text = strip_headers(load_etext(book_number))
        # print(list_supported_metadatas())  # prints (u'author', u'formaturi', u'language', ...)
        # print(get_metadata('title', 2701))  # prints frozenset([u'Moby Dick; Or, The Whale'])
        # print(get_metadata('author', 2701))  # prints frozenset([u'Melville, Hermann'])
        # print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'
        self.pages = []
        self.first_page = first_page
        self.last_page = last_page
        self.print_book()

    def print_book(self):
        lines = self.text.split('\n')
        tmp = ""
        line_counter = 0
        page_counter = 0
        for line in lines:
            tmp = tmp + line + "\n"
            line_counter += 1
            if line_counter == 50:
                page_counter += 1
                line_counter = 0
                if page_counter >= self.first_page:
                    self.pages.append(self.create_page(tmp))
                if page_counter == self.last_page:
                    return
                tmp = ""


    def create_page(self, text):
        return Page(text)
