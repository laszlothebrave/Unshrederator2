import cv2
import numpy as np


class Piece:
    def __init__(self):
        self.img = None
        self.path = None

    def set_img(self, img):
        self.img = img

    def set_img_from_path(self, path):
        self.path = path
        self.img = cv2.imread(self.path, 0)

    def show(self):
        cv2.imshow(self.path, self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def create_empty_piece(self):
        # Create a black image
        self.img = np.zeros((512, 512, 3), np.uint8)

        # Draw a diagonal blue line with thickness of 5 px
        self.img = cv2.line(self.img, (0, 0), (511, 511), (255, 0, 0), 5)
        self.img = cv2.rectangle(self.img, (384, 0), (510, 128), (0, 255, 0), 3)

        pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        self.img = cv2.polylines(self.img, [pts], True, (0, 255, 255))


def main():
    # piece = Piece()
    # piece.set_img_from_path('../resources/examples/piece.png')
    # piece.show()
    # piece2 = Piece()
    # piece2.set_img_from_path('../resources/examples/piece_png.png')
    # piece2.show()
    piece3 = Piece()
    piece3.create_empty_piece()
    piece3.show()


if __name__ == "__main__":
    main()
