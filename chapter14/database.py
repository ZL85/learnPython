# 程序运行的时候，数据都是在内存中的。
# 当程序终止的时候，通常都需要将数据保存到磁盘上，前面我们学习了将数据写入文件，保存在磁盘上。
# 为了便于程序保存和读取数据，而且，能直接通过条件快速查询到指定的数据，就出现了数据库（Database）这种专门用于集中存储和查询的软件。

# 数据库编程接口
# 为了对数据库进行统一的操作，大多数语言都提供了简单的、标准化的数据库接口（API）。
# 在Python Database API 2.0规范中，定义了Python数据库API接口的各个部分，如模块接口、连接对象、游标对象、类型对象和构造器、DB API的可选扩展以及可选的错误处理机制等。

# 连接对象
# 数据库连接对象（Connection Object）主要提供获取数据库游标对象和提交/回滚事务的方法，以及关闭数据库连接。

# 获取连接对象
# 如何获取连接对象呢？这就需要使用connect()函数。该函数有多个参数，具体使用哪个参数，取决于使用的数据库类型。
# 参数        说明
# dsn         数据源名称，给出该参数表示数据库依赖
# user        用户名
# password    用户密码
# host        主机名
# database    数据库名称

# 例如，使用PyMySQL模块连接MySQL数据库，示例代码如下：
# conn = pymysql.connect(host='localhost',
#                              user='user',
#                              password='passwd',
#                              db='test',
#                              charset='utf8',
#                              cursorclass=pymysql.cursors.DictCursor)

# 连接对象的方法
# connect()函数返回连接对象。这个对象表示目前和数据库的会话。
# 方法名      说明
# close()     关闭数据库连接
# commit()    提交事务
# rollback()  回滚事务
# cursor()    获取游标对象，操作数据库，如执行DML操作，调用存储过程等
# commit()方法用于提交事务，事务主要用于处理数据量大、复杂度高的数据。如果操作的是一系列的动作，比如张三给李四转账，有如下两个操作：
# 张三账户金额减少；
# 李四账户金额增加。
# 这时使用事务可以维护数据库的完整性，保证两个操作要么全部执行，要么全部不执行。

# 游标对象
# 游标对象（Cursor Object）代表数据库中的游标，用于指示抓取数据操作的上下文。
# 主要提供执行SQL语句、调用存储过程、获取查询结果等方法。
# 如何获取游标对象呢？通过使用连接对象的cursor()方法，可以获取到游标对象。
# 游标对象的属性如下所示：
# description：数据库列类型和值的描述信息。
# rowcount：回返结果的行数统计信息，如SELECT、UPDATE、CALLPROC等。

# 方法名                                  说明
# callproc(procname,[, parameters])      调用存储过程，需要数据库支持
# close()                                关闭当前游标
# execute(operation[, parameters])       执行数据库操作，SQL语句或者数据库命令
# executemany(operation, seq_of params)  用于批量操作，如批量更新
# fetchone()                             获取查询结果集中的下一条记录
# fetchmany(size)                        获取指定数量的记录
# fetchall()                             获取结果集的所有记录
# nextset()                              跳至下一个可用的结果集
# arraysize                              指定使用fetchmanyO获取的行数，默认为1
# setinputsizes(sizes)                   设置在调用execute*()方法时分配的内存区域大小
# setoutputsize(sizes)                   设置列缓冲区大小，对大数据列如LONGS和BLOBS尤其有用
