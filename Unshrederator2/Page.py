from PIL import Image, ImageDraw, ImageFont

from Unshrederator2.ImageText import ImageText


class Page:
    def __init__(self, text):
        self.text = text.replace('\r', "")
        self.image = None

        img = Image.new('RGBA', (2480 , 3508), color=(255, 255, 255, 255))
        # 140, 254 + 60
        font = ImageFont.truetype('resources/LibreBaskerville-Regular.ttf', 50)
        d = ImageDraw.Draw(img)
        d.multiline_text((140, 254), self.text, font=font, fill=(0, 0, 0), spacing = 10)
        print(self.text)
        img.save('page.png')

        font = 'resources/LibreBaskerville-Regular.ttf'
        color = (50, 50, 50)
        img = ImageText((2480 , 3508), background=(255, 255, 255, 255))  # 200 = alpha

        img.write_text_box((140, 254), self.text, box_width=2200, font_filename=font,
                           font_size=40, color=color)

        img.save('sample-imagetext.png')

