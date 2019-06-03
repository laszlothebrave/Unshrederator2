from gutenberg.acquire import set_metadata_cache
from gutenberg.acquire.metadata import SqliteMetadataCache, get_metadata_cache

from Unshrederator2.Bin import Bin
from Unshrederator2.Book import Book
from Unshrederator2.Evaluator import Evaluator
from Unshrederator2.Page import Page
from Unshrederator2.Piece import *
from textblob import TextBlob

from Unshrederator2.Shreder import Shreder
from Unshrederator2.Unshrederator import Unshrederator


def main():
    original_bin = Bin()
    book = Book(27011)
    original_bin.add_book(book)

    shreder = Shreder()
    pieces = shreder.shred(bin)

    unshrederator = Unshrederator()
    recreated_bin = unshrederator.recreate(pieces)

    evaluator = Evaluator()
    evaluator.set_original_bin(original_bin)
    evaluator.evaluate_bin(recreated_bin)

main()

