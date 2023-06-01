# 基本输入输出
# 在Python中，使用内置函数input()可以接收用户的键盘输入
# 在Python 3.x中，无论输入的是数字还是字符都将被作为字符串读取。如果想要接收数值，需要把接收到的字符串进行类型转换
# 在Python中，使用内置的print()函数可以将结果输出到IDLE或者标准控制台上
int1 = input("please input an int num: ")
print(type(int1))
int2 = int(int1)
print(type(int2))
print("your input is " + int1)

# 在Python中，默认情况下，一条print()语句输出后会自动换行，如果想要一次输出多个内容，而且不换行，可以将要输出的内容使用英文半角的逗号分隔。
print(1024, end=" ")  # 不换行
print(2048)  # 默认换行
print(1024, 2048)

# 在输出时，也可以把结果输出到指定文件
fp = open(r"D:\JetBrains\PyCharm Projects\learnPython\chapter2\testIO.txt", 'a+')
print("thi is a test of IO", file=fp)
fp.close()