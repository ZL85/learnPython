# 下载MySQL
# https://dev.mysql.com/downloads/windows/installer/5.7.html
import pymysql

# 打开数据库连接,参数1:主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名称
db = pymysql.connect(host="localhost", user="root", password="root", database="testdatabase")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % data)
# 关闭数据库连接
db.close()
# 上述代码中，首先使用connect()方法连接数据库，然后使用cursor()方法创建游标，
# 接着使用excute()方法执行SQL语句查看MySQL数据库版本，然后使用fetchone()方法获取数据，
# 最后使用close()方法关闭数据库连接。


# 创建数据表
# books表包含id（主键）、name（图书名称），category（图书分类），price（图书价格）和publish_time（出版时间）5个字段。
db = pymysql.connect(host="localhost", user="root", password="root", database="testdatabase")
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS books")
# 使用预处理语句创建表
sql = """
CREATE TABLE books (
  id int(8) NOT NULL AUTO_INCREMENT,
  name varchar(50) NOT NULL,
  category varchar(50) NOT NULL,
  price decimal(10,2) DEFAULT NULL,
  publish_time date DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
# 执行SQL语句
cursor.execute(sql)
# 关闭数据库连接
db.close()
![](https://cdn.jsdelivr.net/gh/ZL85/ImageBed@main//20230602175026.png)

# MySQL数据表的操作主要包括数据的增删改查
# 在向books图书表中插入图书数据时，可以使用excute()方法添加一条记录， 也可以使用executemany() 方法批量添加多条记录
# executemany(operation, seq_of_params)
# operation：操作的SQL语句。
# seq_of_params：参数序列。
db = pymysql.connect(host="localhost", user="root", password="root", database="testdatabase")
cursor = db.cursor()
# 数据列表
data = [("零基础学Python", 'Python', '79.80', '2018-5-20'),
        ("Python从入门到精通", 'Python', '69.80', '2018-6-18'),
        ("零基础学PHP", 'PHP', '69.80', '2017-5-23'),
        ("PHP项目开发实战入门", 'PHP', '79.80', '2016-5-23'),
        ("零基础学Java", 'Java', '69.80', '2017-5-23'),
        ]
try:
    # 执行sql语句，插入多条数据
    cursor.executemany("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)", data)
    # 提交数据
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()

# 使用connect()方法连接数据库时， 额外设置字符集charset="utf-8"，可以防止插入中文时出错。
# 在使用insert语句插入数据时，使用%s作为占位符，可以防止SQL注入。
# ![](https://cdn.jsdelivr.net/gh/ZL85/ImageBed@main//20230602174926.png)
