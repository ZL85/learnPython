# coding:utf-8
# 重复一定次数的循环，称为计次循环，如for循环

# 进行数值循环
# range()函数是Python内置的函数，用于生成一系列连续的整数
# range(start,end,step)
# start：用于指定计数的起始值，可以省略，如果省略则从0开始。
# end：用于指定计数的结束值（但不包括该值），不能省略。
# step：用于指定步长，即两个数之间的间隔，可以省略，如果省略则表示步长为1
# 当range()函数中只有一个参数时，即表示指定计数的结束值。
# 例如，使用下面的for循环语句，将输出10以内的所有奇数。
for i in range(1, 10, 2):
    print(i, end=' ')
print()
# 遍历字符串
# 将横向显示的字符串转换为纵向显示。
string = 'I CAN!'
print(string)
for ch in string:
    print(ch)

# for循环语句还可以用于迭代（遍历）列表、元组、集合和字典等

# 在Python中，for循环和while循环都可以进行循环嵌套。

# 打印九九乘法表
for i in range(1, 10):  # 输出9行
    for j in range(1, i + 1):  # 输出与行数相等的列
        print(str(j) + "×" + str(i) + "=" + str(i * j) + "\t", end='')
    print('')  # 换行

# break语句
# break语句可以终止当前的循环，包括while和for在内的所有控制语句
# 解决黄蓉难倒瑛姑的数学题（for循环改进版）
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？")
for number in range(100):
    print(number,end=" ")
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:  # 判断是否符合条件
        print("答曰：这个数是", number)  # 输出符合条件的数
        break  # 跳出for循环

# continue语句
# continue语句的作用没有break语句强大，它只能中止本次循环而提前进入下一次循环中
# 计算100以内所有偶数的和
total = 0  # 用于保存累加和的变量
for number in range(1, 100):
    if number % 2 == 1:  # 判断是否符合条件
        continue  # 继续下一次循环
    total += number  # 累加偶数的和
print("1到100之间（不包括100）的偶数和为：", total)  # 输出累加结果

# 第3行代码实现的是：当所判断的数字是奇数时，会执行第4行的continue语句，跳过后面的累加操作，直接进入下一次循环。

# pass语句
# 在Python中还有一个pass语句，表示空语句。它不做任何事情，一般起到占位作用
# 例如，在应用for循环输出1～10（不包括10）的偶数时，在不是偶数时，应用pass语句占个位置，方便以后对不是偶数的数进行处理。代码如下：
for i in range(1, 10):
    if i % 2 == 0:  # 判断是否为偶数
        print(i, end=' ')
    else:  # 不是偶数
        pass  # 占位符，不做任何事情
