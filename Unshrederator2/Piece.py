from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import list_supported_metadatas, get_metadata


class Piece:
    def __init__(self):
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def show_piece(self):
        print("This is piece")
