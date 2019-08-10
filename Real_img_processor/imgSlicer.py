import cv2
import numpy as np


class ImgSlicer:
    def __init__(self, img_path):
        self.img_path = img_path
        self.img = cv2.imread(img_path, 0)
        self.pieces = []

    def slice(self):
        # ret, self.img = cv2.threshold(self.img, 127, 255, cv2.THRESH_BINARY)
        # self.img = cv2.GaussianBlur(self.img, (3, 3), 0)
        self.img = self.img[100:300,200:600]
        cv2.imshow('title', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    imgSlicer = ImgSlicer('../resources/examples/piece_png.png')
    imgSlicer.slice()
    for piece in imgSlicer.pieces:
        piece.show()


if __name__ == "__main__":
    main()