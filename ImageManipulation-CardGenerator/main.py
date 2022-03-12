from TemplateGenerator import Template

if __name__ == '__main__':
    source_image_path = "photos\\8.jpg"
    template = Template("photos/NRC_Sample.jpg")
    font = "fonts/Pyidaungsu-2.5_Regular.ttf"
    template.add_image(image=source_image_path, prepare_size=(165, 190),
                       paste_image_location=(25, 75, 190, 265))
    template.write_text(location=(315, 84), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=20, font_color="blue")
    template.write_text(location=(315, 130), text="ဟန်ဇော်ငြိမ်း",
                        font_style=font,
                        size=20, font_color="blue")
    template.write_text(location=(315, 175), text="နေရှင်နယ်ဆိုက်ဘာစီးတီး",
                        font_style=font,
                        size=20, font_color="blue")
    template.write_text(location=(315, 222), text="ကဆုန်လဆန်း ၁၀ ရက် ၁၃၆၄",
                        font_style=font,
                        size=20, font_color="blue")
    result = template.save("cards\\8.jpg")
    print("Image Savae Successfully : ", result)
