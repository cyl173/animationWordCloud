# 导入词云制作库wordcloud和中文分词库jieba
import jieba
import wordcloud
import jieba.analyse
from PIL import Image
import numpy as np
import cv2

# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片
import imageio
mk = imageio.imread("test_img/image_test8.png")#形状提取
w = wordcloud.WordCloud(mask=mk)

file_path = 'white_bg.png'
img = Image.open(file_path)
imgSize = img.size  #大小/尺寸
width_img = img.width       #图片的宽
height_img = img.height      #图片的高
f_img = img.format      #图像格式
 
# 构建并配置词云对象w，注意要加scale参数，提高清晰度
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
f = open('关键字.txt',encoding='utf-8')
txt = f.read()
#txtlist = jieba.lcut(txt)
#txtlist=jieba.analyse.textrank(txt, topK=40, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
txtlist=jieba.analyse.textrank(txt, topK=100, withWeight=False)

string = " ".join(txtlist)
print(string)


# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file('result.png')
