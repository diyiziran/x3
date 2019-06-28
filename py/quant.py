#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
量化草稿
通用的再整理到quant包下
'''
#从新浪读期货数据（历史和实时）：https://blog.csdn.net/tcy23456/article/details/80946838


import pandas as pd
#import DataFrame as df
import matplotlib.pyplot as plt
import numpy as np
import tushare as ts
import random
from openpyxl import load_workbook
from openpyxl import Workbook


#df = ts.get_tick_data('600848',date='2018-12-12',src='tt')
#df.head(10)

import requests
import sys
import numpy as np


#读实盘数据
#功能：  实时读取新浪财经期货数据
#参数:   请输入要读取的合约名称
#返回值：以数组的形式返回


def read_real_future_data(future_code):




##    future_code ='M1809'
    #从新浪财经读数据
    url_str = ('http://hq.sinajs.cn/list=' +future_code)
    r = requests.get(url_str)
    #数据处理，保存在临时数组中
    b=list(r)
    str1=b[0].decode(encoding='gbk') +b[1].decode(encoding='gbk')
    str2=str1.split(',')
    str3=str2[0].split('_')[-1]
    str4=str3.split('=')
    ##-------------------------------------------------------------------------
    ##  2018/7/5 shanghai tcy python版本
    ##f=[0,0,0,0,0,0,0,0]
    ##f[0]=str4[0]             #code
    ##f[1]=str4[1].strip('"')  #name
    ##f[2]=str2[17]  #date
    ##f[3]=str2[2]   #open
    ##f[4]=str2[3]   #high
    ##f[5]=str2[4]   #low
    ##f[6]=str2[6]   #close
    ##f[7]=str2[14]  #vol
    ##--------------------------------------------------------------------------
    ## numpy版本运行速度快
    dt=np.dtype([('code','S10'),('name','U10'),('date','datetime64[D]'),('open',np.float32),
               ('high',np.float32),('low',np.float32),('close',np.float32),('vol',np.float32)])

#0：豆粕连续，名字
#1：145958，数据读取时间
#2：3170，开盘价
#3：3190，最高价
#4：3145，最低价
#5：3178，昨日收盘价 （2018年6月27日）
#6：3153，买价，即“买一”报价
#7：3154，卖价，即“卖一”报价
#8：3154，最新价，即收盘价
#9：3162，结算价
#10：3169，昨结算
#11：1325，买  量
#12：223，卖  量
#13：1371608，持仓量
#14：1611074，成交量
#15：连，大连商品交易所简称
#16：豆粕，品种名简称
#17：2018-06-28，日期
    
    f=np.array([("","",'1970-01-01',0.0,0.0,0.0,0.0,0.0)],dtype=dt)
    f[0]['code']=str4[0]   #code
    f[0]['name']=str2[16]  #name
    f[0]['date']=str2[17]  #date
    f[0]['open']=str2[2]   #open
    f[0]['high']=str2[3]   #high
    f[0]['low']=str2[4]    #low
    f[0]['close']=str2[6]  #close
    f[0]['vol']=str2[14]   #vol
    #测试程序
##    print('code name date,open,high,low,close,vol')
##    print(f)
    return f


#读历史数据
future_code = 'M1909'
url_str = ('http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=' +
future_code)
r = requests.get(url_str)
r_json = r.json()
r_lists = list(r_json)
print('future_code,date,open,high,low,close,vol')


for r_list in r_lists:
    for v in r_list:
        print(v + ',',end='')
    print('\n')

l=r_lists
for al in l:
    al.append('M1909')
    
df=pd.DataFrame(l,columns=['date','open','high','low','close','vol','future_code'])
#调整columns顺序，注意语法是双中括号
df=df[['date','future_code','open','high','low','close','vol']]
#计算移动平均数
df['MA20']=df['close'].rolling(window=20).mean()


#3，分词结果写到excel文件
filename="tmp.xlsx"
wb = load_workbook(filename)
#sheet = wb.active
sheet = wb["工作表1"]
#sheet = wb.get_sheet_by_name("工作表1")
#sheet.title='分词结果'
#写到excel文件

for i in range(1,len(df)):
    sheet["A%d" % (i+1)]=df.iloc[i]['close']
    sheet["B%d" % (i+1)]=df.iloc[i]['MA20']
    sheet["c%d" % (i+1)]=df.iloc[i]['date']
    i=i+1

wb.save(filename)   



# 2.新浪期货数据各品种代码（商品连续）如下
#
#
#         RB0 螺纹钢
#         AG0 白银
#         AU0 黄金
#         CU0 沪铜
#         AL0 沪铝
#         ZN0 沪锌
#         PB0 沪铅
#         RU0 橡胶
#         FU0 燃油
#         WR0 线材
#         A0 大豆
#         M0 豆粕
#         Y0 豆油
#         J0 焦炭
#         C0 玉米
#         L0 乙烯
#         P0 棕油
#         V0 PVC
#         RS0 菜籽
#         RM0 菜粕
#         FG0 玻璃
#         CF0 棉花
#         WS0 强麦
#         ER0 籼稻
#         ME0 甲醇
#         RO0 菜油
#         TA0 甲酸
#         CFF_RE_IF1307  股指期货
    
########################################
    #从新浪读历史数据
# 历史数据读取
#
#
#    商品期货
#    http://stock2.finance.sina.com.cn/futures/api/json.php/
#    IndexService.getInnerFuturesMiniKLineXm?symbol=CODE
#    例子：
#        http://stock2.finance.sina.com.cn/futures/api/json.php/
#        IndexService.getInnerFuturesMiniKLine5m?symbol=M0
#    5分钟
#        http://stock2.finance.sina.com.cn/futures/api/json.php/
#        IndexService.getInnerFuturesMiniKLine5m?symbol=M0
#    15分钟
#        http://stock2.finance.sina.com.cn/futures/api/json.php/
#        IndexService.getInnerFuturesMiniKLine15m?symbol=M0
#    30分钟
#        http://stock2.finance.sina.com.cn/futures/api/json.php/
#        IndexService.getInnerFuturesMiniKLine30m?symbol=M0
#    60分钟
#        http://stock2.finance.sina.com.cn/futures/api/json.php/
#        IndexService.getInnerFuturesMiniKLine60m?symbol=M0
#    日K线
#        http://stock2.finance.sina.com.cn/futures/api/json.php/
#        IndexService.getInnerFuturesDailyKLine?symbol=M0
#
#
#    股指期货
#    5分钟
#    http://stock2.finance.sina.com.cn/futures/api/json.php/
#    CffexFuturesService.getCffexFuturesMiniKLine5m?symbol=IF1306
#
#
#    15
#    http://stock2.finance.sina.com.cn/futures/api/json.php/
#    CffexFuturesService.getCffexFuturesMiniKLine15m?symbol=IF1306
#    30分钟
#    http://stock2.finance.sina.com.cn/futures/api/json.php/
#    CffexFuturesService.getCffexFuturesMiniKLine30m?symbol=IF1306
#
#
#    60分钟
#    http://stock2.finance.sina.com.cn/futures/api/json.php/
#    CffexFuturesService.getCffexFuturesMiniKLine60m?symbol=IF1306
#
#
#    日线
#    http://stock2.finance.sina.com.cn/futures/api/json.php/
#    CffexFuturesService.getCffexFuturesDailyKLine?symbol=IF1306   

