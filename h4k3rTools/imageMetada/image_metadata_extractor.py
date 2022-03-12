from PIL import Image
from PIL.ExifTags import TAGS

class imageMetaData:
    def __init__(self,imageName):
        self.imageName = imageName

    def extract(self):
        #imagename = "image.jpg"  # sys.argv[1]
        image = Image.open(self.imageName)

        # extract EXIF data
        exifdata = image.getexif()

        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")

if __name__ == '__main__':
    imageMetaData = imageMetaData('image.jpg')
    imageMetaData.extract()