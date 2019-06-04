from cv2.cv2 import imread

from Unshrederator2.AlphabetPrinter import AlphabetPrinter
from Unshrederator2.Bin import Bin
from Unshrederator2.Book import Book
from Unshrederator2.Evaluator import Evaluator
from Unshrederator2.LetterReconizer import recognize_letter
from Unshrederator2.Shreder import Shreder
from Unshrederator2.Unshrederator import Unshrederator


def main():
    original_bin = Bin()
    book = Book(2701)
    original_bin.add_book(book)

    shreder = Shreder()
    pieces = shreder.shred(original_bin)

    unshrederator = Unshrederator()
    recreated_bin = unshrederator.recreate(pieces)

    evaluator = Evaluator()
    evaluator.set_original_bin(original_bin)
    evaluator.evaluate_bin(recreated_bin)


AlphabetPrinter.read_alphabet_from_files()
main()
