from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import list_supported_metadatas, get_metadata

import base64

class Piece:
    def __init__(self):
        self.left = None
        self.right = None
        self.up = None
        self.down = None

    def show_piece(self):
        print("This is piece")

    def find_letter(self, scinek):
        with open(scinek, "rb") as imageFile:
            stri = base64.b64encode(imageFile.read())
        assert isinstance(stri, str)
        return self.find_letter_in_string(stri)

    def find_letter_in_string(self, scinek):
        return set(scinek)


