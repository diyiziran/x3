#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Spyder Editor

This is a temporary script file.
"""

import json
import urllib3

#利用urllib2获取网络数据
http = urllib3.PoolManager()
url ="http://caipiaojieguo.com/api/lottrey?biaoshi=ssq&format=json&rows=10"        
r = http.request('GET', url)
value=json.loads(r.data)
rootlist=value.keys()
for rootkey in rootlist:
    print(rootkey)
datas=value['data']


dictObj = {
	'andy':{
		'age': 23,
		'city': 'shanghai',
		'skill': 'python'
	},
	'william': {
		'age': 33,
		'city': 'hangzhou',
		'skill': 'js'
	}
}
 
#写入json文件
jsObj = json.dumps(dictObj)
 
fileObject = open('jsonFile.json', 'w')
fileObject.write(jsObj)
fileObject.close()

#读取json文件，生成一个dict
file = open('test.txt', 'r') 
js = file.read()
dic = json.loads(js)   
print(dic) 
file.close()


http://caipiaojieguo.com/api/lottrey?biaoshi=ssq&format=json&rows=10