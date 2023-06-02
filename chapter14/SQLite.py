# SQLite不是一个客户端/服务器结构的数据库引擎，而是一种嵌入式数据库，它的数据库就是一个文件。
# SQLite将整个数据库，包括定义、表、索引以及数据本身，作为一个单独的、可跨平台使用的文件存储在主机中。
# 由于SQLite本身是用C语言写的，而且体积很小，所以，经常被集成到各种应用程序中。
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何模块，直接使用。

# Python操作数据库的通用的流程:
# 开始->创建connection->获取cursor->执行SQL语句，处理数据结果->关闭cursor->关闭connection->结束
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect('test.db')
# # 创建一个Cursor:
# cursor = conn.cursor()
# # 执行一条SQL语句，创建user表:
# cursor.execute('create table user (id int(10)  primary key, name varchar(20))')
# # 关闭游标
# cursor.close()
# # 提交事务:
# conn.commit()
# # 关闭Connection:
# conn.close()

# 操作SQLite

# 新增用户数据信息
# insert into 表名(字段名1,字段名2,…,字段名n) values (字段值1,字段值2,…,字段值n)
# 在user表中有两个字段，字段名分别为id和name。
# 而字段值需要根据字段的数据类型来赋值，如id是一个长度为10的整型，name是长度为20的字符串型数据。
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# # 向user表中插入3条用户信息记录
# cursor.execute('create table user (id int(10)  primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values ("1","张三")')
# cursor.execute('insert into user (id, name) values ("2","李四")')
# cursor.execute('insert into user (id, name) values ("3","王五")')
# cursor.close()
# conn.commit()
# conn.close()

# 查看用户数据信息
# select 字段名1,字段名2,字段名3,… from 表名 where 查询条件
# 查看用户信息的代码与插入数据信息大致相同，不同点在于使用的SQL语句不同。
# 此外，查询数据时通常使用如下3种方式：
# fetchone()：获取查询结果集中的下一条记录。
# 使用fetchone()方法返回的result1为一个元组
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into user (id, name) values ("1","张三")')
cursor.execute('insert into user (id, name) values ("2","李四")')
cursor.execute('insert into user (id, name) values ("3","王五")')
cursor.execute('SELECT * FROM user')
result1 = cursor.fetchone()
print(result1)
cursor.close()
conn.commit()
conn.close()
# fetchmany(size)：获取指定数量的记录。
# 使用fetchmany()方法传递一个参数，其值为2，默认为1。返回的result2为一个列表，列表中包含两个元组
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into user (id, name) values ("1","张三")')
cursor.execute('insert into user (id, name) values ("2","李四")')
cursor.execute('insert into user (id, name) values ("3","王五")')
cursor.execute('SELECT * FROM user')
result2 = cursor.fetchmany(2)
print(result2)
cursor.close()
conn.commit()
conn.close()

# fetchall()：获取结构集的所有记录。
# 使用fetchall()方法返回的result3为一个列表
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into user (id, name) values ("1","张三")')
cursor.execute('insert into user (id, name) values ("2","李四")')
cursor.execute('insert into user (id, name) values ("3","王五")')
cursor.execute('SELECT * FROM user')
result3 = cursor.fetchall()
print(result3)
cursor.close()
conn.commit()
conn.close()

# 在select查询语句中使用问号作为占位符代替具体的数值，然后使用一个元组来替换问号（注意，不要忽略元组中最后的逗号）。
# 使用占位符的方式可以避免SQL注入的风险，推荐使用这种方式。
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into user (id, name) values ("1","张三")')
cursor.execute('insert into user (id, name) values ("2","李四")')
cursor.execute('insert into user (id, name) values ("3","王五")')
cursor.execute('SELECT * FROM user WHERE id > ?', (1,))
# 等价于cursor.execute('SELECT * FROM user WHERE id > 1')
result3 = cursor.fetchall()
print(result3)
cursor.close()
conn.commit()
conn.close()

# 修改用户数据信息
# update 表名 set 字段名 = 字段值 where 查询条件
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into user (id, name) values ("1","张三")')
cursor.execute('insert into user (id, name) values ("2","李四")')
cursor.execute('insert into user (id, name) values ("3","王五")')
cursor.execute('UPDATE user SET name = ? WHERE id = ?', ('刘一', 1))
cursor.execute('SELECT * FROM user')
result = cursor.fetchall()
print(result)
cursor.close()
conn.commit()
conn.close()
