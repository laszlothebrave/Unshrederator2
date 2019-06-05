from PIL import Image
from PIL.ImageShow import show
from cv2.cv2 import imwrite, imread


def show_from_array(array):
    img = Image.fromarray(array, 'RGB')
    show(img)

def make_image_from_array(matrix):
    image = Image.fromarray(matrix, 'RGB')
    imwrite('temp.png', matrix)
    return imread('temp.png')
