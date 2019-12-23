# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from hanshu import my_abs

# print('Hello World!')
# name = input('please enter your name: ')
# print(name)

# =============================
# list集合
list = ["lizhi", "fangfang", "pangpang"]
# print(list)
#
# print(len(list))
#
# print(list[2])

# list.insert(1, "baobao")
# print(list)
#
# list.pop()
# print(list)

# list.pop(3)
# print(list)

# list[1] = "search"
# print(list)


# ===================================================
# if else 判断
# str = input("please enter value： ")
# value = int(str)
# if value > 100:
#     print(str)
# elif value < 80:
#     print("hello value : " + str)
# else:
#     print("80 < " + str + " < 100")


# =======================================================
# 循环
# names = ['heng', 'ha', 'erjiang']
# for name in names:
#     print(name)

# sum = 0
# for i in [1, 2, 3, 4, 5]:
#     sum = sum + i
# print(sum)

# sum = 0
# for i in range(101):
#     sum = sum + i
# print(sum)


# sum = 0
# # n = 100
# # while n > 0:
# #     sum = sum + n
# #     n = n - 1
# # print(sum)

# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n +1
# print("END")

# n = 0
# # while n < 10:
# #     n = n + 1
# #     if n % 2 == 0:
# #         continue
# #     print(n)


# dict在java中又叫map 属于key-value
# d = {'lizhi': 100, 'xiaopang': 80, 'fangfang': 10}
# print(d['lizhi'])
#
# if 'xiao' in d:
#     print("xiao 是存在的")
# else:
#     print('xiao 不存在')
#
# print(d.get('xiao'))
# print(d.get('xiao', -1))
#
# d.pop('xiaopang')
# print(d)


# help(abs)
#
# a = abs
#
# print(a(-1))

print(my_abs(99))