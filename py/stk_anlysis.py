#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#股票分析第一部分
# http://mp.weixin.qq.com/s?__biz=MjM5NzU0MzU0Nw==&mid=2651372610&idx=1&sn=01674a9b9b0e1649ea425003032509f2&chksm=bd2477568a53fe40732d9b461fe7964f491542201523a60b2de01d44032b9a60ea26fc6543b9&mpshare=1&scene=1&srcid=0103E5IPu72RgBXa6oW2oIo5#rd
# 

import pandas as pd#
#import pandas.io.dat as web
from pandas_datareader import wb,data
import matplotlib.pyplot as plt
import datetime
import tushare as ts

start = datetime.datetime(2016,1,1)
end = datetime.date.today()

goog = data.DataReader("GOOG","yahoo")
#国内的数据可以tushare查询
stk_data=ts.get_hist_data('600848',start='2019-05-05',end='2019-06-03')
df=goog[goog.index>'2019-04-01']
plt.plot(df['Open'])
plt.plot(df['Close'])
plt.show()



#tushare pro的使用
#ts.set_token('b7bbd6907437d1f894145e7487709d27ee220b6c3772205ef05c83fb')
#pro=ts.pro_api()

ts.set_token('b7bbd6907437d1f894145e7487709d27ee220b6c3772205ef05c83fb')
pro=ts.pro_api()
df=pro.daily(ts_code='000001.SZ', start_date='20190501', end_date='20190603')
plt.plot(df['open'])
plt.plot(df['close'])
plt.show()
plt.plo