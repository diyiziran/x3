#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#股票分析第一部分
# http://mp.weixin.qq.com/s?__biz=MjM5NzU0MzU0Nw==&mid=2651372610&idx=1&sn=01674a9b9b0e1649ea425003032509f2&chksm=bd2477568a53fe40732d9b461fe7964f491542201523a60b2de01d44032b9a60ea26fc6543b9&mpshare=1&scene=1&srcid=0103E5IPu72RgBXa6oW2oIo5#rd
# 

import pandas as pd#
#import pandas.io.dat as web
from pandas_datareader import wb,data
import datetime

start = datetime.datetime(2016,1,1)
end = datetime.date.today()

goog = data.DataReader("GOOG","yahoo")
print type(goog)
print goog.head()