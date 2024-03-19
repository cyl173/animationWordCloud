# 所有代码集合
import jieba
import wordcloud
import jieba.analyse
from PIL import Image
import numpy as np
import cv2

import rembg
import numpy as np
from PIL import Image
import cv2 as cv
import os
from PIL import Image
import numpy as np
import cv2
import cv2
import numpy as np

# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import imageio

def word_cloud(img_path,keyword_path):
    #获取图片大小
    img = Image.open(img_path)
    imgSize = img.size  #大小/尺寸
    width_img = img.width       #图片的宽
    height_img = img.height      #图片的高
    f_img = img.format      #图像格式
    
    # 构建并配置词云对象w，注意要加scale参数，提高清晰度
    mk = imageio.imread(img_path)#形状提取
    w = wordcloud.WordCloud(mask=mk)
    w = wordcloud.WordCloud(width=width_img,
                            height=height_img,
                            background_color='white',#背景颜色
                            font_path='msyh.ttc',#中文支持
                            mask=mk,#词云图自定义形状
                            scale=1,
                            stopwords={"我","的","了","他","都","你","对",
                                    "让","是","这","还","才","吧","不",
                                    "而","也","只是","就是","在","上",
                                    "无法","我们","什么","会","有","这个",
                                    "一个","这样","这么","就","不要","因为",
                                    "个","要","把"},#屏蔽无关词
                            contour_color='steelblue')
    
    # 对来自外部文件的文本进行中文分词，得到string
    f = open(keyword_path,encoding='utf-8')
    txt = f.read()
    #txtlist = jieba.lcut(txt)
    #txtlist=jieba.analyse.textrank(txt, topK=40, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
    txtlist=jieba.analyse.textrank(txt, topK=100, withWeight=False)
    string = " ".join(txtlist)
    print(string)

    # 将string变量传入w的generate()方法，给词云输入文字
    w.generate(string)
    # 将词云图片导出到当前文件夹
    w.to_file('wordcloud.png')
    return 'wordcloud.png'

def remove_bg(img_path):
    # Load the input image
    input_image = Image.open(img_path)

    # Convert the input image to a numpy array
    input_array = np.array(input_image)
    # Apply background removal using rembg
    output_array = rembg.remove(input_array)
    # Create a PIL Image from the output array
    output_image = Image.fromarray(output_array)
    # Save the output image
    output_image.save('remove_bg.png')

    # add white background
    im = Image.open('remove_bg.png')
    x,y = im.size 
    try: 
        # 填充白色背景
        p = Image.new('RGBA', im.size, (255,255,255))
        p.paste(im, (0, 0, x, y), im)
        p.save('remove_bg.png')
    except Exception as exc:
        print(exc)
    return "remove_bg.png"

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

def picadd(img_path,wordcloud_path):
    image = cv2.imread(img_path)
    wordcloud=cv2.imread(wordcloud_path)
    result=cv2.addWeighted(image,0.5,wordcloud,0.5,0.5)
    cv2.imshow('image',image)
    cv2.imshow('wordcloud',wordcloud)
    cv2.imshow('result',result)
    cv2.waitKey(0)
    cv2.destoryAllWindows()
    cv2.imwrite('result.png', result)
    return 'result.png'
    
if __name__ == '__main__':
    img_path="image.png"
    keyword_path="keyword.txt"
    print("背景是否为白色纯色背景，如果不是，请输入no，如果是，请输入yes：")
    is_white_bg=input()
    if is_white_bg=="no":
        img_path=remove_bg()
        print("背景已经去除，已经生成白色背景图片。\n请查看同级文件夹的remove_bg.png是否符合要求。\n如果不符合，您可以：\n1.使用PS或者procreate等其他工具自行处理背景；\n2.替换符合要求的照片。\n并再次运行程序。\n")
    elif is_white_bg=="yes":
        pass
    else:
        print("输入错误，请输入yes或者no。")
    wordcloud_path=word_cloud(img_path,keyword_path)
    #PNG_JPG()
    re_path=picadd(img_path,wordcloud_path)
    print("已经生成图片，请查看同级文件夹的%s图片。",re_path)