#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 23:10:32 2018

@author: zhengjt
"""
#在聚宽上面跑的模拟策略
import jqdata
from jqlib.technical_analysis import *

def initialize(context):
	set_benchmark('000300.XSHG')
	# g.security = list()
	#持仓数量
	g.stocknum = 5
	# 开启动态复权模式(真实价格)
	set_option('use_real_price', True)
	# 股票类每笔交易时的手续费是：买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税, 每笔交易佣金最低扣5块钱
	set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
	# run_daily(stock_filter, time='after_close')
	run_daily(trade, time='14:50')

def trade(context):
	days = context.current_dt.day
	#Buylist = ['159902.XSHE','159901.XSHE']
	#过滤掉停牌、退市
	stock_list = filter_paused(stocklist())
	#金叉可买入，同时过滤掉涨停无法买入的股票
	toBuyList = filter_high_limit(isMACDGold(context,stock_list))
	#死叉卖出，同时过滤掉跌停无法卖出的股票
	toSellList = filter_low_limit(isMACDDead(context,stock_list))
	
	#卖出死叉的证券
	for stock in toSellList:
	    order_target(stock, 0)
	    log.info("sail stock", stock)

	#分配每只股票的买入金额            
	if len(context.portfolio.positions) < g.stocknum :
	    Num = g.stocknum - len(context.portfolio.positions)
	    Cash = context.portfolio.cash/Num
	else:
	    Cash = 0

	#买入金叉股票，知道持仓数量为stocknum
	while len(context.portfolio.positions) < g.stocknum and len(toBuyList)>0:
	    stock_code = toBuyList.pop(0)
	    order_value(stock_code,Cash)
	    log.info("buy_stock", stock_code)


#股票池,返回list类型的股票清单
def stocklist():
    #按证券概念，但是没有返回数据，原因？
    #return get_concept_stocks('GN189')
    #按证券所属行业
    #return get_industry_stocks('A01')
    return get_industry_stocks('C15')
    #按证券标的类型
    #return list(get_all_securities(types=['fund']).index)
    #所有股
    #return list(get_all_securities().index) 
    
def isMACDGold(context,security):
    '''
    判断是否 MACD 金叉
    return 金叉买入清单list
    '''
    #当天和前一个交易日的日期
    check_date = context.current_dt.strftime('%Y-%m-%d')
    previous_date = context.previous_date
    
    # 计算并输出 security 的 MACD 值
    macd_dif, macd_dea, macd_macd = MACD(security,check_date=check_date, SHORT = 12, LONG = 26, MID = 9)
    previous_date_macd_dif, previous_date_macd_dea, previous_date_macd_macd = MACD(security,check_date=previous_date, SHORT = 12, LONG = 26, MID = 9)

    MACDGoldList = list()
    for st in security:
        if macd_dif[st]>0 and macd_dif[st]>previous_date_macd_dif[st]*1.05 and previous_date_macd_macd[st] < 0  and macd_macd[st] > 0:
        #if macd_dif[st]>0 and macd_dea[st]>0 and previous_date_macd_macd[st] < 0  and macd_macd[st] > 0:
            MACDGoldList.append(st)
    return MACDGoldList
    
    
def isMACDDead(context,security):
    '''
    判断是否 MACD 死叉
    return 死叉卖出清单list
    '''
    #当天和前一个交易日的日期
    check_date = context.current_dt.strftime('%Y-%m-%d')
    previous_date = context.previous_date
    
    # 计算并输出 security 的 MACD 值
    macd_dif, macd_dea, macd_macd = MACD(security,check_date=check_date, SHORT = 12, LONG = 26, MID = 9)
    previous_date_macd_dif, previous_date_macd_dea, previous_date_macd_macd = MACD(security,check_date=previous_date, SHORT = 12, LONG = 26, MID = 9)
    
    MACDDeadList = list()
    for st in security:
        if (previous_date_macd_macd[st] > 0  and macd_macd[st] < 0) or macd_dif[st]<previous_date_macd_dif[st]:
            MACDDeadList.append(st)
    return MACDDeadList
  

# --------------------- 特殊股票过滤 ------------------------------------
# 过滤停牌、退市、ST股票、涨停、跌停
def filter_specials_all(stock_list):
    curr_data = get_current_data()
    stock_list = [stock for stock in stock_list if \
                  (not curr_data[stock].paused)  # 未停牌
                  and (not curr_data[stock].is_st)  # 非ST
                  and ('ST' not in curr_data[stock].name)
                  and ('*' not in curr_data[stock].name)
                  and ('退' not in curr_data[stock].name)
                  and (curr_data[stock].low_limit < curr_data[stock].last_price < curr_data[stock].high_limit)  # 未涨跌停
                  ]

    return stock_list
# 过滤过滤停牌
def filter_paused(stock_list):
    curr_data = get_current_data()
    stock_list = [stock for stock in stock_list if \
                  (not curr_data[stock].paused)  # 未停牌
                  ]

    return stock_list
# 过滤ST股票、退市
def filter_st(stock_list):
    curr_data = get_current_data()
    stock_list = [stock for stock in stock_list if \
                  (not curr_data[stock].is_st)  # 非ST
                  and ('ST' not in curr_data[stock].name)
                  and ('*' not in curr_data[stock].name)
                  and ('退' not in curr_data[stock].name)
                  ]

    return stock_list
# 过滤涨停
def filter_high_limit(stock_list):
    curr_data = get_current_data()
    stock_list = [stock for stock in stock_list if \
                  (curr_data[stock].last_price < curr_data[stock].high_limit)  # 未涨停
                  ]

    return stock_list
# 过滤跌停
def filter_low_limit(stock_list):
    curr_data = get_current_data()
    stock_list = [stock for stock in stock_list if \
                  (curr_data[stock].low_limit < curr_data[stock].last_price)  # 未跌停
                  ]

    return stock_list


