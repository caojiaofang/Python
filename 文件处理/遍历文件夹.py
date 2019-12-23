# !/usr/bin/python
# -*- coding: utf-8 -*-

# E:\360downloads
import os

path = 'E:/360downloads'

def get_file(path):
    # abspath获取目标文件夹的绝对路径
    path = os.path.abspath(path)
    # listdir获取指定文件夹中的所有文件和文件夹组成的列表
    files = os.listdir(path)
    for file in files:
        # join将2个路径合成一个路径
        abs_path = os.path.join(path, file)
        if os.path.isfile(abs_path):
            print(abs_path)
            if abs_path.endswith('新建文本文档.txt'):
                f = open(abs_path, encoding='utf-8')
                print(f.read())
        else:
            get_file(abs_path)

get_file(path)