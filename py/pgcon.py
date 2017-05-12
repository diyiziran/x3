#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#安装 pip install psycopg2
import sys
import pandas as pd
import psycopg2

print sys.version




conn = psycopg2.connect(host="10.2.121.101",user="postgres",password="greenplum",database="hive")
cur = conn.cursor()
sql = "SELECT loginid, username, displayname, dpdn  FROM gfoa_user_org limit 5"
print 'tag'
cur.execute(sql)
rows=cur.fetchall()
#rows2=rows.encode('gb2312')
for i in rows :
	print len(i)
	print i[3]

#for i in rows :
#	for j in i:
#		print j

	

conn.commit()  # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
conn.close()