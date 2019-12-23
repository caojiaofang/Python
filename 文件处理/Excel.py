# !/usr/bin/python
# -*- coding: utf-8 -*-

import xlrd
import xlwt

def readexcel():
    # 这个部分是读取内容
    workbook = xlrd.open_workbook('E:\公司\公积金二期后续任务计划1.1.xlsx')
    # 输出页签名
    print(workbook.sheet_names())
    # 打开页签
    sheet2 = workbook.sheet_by_name('Sheet1')
    # 获取行数
    nrows = sheet2.nrows
    # 获取列数
    ncols = sheet2.ncols
    # 输出结果
    print(nrows, ncols)


    # 取出第二行第二列的值
    cell_sheet2 = sheet2.cell(1, 1).value
    print(cell_sheet2)

if __name__ == '__main__':
    readexcel()
