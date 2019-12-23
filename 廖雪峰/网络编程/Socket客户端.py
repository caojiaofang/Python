# !/usr/bin/python
# -*- coding: utf-8 -*-

# 导入socket库
import socket

# 创建一个socket   AF_INET 指定使用IPv4协议  AF_INET6指定IPv6协议
# SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('127.0.0.1', 9999))

print(s.recv(1024).decode('utf-8'))

# socket发送消息报a bytes-like object is required, not 'str'错的时候试发送的内容要为byte

for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据
    print('发送的数据是[% s]' % data)
    s.send(data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))

s.send('exit'.encode('utf-8'))
s.close()