#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pandas as pd
#import DataFrame as df
import matplotlib.pyplot as plt
import numpy as np
import tushare as ts
import random
from openpyxl import load_workbook
from openpyxl import Workbook

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
#random.seed(0)
l1=list()
q_mod=list()
q_mul=list()
#for i in range(2,10):
#    l1.append(i)
l1=[2,3,4,4,4,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,2,3,4,4,4,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9]
l_num=len(l1)
q_num=9
l2=random.sample(l1,q_num)
l3=random.sample(l1,q_num)
     
for j in l3:
    for i in l2:
        print(str(j)+' x '+str(i)+' = ')

#除法口诀
#按顺序
arr=np.zeros((l_num,l_num,3),dtype=np.int32)
for i in l_num:
    for j in l_num:
        if i<=j:
            arr[i-1][j-1]=[i,j,i*j]
            f1=arr[i-1][j-1][0]
            f2=arr[i-1][j-1][1]
            p=arr[i-1][j-1][2]
            if f1*f2*p>0:
                q_mod.append(str(p)+' ÷ '+str(f1)+' = '+str(f2)+'   ')
                print(str(p)+' ÷ '+str(f1)+' = '+str(f2)+'   ',end='')
    print()

wb = load_workbook("grade2.xlsx")
sheet = wb.active
#sheet = wb.get_sheet_by_name("工作表1")
sheet.title='除法'
#wb = Workbook()
#sheet = wb.active
#sheet = wb.get_sheet_by_name("Sheet3")
sheet["A%d" % (i+1)]
wb.save('保存一个新的excel.xlsx')
###############################################################
#random.seed(0)
l1=list()
q_mod=list()
q_mul=list()
#for i in range(2,10):
#    l1.append(i)
l1=[2,3,4,4,4,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,2,3,4,4,4,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9]
l_num=len(l1)  #随机抽样数
#q_num=9
l2=random.sample(l1,l_num)
l3=random.sample(l1,l_num)            
#随机   
arr=np.zeros((l_num,l_num,3),dtype=np.int32)
for i in l2:
    for j in l3:
        if i<=j:
            arr[i-1][j-1]=[i,j,i*j]
            f1=arr[i-1][j-1][0]
            f2=arr[i-1][j-1][1]
            p=arr[i-1][j-1][2]
            if f1*f2*p>0:
                q_mod.append(str(p)+' ÷ '+str(f1)+' = '+'   ')
#                print(str(p)+' ÷ '+str(f1)+' = '+'   ')
#写到excel文件
wb = load_workbook("grade2.xlsx")
sheet = wb.get_sheet_by_name("除法")
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["A%d" % (i+1)].value=q_mod_print[i-1]
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["B%d" % (i+1)].value=q_mod_print[i-1]    
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["C%d" % (i+1)].value=q_mod_print[i-1]
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["D%d" % (i+1)].value=q_mod_print[i-1]
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["E%d" % (i+1)].value=q_mod_print[i-1]
wb.save('grade2.xlsx')

#写到文本文件
f = open('test.txt', 'w')         
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
#    print(q_mod_print.pop())
    f.write(q_mod_print[i-1]+'\n')
#    print(q_mod_print[i-1])

f.close()    
###############################################################    
###########################乘法####################################
#random.seed(0)
l1=list()
q_mod=list()
q_mul=list()
#for i in range(2,10):
#    l1.append(i)
l1=[2,3,4,4,4,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9,2,3,4,4,4,5,5,5,6,6,6,7,7,7,7,7,8,8,8,8,9,9,9,9]
l_num=len(l1)  #随机抽样数
#q_num=9
l2=random.sample(l1,l_num)
l3=random.sample(l1,l_num)            
#随机   
arr=np.zeros((l_num,l_num,3),dtype=np.int32)
for i in l2:
    for j in l3:
        if i<=j:
            arr[i-1][j-1]=[i,j,i*j]
            f1=arr[i-1][j-1][0]
            f2=arr[i-1][j-1][1]
            p=arr[i-1][j-1][2]
            if f1*f2*p>0:
                if  random.randint(1,10) % 2 ==0 :
                    q_mod.append(str(f1)+' x '+str(f2)+' = '+'   ')
                else:    
                    q_mod.append(str(f2)+' x '+str(f1)+' = '+'   ')
#                print(str(p)+' ÷ '+str(f1)+' = '+'   ')

#写到excel文件
wb = load_workbook("grade2.xlsx")
sheet = wb.get_sheet_by_name("乘法")
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["A%d" % (i+1)].value=q_mod_print[i-1]
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["B%d" % (i+1)].value=q_mod_print[i-1]    
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["C%d" % (i+1)].value=q_mod_print[i-1]
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["D%d" % (i+1)].value=q_mod_print[i-1]
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
    sheet["E%d" % (i+1)].value=q_mod_print[i-1]
wb.save('grade2.xlsx')


f = open('乘法.txt', 'w')         
q_mod_print=random.sample(q_mod,len(q_mod))
for i in range(len(q_mod_print)):
#    print(q_mod_print.pop())
    f.write(q_mod_print[i-1]+'\n')
#    print(q_mod_print[i-1])

f.close()    
###########################乘法####################################

