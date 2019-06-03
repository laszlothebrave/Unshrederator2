from PIL import Image, ImageDraw, ImageFont

class Page:
    def __init__(self, text):
        self.text = text.replace('\r', "")
        self.image = None

        img = Image.new('RGBA', (2480 , 3508), color=(255, 255, 255, 255))
        font = ImageFont.truetype('resources/LibreBaskerville-Regular.ttf', 50)
        d = ImageDraw.Draw(img)
        d.multiline_text((140, 254), self.text, font=font, fill=(0, 0, 0), spacing = 10)
        img.save('page.png')

