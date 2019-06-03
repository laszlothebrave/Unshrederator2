from PIL import Image, ImageFont, ImageDraw


class AlphabetPrinter:

    def __init__(self):
        pass

    def print(self, letter):
        img = Image.new('RGBA', (30, 50), color=(255, 255, 255, 255))
        font = ImageFont.truetype('resources/LibreBaskerville-Regular.ttf', 50)
        d = ImageDraw.Draw(img)
        d.multiline_text((0, 0), letter, font=font, fill=(0, 0, 0), spacing=10)
        img.save('resources/alphabet/' + letter + '.png')