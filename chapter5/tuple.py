# 元组是由一系列按特定顺序排列的元素组成的不可变的列表
# 在形式上，元组的所有元素都放在一对小括号“()”中，两个相邻元素间使用逗号“,”分隔
# 在内容上，可以将整数、实数、字符串、列表、元组等任何类型的内容放入元组中，并且同一个元组中，元素的类型可以不同
# 通常情况下，元组用于保存程序中不可修改的内容
import random

# 元组的创建和删除
# 使用赋值运算符直接创建元组
# tuplename = (element 1,element 2,element 3,...,element n)
# tuplename表示元组的名称，可以是任何符合Python命名规则的标识符；
# element 1、element 2、element 3、element n表示元组中的元素，个数没有限制，并且只要是Python支持的数据类型就可以。
tuple1 = (7, 14, 21, 28, 35, 42, 49, 56, 63)
print(type(tuple1))
tuple2 = ('Python', 66, ("1", "2"), ["1", "2", "3", "4"])
print(type(tuple2))
tuple3 = ('elegant', "explicit", '''simple''')
print(type(tuple3))
# 在Python中，虽然元组是使用一对小括号将所有的元素括起来。
# 但是实际上，小括号并不是必需的，只要将一组值用逗号分隔开来，Python就可以认为它是元组。
tuple4 = 'elegant', "explicit", '''simple'''
print(type(tuple4))
# 如果要创建的元组只包括一个元素，则需要在定义元组时，在元素的后面加一个逗号“,”。
tuple5 = "hello",
print(type(tuple5))
print(len(tuple5))

# 创建空元组
emptytuple = ()
# 空元组可以应用在为函数传递一个空值或者返回空值时。

# 创建数值元组
# 在Python中，可以使用tuple()函数直接将range()函数循环出来的结果转换为数值元组。
# tuple(data)
# data表示可以转换为元组的数据，其类型可以是range对象、字符串、元组或者其他可迭代类型的数据。
tuple6 = tuple(range(10, 20, 2))
print(tuple6)

# 删除元组
# del tuplename
# tuplename为要删除元组的名称
del emptytuple

# 访问元组元素
# 在Python中，可以直接使用print()函数将元组的内容输出
# 在输出元组时，是包括左右两侧的小括号的。
# 如果不想输出全部元素，也可以通过元组的索引获取指定的元素。
print(tuple6[0])
# 在输出单个元组元素时，不包括小括号，如果是字符串，还不包括左右的引号。

# 元组也可以使用for循环进行遍历
for item in tuple6:
    print(item, end=" ")
print()

# 元组还可以使用for循环和enumerate()函数结合进行遍历。
for index, item in enumerate(tuple6):
    print(f"{index}:{item}", end="\t")
print()

# 修改元组
# 元组是不可变序列，所以我们不能对它的单个元素值进行修改，但是元组也不是完全不能修改。
# 我们可以对元组进行重新赋值。
tuple6 = tuple(range(0, 10, 2))
print("the original tuple6:", tuple6)
# 在进行元组连接时，连接的内容必须都是元组
tuple6 = tuple6 + (10, 12, 14, 16)
print("the tuple6 after modification:", tuple6)

# 元组推导式
tuple7 = tuple(random.randint(10, 100) for i in range(10))
print("generated tuple:", tuple7)
# 还可以直接通过for循环遍历或者直接使用__next()__方法进行遍历
tuple8 = (i for i in range(10))
print(tuple8.__next__())  # 输出第一个元素
print(tuple8.__next__())  # 输出第二个元素
print(tuple8.__next__())  # 输出第三个元素

for item in tuple8:
    print(item, end=" ")
print()
print(tuple(tuple8))
# 无论通过哪种方法遍历，如果还想再使用该生成器对象，都必须重新创建一个生成器对象。因为遍历后，原生成器对象已经不存在了。

# 元组与列表的区别
# 列表属于可变序列，它的元素可以随时修改或者删除，而元组属于不可变序列，其中的元素不可以修改，除非整体替换。
# 列表可以使用append()、extend()、insert()、remove()和pop()等方法实现添加和修改列表元素，而元组则没有这几个方法，因为不能向元组中添加和修改元素。同样，也不能删除元素。
# 列表可以使用切片访问和修改列表中的元素。元组也支持切片，但是它只支持通过切片访问元组中的元素，不支持修改。
# 元组比列表的访问和处理速度快。所以如果只需要对其中的元素进行访问，而不进行任何修改，建议使用元组而不使用列表。
# 列表不能作为字典的键，而元组可以。
