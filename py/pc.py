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
