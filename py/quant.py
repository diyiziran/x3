#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
print sys.version
import pandas as pd
#import DataFrame as df


import tushare as ts

#2015年第三季度基金持股情况
df=ts.fund_holdings(2015,3)
#df.to_csv('d:/x3/py/jjcg.csv')
df.to_excel('d:/x3/py/jjcg.xlsx')
df.sort(columns='nums').tail()
#设置通联数据的凭证
ts.set_token('a6077ed0e7f1f4e3758f4beb973bb7180a5971026c6558a7ea57433a1533a064')