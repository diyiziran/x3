#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:17:45 2019

@author: zhengjt
"""
import tushare as ts



def future_pool():
    '''
    根据规则自动维护一个标的池
    '''
    futures=get_all_securities(types=['futures'])
    prd_list=futures[futures.index.str.contains('9999')].index
    return prd_list

def prd_pool():
    '''
    人工维护一个标的池
    '''
    prd_list=['A9999.XDCE', 'AG9999.XSGE', 'AL9999.XSGE', 'AP9999.XZCE',
       'AU9999.XSGE', 'B9999.XDCE', 'BB9999.XDCE', 'BU9999.XSGE', 'C9999.XDCE',
       'CF9999.XZCE', 'CJ9999.XZCE', 'CS9999.XDCE', 'CU9999.XSGE',
       'CY9999.XZCE', 'EG9999.XDCE', 'ER9999.XZCE', 'FB9999.XDCE',
       'FG9999.XZCE', 'FU9999.XSGE', 'GN9999.XZCE', 'HC9999.XSGE',
       'I9999.XDCE', 'IC9999.CCFX', 'IF9999.CCFX', 'IH9999.CCFX', 'J9999.XDCE',
       'JD9999.XDCE', 'JM9999.XDCE', 'JR9999.XZCE', 'L9999.XDCE',
       'LR9999.XZCE', 'M9999.XDCE', 'MA9999.XZCE', 'ME9999.XZCE',
       'NI9999.XSGE', 'OI9999.XZCE', 'P9999.XDCE', 'PB9999.XSGE',
       'PM9999.XZCE', 'PP9999.XDCE', 'RB9999.XSGE', 'RI9999.XZCE',
       'RM9999.XZCE', 'RO9999.XZCE', 'RS9999.XZCE', 'RU9999.XSGE',
       'SC9999.XINE', 'SF9999.XZCE', 'SM9999.XZCE', 'SN9999.XSGE',
       'SP9999.XSGE', 'SR9999.XZCE', 'T9999.CCFX', 'TA9999.XZCE',
       'TC9999.XZCE', 'TF9999.CCFX', 'TS9999.CCFX', 'V9999.XDCE',
       'WH9999.XZCE', 'WR9999.XSGE', 'WS9999.XZCE', 'WT9999.XZCE',
       'Y9999.XDCE', 'ZC9999.XZCE', 'ZN9999.XSGE']
    return prd_list

def break_prd(prd_list,day_num):
    '''
    突破均线的标的
    '''
    up_break_list=[]
    down_break_list=[]
    
    for prd in prd_list: 
        price_list = attribute_history(prd,day_num,'1d',['close'])
        stk_data=ts.get_hist_data(prd,start='2019-05-05',end='2019-06-03')
        ma = price_list['close'].mean()
        today_price = price_list['close'][-1]
        yesterday_price = price_list['close'][-2]
        #向上突破：昨天小于均线，今天大于均线
        if yesterday_price < ma and today_price > ma :
            up_break_list.append(prd)
        #向下突破：昨天大于均线，今天小于均线
        elif yesterday_price > ma and today_price < ma :
            down_break_list.append(prd)
        
    return up_break_list,down_break_list

