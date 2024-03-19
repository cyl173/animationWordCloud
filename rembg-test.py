# 功能1：去除背景
import rembg
import numpy as np
from PIL import Image
import cv2 as cv
import os
def remove_bg():
    # Load the input image
    input_image = Image.open('test_img/image_test2.jpg')

    # Convert the input image to a numpy array
    input_array = np.array(input_image)

    # Apply background removal using rembg
    output_array = rembg.remove(input_array)

    # Create a PIL Image from the output array
    output_image = Image.fromarray(output_array)

    # Save the output image
    output_image.save('rembg-result.png')

    # add white background
    im = Image.open('rembg-result.png')
    x,y = im.size 
    try: 
        # 填充白色背景
        p = Image.new('RGBA', im.size, (255,255,255))
        p.paste(im, (0, 0, x, y), im)
        p.save('white_bg.png')
    except Exception as exc:
        print(exc)

def PNG_JPG():
    img = cv.imread('white_bg.png', 0)
    w, h = img.shape[::-1]
    infile = 'white_bg.png'
    outfile = os.path.splitext(infile)[0] + ".jpg"
    img = Image.open(infile)
    #img = img.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=70)
            #os.remove(PngPath)
        else:
            img.convert('RGB').save(outfile, quality=70)
            #os.remove(PngPath)
        return outfile
    except Exception as e:
        print("PNG转换JPG 错误", e)

remove_bg()
PNG_JPG()