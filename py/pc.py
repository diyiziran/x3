#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#爬网页新闻
#

import urllib2
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

url='http://news.baidu.com/'
content=urllib2.urlopen(url).read()

soup=BeautifulSoup(content,from_encoding='utf-8')

hotNews=soup.find_all('ul',{'class','ulist focuslistnews'})[0].find_all('li')

for i in hotNews:
	print i.a.text
	print i.a['href']



from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
bar.render()    # 生成本地 HTML 文件