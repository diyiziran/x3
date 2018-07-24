import pickle
from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

comment = []
with open('data.txt',mode='r',encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if len(row.split(',')) == 5:
            comment.append(row.split(',')[4].replace('\n',''))
jieba.add_word('彭于晏')   #自定义词

#分词
comment_after_split = jieba.cut(str(comment),cut_all=False)

wl_space_split= " ".join(comment_after_split)
#导入背景图
#backgroud_Image = plt.imread('1.jpg') 
stopwords = STOPWORDS.copy()
#可以加多个屏蔽词
stopwords.add("电影")
stopwords.add("一部")
stopwords.add("一个")
stopwords.add("没有")
stopwords.add("什么")
stopwords.add("有点")
stopwords.add("这部")
stopwords.add("这个")
stopwords.add("不是")
stopwords.add("真的")
stopwords.add("感觉")
stopwords.add("觉得")
stopwords.add("还是")


#设置词云参数 
#参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状 
wc = WordCloud(width=1024,height=768,background_color='white',
    font_path='simhei.ttf',#黑体字
    stopwords=stopwords,max_font_size=400,
    random_state=50)
wc.generate_from_text(wl_space_split)
#img_colors= ImageColorGenerator(backgroud_Image)
#wc.recolor(color_func=img_colors)
plt.imshow(wc)
#plt.axis('off')#不显示坐标轴  
plt.show()
#保存结果到本地
wc.to_file('xie_zheng.jpg')