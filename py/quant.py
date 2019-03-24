#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pandas as pd
#import DataFrame as df
import matplotlib.pyplot as plt
import numpy as np
import tushare as ts

#2015年第三季度基金持股情况
df=ts.fund_holdings(2017,2)
#df.to_csv('d:/x3/py/jjcg.csv')
df.to_excel('d:/x3/py/jjcg.xlsx')

df.sort(columns='nums').tail()
df.s

#设置通联数据的凭证
ts.set_token('a6077ed0e7f1f4e3758f4beb973bb7180a5971026c6558a7ea57433a1533a064')
ts.get_notices(code='000776.sh')


#打印乘法口诀
l1=list()
for i in range(1,10):
    l1.append(i)
l2=random.sample(l1,9)
l3=random.sample(l1,9)
     
for j in l3:
    for i in l2:
        print(str(j)+' x '+str(i)+' = ')
    
for j in range(7,10):
    for i in l2:
        print(str(j)+' x '+str(i)+' = ')    
    
f1=np.random.randint(9,size=9)

for i in range(10):
    for j in range(10):
        print(str(i)+' x '+str(j)+' = ')
        
        
for i in np.random.randint(1,10,size=9):
    print('9 x '+str(i)+' = ')
    