# 功能3：两个图片叠加
import cv2
import numpy as np
'''
cv2.addWeighted(src1,alpha,src2,beta,gamma)

src1:第一幅图像
alpha:系数1
src2:第二幅图像
beta:系数2
gamma:亮度调节
图像融合=图像1系数1+图像2系数2+亮度调节

'''
img = cv2.imread('result.png')
d=cv2.imread('white_bg.png')
result=cv2.addWeighted(img,0.5,d,0.5,0.5)
cv2.imshow('img',img)
cv2.imshow('d',d)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destoryAllWindows()

