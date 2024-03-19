# 功能2：根据图片大小生成纯色背景图
from PIL import Image
import numpy as np
import cv2

file_path = 'rembg-result.png'
 
img = Image.open(file_path)
imgSize = img.size  #大小/尺寸
width = img.width       #图片的宽
height = img.height      #图片的高
f = img.format      #图像格式
 
print(imgSize)
print(width, height, f)

color = (255, 255, 255) # color you want
arr = np.zeros((height,width, 3), dtype=np.uint8) # all-zero array
pic = color - arr
cv2.imwrite('white_bg.png', pic)

