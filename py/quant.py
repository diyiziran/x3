#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
量化草稿
通用的再整理到quant包下
'''
#从新浪读期货数据（历史和实时）：https://blog.csdn.net/tcy23456/article/details/80946838


#import DataFrame as df
import matplotlib.pyplot as plt
import numpy as np
import tushare as ts
import operator
from openpyxl import load_workbook
from openpyxl import Workbook


import requests
import numpy as np
import psycopg2

#读实盘数据
#功能：  实时读取新浪财经期货数据
#参数:   请输入要读取的合约名称
#返回值：以数组的形式返回

#维护一个关注的期货list，包含代码和中文名
future_dict={'L0':'塑料','C0':'玉米','RB0':'螺纹钢','AG0':'白银','AU0':'黄金','CU0':'沪铜'
             ,'AL0':'沪铝','ZN0':'沪锌','PB0':'沪铅','RU0':'橡胶','FU0':'燃油','WR0':'线材'
             ,'A0':'大豆','M0':'豆粕','Y0':'豆油','J0':'焦炭','P0':'棕油','V0':'PVC'
             ,'V0':'菜籽','RM0':'菜粕','FG0':'玻璃','CF0':'棉花','WS0':'强麦','ER0':'籼稻'
             ,'ME0':'甲醇','RO0':'菜油','TA0':'甲酸'}

write_future_his_data_to_db(future_dict,all_his=True)

def write_future_his_data_to_db(future_dict,all_his=False):
    conn = psycopg2.connect(database="postgres",user="postgres",password="123456",host="localhost",port="5432")
    cur = conn.cursor()
#    调用函数，读取数据
    df=get_his_data(list(future_dict),all_his)
    
    for i in range(1,len(df)):
        cur.execute("delete from public.future_his_data where date=%s and future_code=%s",
                    (df.iloc[i].date,df.iloc[i].future_code))
        cur.execute("INSERT INTO public.future_his_data(date, future_code, future_name, open,high,low,close,vol,ma5,ma10,ma20,ma30,ma40,ma60,ma120)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (df.iloc[i].date,df.iloc[i].future_code,future_dict[df.iloc[i].future_code],df.iloc[i].open,df.iloc[i].high,df.iloc[i].low,df.iloc[i].close,df.iloc[i].vol
                     ,df.iloc[i].MA5,df.iloc[i].MA10,df.iloc[i].MA20,df.iloc[i].MA30,df.iloc[i].MA40
                     ,df.iloc[i].MA60,df.iloc[i].MA120))
    
    #提交
    conn.commit()
    # 关闭练级
    cur.close()
    conn.close()
    
def write_future_real_data_to_db(future_dict):
    conn = psycopg2.connect(database="postgres",user="postgres",password="123456",host="localhost",port="5432")
    cur = conn.cursor()
#    调用函数，读取数据
    df=read_real_future_data2(list(future_dict))
#    'date','future_code','future_name','read_data_time','open','high','low','close','vol'
    for i in range(1,len(df)):
        cur.execute("delete from public.future_real_data where date=%s and future_code=%s and read_data_time=%s",
                    (df.iloc[i].date,df.iloc[i].future_code,df.iloc[i].read_data_time))
        cur.execute("INSERT INTO public.future_real_data(date, future_code, future_name, read_data_time,open,high,low,close,vol)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (df.iloc[i].date,df.iloc[i].future_code,future_dict[df.iloc[i].future_code],df.iloc[i].read_data_time,df.iloc[i].open,df.iloc[i].high,df.iloc[i].low,df.iloc[i].close,df.iloc[i].vol)
                    )
    
    #提交
    conn.commit()
    # 关闭练级
    cur.close()
    conn.close()
future_dict2={'L0':'塑料','AG0':'白银','AU0':'黄金','CU0':'沪铜'
             ,'AL0':'沪铝','ZN0':'沪锌','PB0':'沪铅','RU0':'橡胶','FU0':'燃油','WR0':'线材'
             ,'A0':'大豆','Y0':'豆油','J0':'焦炭','P0':'棕油','V0':'PVC'
             ,'V0':'菜籽','RM0':'菜粕','FG0':'玻璃','CF0':'棉花'
             ,'TA0':'甲酸'}    
write_future_real_data_to_db(future_dict2)


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

def read_real_future_data2(future_code_list):
##    future_code ='M1809'
    #从新浪财经读数据
    import pandas as pd
    df_merge=pd.DataFrame()
    for future_code in future_code_list :
#        future_code='M1909'
        print(future_code)
        url_str = ('http://hq.sinajs.cn/list=' +future_code)
        r = requests.get(url_str)
        #数据处理，保存在临时数组中
        b=list(r)
        str1=b[0].decode(encoding='gbk') +b[1].decode(encoding='gbk')
        str2=str1.split(',')
        str3=str2[0].split('_')[-1]
        str4=str3.split('=')
        
        l=[[str2[17],str4[0],str2[16],str2[1],str2[2],str2[3],str2[4],str2[6],str2[14]]]
        df=pd.DataFrame(l,columns=['date','future_code','future_name','read_data_time','open','high','low','close','vol'])
        df_merge=df_merge.append(df,ignore_index =True)

    
    return df_merge

df=read_real_future_data2(list(future_dict))
df1=read_real_future_data2(['RB1909'])
df=read_real_future_data2(['L0',
 'AG0',
 'AU0',
 'CU0',
 'AL0',
 'ZN0',
 'PB0',
 'RU0',
 'FU0',
 'WR0',
 'A0',
 'Y0',
 'J0',
 'P0',
 'V0',
 'RM0',
 'FG0',
 'CF0',
 'TA0'])
#读历史数据
def get_his_data(future_code_list,all_his=False):
    '''
    future_code_list:期货产品代码列表
    从新浪读取历史行情数据，并计算n日移动平均数据指标
    return：行情数据DataFrame，包含n日移动平均数据指标
    '''
    import pandas as pd
    df_merge=pd.DataFrame()
    for future_code in future_code_list :
#        future_code = 'M1909'
        print(future_code)
        url_str = ('http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=' +
        future_code)
        r = requests.get(url_str)
        r_json = r.json()
        r_lists = list(r_json)
        r_lists.sort(key=operator.itemgetter(0))
        l=r_lists
        
        if all_his==False :
            l=l[-2:-1]
        for al in l:
            al.append(future_code)            
        df=pd.DataFrame(l,columns=['date','open','high','low','close','vol','future_code'])
        #调整columns顺序，注意语法是双中括号
        df=df[['date','future_code','open','high','low','close','vol']]
        #计算移动平均数
        df['MA5']=df['close'].rolling(window=5).mean()
        df['MA10']=df['close'].rolling(window=10).mean()
        df['MA20']=df['close'].rolling(window=20).mean()
        df['MA30']=df['close'].rolling(window=30).mean()
        df['MA40']=df['close'].rolling(window=40).mean()
        df['MA60']=df['close'].rolling(window=60).mean()
        df['MA120']=df['close'].rolling(window=120).mean()
#        注意要加上ignore_index =True，否则就会因为index值一样而被覆盖掉了
        df_merge=df_merge.append(df,ignore_index =True)
    
    return df_merge

df=get_his_data(['M1909'])



# 2.新浪期货数据各品种代码（商品连续）如下
#
#
#future_dict={'L0':'塑料','C0':'玉米','RB0':'螺纹钢','AG0':'白银','AU0':'黄金','CU0':'沪铜'
#             ,'AL0':'沪铝','ZN0':'沪锌','PB0':'沪铅','RU0':'橡胶','FU0':'燃油','WR0':'线材'
#             ,'A0':'大豆','M0':'豆粕','Y0':'豆油','J0':'焦炭','P0':'棕油','V0':'PVC'
#             ,'V0':'菜籽','RM0':'菜粕','FG0':'玻璃','CF0':'棉花','WS0':'强麦','ER0':'籼稻'
#             ,'ME0':'甲醇','RO0':'菜油','TA0':'甲酸'}
# RB0 螺纹钢
# AG0 白银
# AU0 黄金
# CU0 沪铜
# AL0 沪铝
# ZN0 沪锌
# PB0 沪铅
# RU0 橡胶
# FU0 燃油
# WR0 线材
# A0 大豆
# M0 豆粕
# Y0 豆油
# J0 焦炭
# C0 玉米
# L0 乙烯
# P0 棕油
# V0 PVC
# RS0 菜籽
# RM0 菜粕
# FG0 玻璃
# CF0 棉花
# WS0 强麦
# ER0 籼稻
# ME0 甲醇
# RO0 菜油
# TA0 甲酸
# CFF_RE_IF1307  股指期货
#    
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

