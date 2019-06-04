from PIL import Image
from PIL.ImageShow import show


def show_from_array(array):
    img = Image.fromarray(array, 'RGB')
    show(img)