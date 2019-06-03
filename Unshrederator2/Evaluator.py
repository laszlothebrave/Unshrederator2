class Evaluator:
    def __init__(self):
        self.original_bin = None

    def set_original_bin(self, original_bin):
        self.original_bin = original_bin
        print('Bin set')

    def evaluate_page(self, original_page, recreated_page):
        original_page_split = original_page.split()
        original_page_len = len(original_page_split)
        recreated_page_split = recreated_page.split()
        recreated_page_len = len(recreated_page.split())
        recreated_score = 0

        for word in recreated_page.split():
            if word in original_page:
                recreated_score += 1

        score = (recreated_score / original_page_len) * 0.75

        recreated_score = 0
        for word in recreated_page_split:
            if recreated_page_split[recreated_page_split.index(word) + 1] in \
            original_page_split[original_page_split.index(word):]:
                recreated_score += 1

        score = (recreated_score / (recreated_page_len - 1)) * 0.25

        return score

    def evaluate_book(self, original, recreated):
        score = 0
        original_split = original.split()
        recreated_split = recreated.split()
        original_len = len(original_split)
        # recreated_len = len(recreated_split)

        for page in recreated_split:
            if recreated_split[recreated_split.index(page) + 1] in original_split[original_split.index(page):]:
                score += 1

        return score / original_len

    def evaluate_bin(self, recreated):
        print ('Bin evaluated')

