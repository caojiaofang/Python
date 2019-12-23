# !/usr/bin/python
# -*- coding: utf-8 -*-

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

# print(L)
# print(n)

# r = []
# n = 6
# for i in range(n):
#     r.append(L[i])


# python 中的切片功能

# print(L[:6])
# print(L[2:6])
#
# print(L[-9:-7])


# python 中的迭代
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)


# python 中的列表生成式
import  os

s = [d for d in os.listdir('.')]
print(s)

# python 中的生成器 生成的是generator
g = (x * x for x in  range(10))
for n in g:
    print(n)