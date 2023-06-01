# 字典（dictionary）和列表类似，也是可变序列，不过与列表不同，它是无序的可变序列，保存的内容是以“键-值对”的形式存放的。
# 键是唯一的，而值可以有多个。字典在定义一个包含多个命名字段的对象时，很有用。
# Python中的字典相当于Java或者C++中的Map对象。
import random

# 字典的主要特征如下：

# 通过键而不是通过索引来读取。
# 字典有时也称为关联数组或者散列表（hash）。它是通过键将一系列的值联系起来的，这样就可以通过键从字典中获取指定项，但不能通过索引来获取。

# 字典是任意对象的无序集合。
# 字典是无序的，各项是从左到右随机排序的，即保存在字典中的项没有特定的顺序。这样可以提高查找顺序。

# 字典是可变的，并且可以任意嵌套。
# 字典可以在原处增长或者缩短（无须生成一份拷贝），并且它支持任意深度的嵌套（即它的值可以是列表或者其他的字典）。

# 字典中的键必须唯一。
# 不允许同一个键出现两次，如果出现两次，则后一个值会被记住。

# 字典中的键必须不可变。
# 字典中的键是不可变的，所以可以使用数字、字符串或者元组，但不能使用列表。

# 字典的创建和删除
# 定义字典
# 每个元素都包含两个部分——“键”和“值”，并且在“键”和“值”之间使用冒号分隔，相邻两个元素使用逗号分隔，所有元素放在一个大括号“{}”中。
# dictionary = {'key1':'value1', 'key2':'value2', ..., 'keyn':'valuen',}
# dictionary：表示字典名称；
# key1, key2, ..., keyn：表示元素的键，必须是唯一的，并且不可变，例如可以是字符串、数字或者元组；
# value1, value2, ..., valuen：表示元素的值，可以是任何数据类型，不是必须唯一。
dict1 = {'QQ': '0123456789', 'WeChat': '0123456789', 'Email': '0123456789@163.com'}
print(type(dict1))
print(dict1)

# 在Python中，可以使用下面两种方法创建空字典。
emptydict = {}
print(emptydict)
emptydict = dict()
print(emptydict)

# 通过映射函数创建字典
# dictionary = dict(zip(list1,list2))
# dictionary：表示字典名称。
# zip()函数：用于将多个列表或元组对应位置的元素组合为元组，并返回包含这些内容的zip对象。
# 如果想得到元组，可以将zip对象使用tuple()函数转换为元组；如果想得到列表，则可以使用list()函数将其转换为列表。
# list1：表示一个列表，用于指定要生成字典的键。
# list2：表示一个列表，用于指定要生成字典的值。如果list1和list2的长度不同，则与最短的列表长度相同。
contact = ['QQ', 'WeChat', 'Email']
info = ['0123456789', '0123456789', '0123456789@163.com']
dict2 = dict(zip(contact, info))
print(dict2)

# 通过给定的“键-值对”创建字典
# dictionary = dict(key1=value1,key2=value2,...,keyn=valuen)
# dictionary：表示字典名称；
# key1, key2, ..., keyn：表示元素的键，必须是唯一的，并且不可变，例如可以是字符串、数字或者元组；
# value1, value2, ..., valuen：表示元素的值，可以是任何数据类型，不是必须唯一。
dict3 = dict(n0='0', n1='1', n2='2', n3='3')
print(dict3)

# 在Python中，还可以使用dict对象的fromkeys()方法创建值为空的字典
# dictionary = dict.fromkeys(list)
# dictionary：表示字典名称；
# list1：作为字典的键的列表。
emptyvaluedict = dict.fromkeys(contact)
print(emptyvaluedict)

# 另外，还可以通过已经存在的元组(作为键)和列表(作为值)创建字典。
dict4 = {tuple(contact): info}
print(dict4)

# 不再需要的字典也可以使用del命令删除
del emptydict

# 可以使用字典对象的clear()方法删除字典的全部元素
dict3.clear()
print(dict3)

# 还可以使用字典对象的pop()删除并返回指定“键”的元素，以及使用字典对象的popitem()方法删除并返回字典中的一个元素。
dict1.pop('QQ')
print(dict1)
key = dict1.popitem()
print(key)
print(dict1)

# 访问字典
# 在Python中，可以直接使用print()函数将字典的内容输出。
# 在Python中，访问字典的元素可以通过下标的方式实现，与列表和元组不同，这里的下标不是索引号，而是键。
# 在使用该方法获取指定键的值时，如果指定的键不存在，使用if语句对不存在的情况进行处理，即给一个默认值。
print(dict2['QQ'] if 'QQ' in dict2 else 'non-existent key')

# Python中推荐的方法是使用字典对象的get()方法获取指定键的值。
# dictionary.get(key[,default])
# dictionary为字典对象，即要从中获取值的字典；key为指定的键；
# default为可选项，用于当指定的键不存在时，返回一个默认值，如果省略，则返回None。
print(dict2.get('Wechat', 'non-existent key'))

# 遍历字典
# Python提供了遍历字典的方法，通过遍历可以获取字典中的全部“键-值对”。
# 使用字典对象的items()方法可以获取字典的“键-值对”列表。
# dictionary.items()
# dictionary为字典对象；返回值为可遍历的“键-值对”元组列表。想要获取到具体的“键-值对”，可以通过for循环遍历该元组列表。
for item in dict2.items():
    print(item)
# 上面的示例得到的是元组中的各个元素，如果想要获取到具体的每个键和值，可以使用下面的代码进行遍历。
for key, value in dict2.items():
    print(f"{key}:{value}")

# 字典对象还提供了values()和keys()方法，用于返回字典的“值”和“键”列表，也需要通过for循环遍历该字典列表，获取对应的值和键。
for key in dict2.keys():
    print(key)
for value in dict2.values():
    print(value)

# 添加、修改和删除字典元素
# 字典是可变序列，所以可以随时在其中添加“键-值对”
# dictionary[key] = value
# dictionary：表示字典名称；
# key：表示要添加元素的键，必须是唯一的，并且不可变；例如可以是字符串、数字或者元组；
# value：表示元素的值，可以是任何数据类型，不是必须唯一。
dict2['Tel'] = '0123456789'
print(dict2)

# 如果新添加元素的“键”与已经存在的“键”重复，那么将使用新的“值”替换原来该“键”的值，这也相当于修改字典的元素。
dict2['QQ'] = '9876543210'
print(dict2)

# 当字典中的某个元素不需要时，可以使用del命令将其删除。
if 'Email' in dict2:
    del dict2['Email']
print(dict2)

# 字典推导式
randomdict = {i: random.randint(10, 100) for i in range(1, 5)}
print("the generated dictionary：", randomdict)

# 使用字典推导式也可根据列表生成字典。
dict5 = {i: j for i, j in zip(contact, info)}
print(dict5)
