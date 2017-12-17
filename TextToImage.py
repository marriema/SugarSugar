import Image
import ImageDraw
import ImageFont

class TexttoImage(object):

    def __init__(self, text, dest):
        self.__text = text
        self.__dest =  dest
        
    def getSize(txt, font):
        testImg = Image.new('RGB', (1, 1))
        testDraw = ImageDraw.Draw(testImg)
        return testDraw.textsize(self.__text, font)

    def getImage():
        fontname = "Arial.ttf"
        fontsize = 11   
        text = self.__text

        colorText = "black"

        font = ImageFont.truetype(fontname, fontsize)
        width, height = getSize(text, font)
        img = Image.new('RGB', (width+4, height+4), colorBackground)
        d = ImageDraw.Draw(img)
        d.text((2, height/2), text, fill=colorText, font=font)
        d.rectangle((0, 0, width+3, height+3), outline=colorOutline)

        dest = self.__dest
        img.save(dest+"/image.png")
