class Evaluator:
    def __init__(self):
        self.original_bin = None

    def set_original_bin(self, original_bin):
        self.original_bin = original_bin
        print ('Bin set')

    def evaluate_page(self, original, recreated):
        pass

    def evaluate_book(self, original, recreated):
        pass

    def evaluate_bin(self, recreated):
        print ('Bin evaluated')

