# 列表是Python中内置的可变序列。
# 在形式上，列表的所有元素都放在一对中括号“[]”中，两个相邻元素间使用逗号“,”分隔。
# 在内容上，可以将整数、实数、字符串、列表、元组等任何类型的内容放入列表中，并且同一个列表中，元素的类型可以不同。
import datetime
import random

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
print()
# 添加、修改和删除列表元素

# 添加元素
# append()方法用于在列表的末尾追加元素
# listname.append(obj)
# listname为要添加元素的列表名称；
# obj为要添加到列表末尾的对象。
list1.append(20)
print(list1)

# listname.extend(seq)
# listname为原列表；
# seq为要添加的列表。
# 语句执行后，seq2的内容将追加到listname的后面。
list2 = list(range(0, 10, 2))
list2.extend(list1)
print(list2)

# 修改元素
# 修改列表中的元素只需要通过索引获取该元素，然后再为其重新赋值即可
list2[0] = 22
print(list2)

# 删除元素

# 根据索引删除
# 删除列表中的指定元素和删除列表类似，也可以使用del语句实现。所不同的就是在指定列表名称时，换为列表元素。
del list2[0]
print(list2)

# 根据元素值删除
# 如果想要删除一个不确定其位置的元素（即根据元素值删除），可以使用列表对象的remove()方法实现。
list2.remove(20)
print(list2)
# 在使用remove()方法删除元素前，最好先判断该元素是否存在，改进后的代码如下：
if list2.count(18) > 0:
    list2.remove(18)
print(list2)

# 对列表进行统计计算

# 获取指定元素出现的次数
# 列表对象的count()方法可以获取指定元素在列表中的出现次数
# listname.count(obj)
# listname表示列表的名称；
# obj表示要判断是否存在的对象，这里只能进行精确匹配，即不能是元素值的一部分。
num = list2.count(10)
print(f"10 appears {num} times in list2")

# 获取指定元素首次出现的下标
# 列表对象的index()方法可以获取指定元素在列表中首次出现的位置（即索引）
# listname.index(obj)
# listname：表示列表的名称；
# obj：表示要查找的对象，这里只能进行精确匹配。如果指定的对象不存在，则抛出异常；
# 返回值：首次出现的索引值。
pos = list2.index(10)
print(f"The index position of 10 that first appears in list2 is {pos}")

# 统计数值列表的元素和
# sum()函数用于统计数值列表中各元素的和
# sum(iterable[,start])
# iterable：表示要统计的列表；
# start：表示统计结果是从哪个数开始（即将统计结果加上start所指定的数），是可选参数，如果没有指定，默认值为0。
total = sum(list2)
print(f"the sum of elements in list2 is {total}")

# 对列表进行排序
# 使用列表对象的sort()方法实现
# listname.sort(key=None,reverse=False)
# listname：表示要进行排序的列表；
# key：表示指定一个从每个列表元素中提取一个比较键（例如，设置“key=str.lower”表示在排序时不区分字母大小写）；
# reverse：可选参数，如果将其值指定为True，则表示降序排列，如果为False，则表示升序排列。默认为升序排列。
list3 = [98, 69, 77, 105, 120, 96, 84, 89, 95, 100]
print("the original list3: ", list3)
list3.sort()
print("the sorted list3 in ascending order: ", list3)
list3.sort(reverse=True)
print("the sorted list3 in descending order: ", list3)

# 使用sort()方法对字符串列表进行排序时，采用的规则是先对大写字母进行排序，然后再对小写字母进行排序。
# 如果想要对字符串列表进行排序（不区分大小写时），需要指定其key参数。
char = ['cat', 'Tom', 'Angela', 'pet']
char.sort()
print("case-sensitive：", char)
char.sort(key=str.lower)
print("Not case-sensitive：", char)

