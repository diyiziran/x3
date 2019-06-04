#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:12:16 2018

@author: zhengjt
"""
#本程序按顺序完成四件工作：
#1，读入文件
#2，分词
#3，分词结果写到excel文件
#4，制作词云

from os import path
from PIL import Image,ImageSequence
import numpy as np
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from openpyxl import load_workbook
from openpyxl import Workbook

#1，读入文件
with open('xykt.txt',mode='r') as f:
    mytext=f.read()
f.close()

#2，分词
##计算并输出词频
sgtxt=jieba.cut(mytext)
count={}    #创建字典
for word in sgtxt:
    if len(word)==1:  #忽略单字
        continue
    else:
        count[word]=count.get(word,0)+1
items=list(count.items())   #转换成列表
items.sort(key=lambda x:x[-1],reverse=True)


#3，分词结果写到excel文件
filename="sg_result.xlsx"
wb = load_workbook(filename)
sheet = wb.active
#sheet = wb.get_sheet_by_name("sheet1")
sheet.title='分词结果'
#写到excel文件
for i in range(len(items)):
    sheet["A%d" % (i+1)],sheet["B%d" % (i+1)]=items[i]

wb.save(filename)    

    
#4，制作词云
#
sgtxt=jieba.cut(mytext)
wl_space_split= " ".join(sgtxt)
#wl_space_split=sgtxt
#导入背景图
backgroud_Image = plt.imread('gf.jpg') 
stopwords = STOPWORDS.copy()
#可以加多个屏蔽词
stopwords.add("通过")
stopwords.add("实现")
stopwords.add("提供")
stopwords.add("进行")
stopwords.add("目前")
stopwords.add("情况")
stopwords.add("开展")
stopwords.add("对于")
stopwords.add("利用")
stopwords.add("课题")
stopwords.add("工作")
stopwords.add("数据")
stopwords.add("分析")




#设置词云参数 
#参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状 
image= Image.open('gf.jpg')
graph = np.array(image)

wc = WordCloud(width=1024,height=768,background_color='white',
    font_path='simhei.ttf',#黑体字
    stopwords=stopwords,max_font_size=400,
    random_state=50,mask=graph)
wc.generate_from_text(wl_space_split)
img_colors= ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
#plt.axis('off')#不显示坐标轴  
plt.show()
#保存结果到本地
wc.to_file('xie_zheng.jpg')