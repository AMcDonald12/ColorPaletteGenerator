from colorthief import ColorThief
from PIL import Image
import os

#lower image resolution for fast code execution
def lower_res(file):
    image = Image.open(file)
    image = image.convert('RGB')
    image.thumbnail((400, 400))
    image.save('low_res.jpeg')

#create ColorThief object and get palette
def get_palette():
    ct = ColorThief('low_res.jpeg')
    colors = 5
    palette = ct.get_palette(color_count=colors)

    #convert from rgb to hex code
    color_list = ['#%02x%02x%02x' % i for i in palette]

    return color_list

#cleanup temp file
def cleanup():
    try:
        os.remove('low_res.jpeg')
    except:
        pass