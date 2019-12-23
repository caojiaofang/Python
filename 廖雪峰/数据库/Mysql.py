# !/usr/bin/python
# -*- coding: utf-8 -*-

# 导入mysql驱动
import pymysql
hostname = '127.0.0.1'
username = 'root'
passwd = '123456'
database = 'demo'
conn = pymysql.connect(hostname, username, passwd, database)

cursor = conn.cursor()

# 创建user表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
try:
    # 执行sql语句
    cursor.execute('INSERT INTO demo.user (id, user_acct, user_name, user_pwd, user_organs, user_insert_time, user_login_time, user_state) '
               'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', ['1', 'admin', '管理员', 'e10adc3949ba59abbe56e057f20f883e', '709901', '2019-02-10 11:24:30', '', '00'])
    conn.commit()
except:
    # 发生错误时回滚
    conn.rollback()
    print('Error: unable to fetch data')

# 运行查询
cursor.execute('select * from user where id = %s', ('1',))
data = cursor.fetchall()
print('查询数据结果:%s' % (data,))

cursor.close()
conn.close()