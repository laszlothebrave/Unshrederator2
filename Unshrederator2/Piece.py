from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

class Piece:
    def __init__(self):
        pass

    def show_piece(self):
        print("This is piece")


        text = strip_headers(load_etext(2701)).strip()
        print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'