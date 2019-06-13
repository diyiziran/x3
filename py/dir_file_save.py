# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
from openpyxl import load_workbook


#写到excel文件
save_file_name="/Users/zhengjt/x3/py/目录.xlsx"
save_sheet_name="kindle"

wb = load_workbook(save_file_name)
sheet = wb.get_sheet_by_name("kindle")
i=1
sheet["A%d" % i].value="目录"
sheet["B%d" % i].value="文件名"
mypath=os.getcwd()
for cur_dir, sub_dirs, files in os.walk(mypath): 
    for file in files :
        sheet["A%d" % (i+1)].value=cur_dir
        sheet["B%d" % (i+1)].value=file
        i=i+1
        
wb.save(save_file_name)
