from TemplateGenerator import Template

if __name__ == '__main__':
    source_image_path = "photos\\8.jpg"
    template = Template("photos/NRC_Sample.jpg")
    font = "fonts/Pyidaungsu-2.5_Regular.ttf"
    template.write_text(location=(225, 41), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(225,63), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(225, 83), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(225, 105), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(225, 125), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(225, 145), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(180, 168), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(320, 168), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(270, 190), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(55, 216), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    template.write_text(location=(55, 236), text="၁၂၃၄၅၆၇၈၉၀",
                        font_style=font,
                        size=12, font_color="blue")
    result = template.save("cards\\nrc.jpg")
    print("Image Savae Successfully : ", result)
