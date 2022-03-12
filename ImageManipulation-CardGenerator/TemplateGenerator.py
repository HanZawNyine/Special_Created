import pandas as pd
from PIL import Image, ImageDraw, ImageFont


class Template:
    def __init__(self, template_path):
        self.template = Image.open(template_path)

    def write_text(self, location: tuple, text, font_style=None, size=12, font_color="black"):
        draw = ImageDraw.Draw(self.template)
        font=None
        if font_style:
            font = ImageFont.truetype(font_style, size=size)
        draw.text(location, str(text), font=font, fill=font_color)

    def add_image(self, image, prepare_size: tuple, paste_image_location: tuple):
        pic = Image.open(image).resize(prepare_size, Image.ANTIALIAS)
        self.template.paste(pic, paste_image_location)

    def save(self, save_path):
        self.template.save(save_path)
        return save_path


if __name__ == '__main__':
    source_image_path = "photos\\1.jpg"
    template = Template("photos/template.png")
    template.add_image(image=source_image_path, prepare_size=(165, 190), paste_image_location=(25, 75, 190, 265))
    template.write_text(location=(315, 84), text="1111111111111",font_style="OpenSans-Semibold.ttf",size=20,font_color="blue")
    template.write_text(location=(315, 130), text="1111111111111",font_style="OpenSans-Semibold.ttf",size=20,font_color="blue")
    template.write_text(location=(315, 175), text="1111111111111",font_style="OpenSans-Semibold.ttf",size=20,font_color="blue")
    template.write_text(location=(315, 222), text="1111111111111",font_style="OpenSans-Semibold.ttf",size=20,font_color="blue")
    result = template.save("cards\\1.jpg")
    print("Image Savae Successfully : ", result)
