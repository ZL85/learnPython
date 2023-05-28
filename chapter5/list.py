# 列表是Python中内置的可变序列。
# 在形式上，列表的所有元素都放在一对中括号“[]”中，两个相邻元素间使用逗号“,”分隔。
# 在内容上，可以将整数、实数、字符串、列表、元组等任何类型的内容放入列表中，并且同一个列表中，元素的类型可以不同。
import datetime

# 列表的创建和删除

# 使用赋值运算符直接创建列表
# listname[element 1,element 2,element3,...,element n]
# listname表示列表的名称，可以是任何符合Python命名规则的标识符；
# element 1、element 2、element 3、element n表示列表中的元素，个数没有限制，并且只要是Python支持的数据类型就可以。
# 通常情况下，我们在一个列表中只放入一种类型的数据，这样可以提高程序的可读性。

# 创建空列表
emptylist = []

# 创建数值列表
# Python中，可以使用list()函数直接将range()函数循环出来的结果转换为列表
# list(data)
# data表示可以转换为列表的数据，其类型可以是range对象、字符串、元组或者其他可迭代类型的数据
list1 = list(range(10, 20, 2))

# 删除列表
# del listname
# listname为要删除列表的名称
# del语句在实际开发时，并不常用。因为Python自带的垃圾回收机制会自动销毁不用的列表
del emptylist

# 访问列表元素
print(list1)
# 在输出列表时，是包括左右两侧的中括号的
print(list1[0])
# 在输出单个列表元素时，不包括中括号，如果是字符串，还不包括左右的引号

day = datetime.datetime.now().weekday()
# datetime.datetime.now()方法用于获取当前日期，
# 而weekday()方法则是从日期时间对象中获取星期，其值为0～6中的一个，为0时代表星期一，为1时代表星期二，依此类推，为6时代表星期日。
print(day)

# 遍历列表

# 用for循环实现
# 只能输出元素的值
# for item in listname:#输出item
# item用于保存获取到的元素值，要输出元素内容时，直接输出该变量即可；
# listname为列表名称。
for item in list1:
    print(item, end=" ")
print()

# 用for循环和enumerate()函数实现
# 可以同时输出索引值和元素内容
# for index,item in enumerate(listname):#输出index和item
# index：用于保存元素的索引；
# item用于保存获取到的元素值，要输出元素内容时，直接输出该变量即可；
# listname为列表名称。
for index, item in enumerate(list1):
    print(index, ":", item, "\t", end=" ")

# 添加元素
# append()方法用于在列表的末尾追加元素
# listname.append(obj)
# listname为要添加元素的列表名称；
# obj为要添加到列表末尾的对象。

# listname.extend(seq)
# listname为原列表；
# seq为要添加的列表。
# 语句执行后，seq2的内容将追加到listname的后面。







