# 使用内置的sorted()函数实现
# 使用该函数进行排序后，原列表的元素顺序不变。
# sorted(iterable,key=None,reverse=False)
# iterable：表示要进行排序的列表名称；
# key：表示指定从每个元素中提取一个用于比较的键（例如，设置“key=str.lower”表示在排序时不区分字母大小写）；
# reverse：可选参数，如果将其值指定为True，则表示降序排列，如果为False，则表示升序排列。默认为升序排列。
list4 = [98, 69, 77, 105, 120, 96, 84, 89, 95, 100]
list4_as = sorted(list4)
print("the sorted list4 in ascending order: ", list4_as)
list4_des = sorted(list4, reverse=True)
print("the sorted list4 in descending order: ", list4_des)
print("list4 after sort: ", list4)

# 列表对象的sort()方法和内置sorted()函数的作用基本相同，
# 所不同的就是使用sort()方法时，会改变原列表的元素排列顺序，但是使用sorted()函数时，会建立一个原列表的副本，该副本为排序后的列表。

# 列表推导式

# 生成指定范围的数值列表
# list = [Expression for var in range]
# list：表示生成的列表名称；
# Expression：表达式，用于计算新列表的元素；
# var：循环变量；
# range：采用range()函数生成的range对象。
randomnum = [random.randint(10, 100) for i in range(10)]
print("The generated random number is：", randomnum)

# 根据列表生成指定需求的列表
# newlist = [Expression for var in list]
# newlist：表示新生成的列表名称；
# Expression：表达式，用于计算新列表的元素；
# var：变量，值为后面列表的每个元素值；
# list：用于生成新列表的原列表。
price = [1200, 5330, 2988, 6200, 1998, 8888]
sale = [int(x * 0.5) for x in price]
print("original price：", price)
print("50% discounted price：", sale)

# 从列表中选择符合条件的元素组成新的列表
# # newlist = [Expression for var in list if condition]
# newlist：表示新生成的列表名称；
# Expression：表达式，用于计算新列表的元素；
# var：变量，值为后面列表的每个元素值；
# list：用于生成新列表的原列表；
# condition：条件表达式，用于指定筛选条件。
price = [1200, 5330, 2988, 6200, 1998, 8888]
sale = [x for x in price if x > 5000]
print("original list：", price)
print("price higher than 5000：", sale)

# 二维列表
# 直接定义二维列表
# 二维列表中的信息以行和列的形式表示，第一个下标代表元素所在的行，第二个下标代表元素所在的列。
# 在Python中，二维列表就是包含列表的列表。即一个列表的每个元素又都是一个列表。
# listname = [[元素11, 元素12, 元素13, ..., 元素1n],
#             [元素21, 元素22, 元素23, ..., 元素2n],
#             ...,
#             [元素n1, 元素n2, 元素n3, ..., 元素nn]]
# listname：表示生成的列表名称；
# [元素11，元素12，元素13，...，元素1n]：表示二维列表的第一行，也是一个列表。其中元素11、元素12……代表第一行中的列；
# [元素21，元素22，元素23，...，元素2n]：表示二维列表的第二行；
# [元素n1，元素n2，元素n3，...，元素nn]：表示二维列表的第n行。
# 创建一个包含4行5列的二维列表
list5 = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]
print(list5)

# 使用嵌套的for循环创建
arr = []  # 创建一个空列表
for i in range(4):
    arr.append([])  # 在空列表中再添加一个空列表
    for j in range(5):
        arr[i].append(j)  # 为内层列表添加元素
print(arr)

# 使用列表推导式创建(推荐)
arr = [[j for j in range(5)] for i in range(4)]
print(arr)

# 创建二维数组后，可以通过以下语法格式访问列表中的元素。
# listname[下标1][下标2]
# listname：表示列表名称；
# 下标1：表示列表中第几行，下标值从0开始，即第一行的下标为0；
# 下标2：表示列表中第几列，下标值从0开始，即第一列的下标为0。
print("The element of the second column of the first row in list5 is", list5[0][1])
