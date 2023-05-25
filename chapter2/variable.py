# 保留字
# ['False', 'None', 'True', 'and', 'as',
# 'assert', 'async', 'await', 'break', 'class',
# 'continue', 'def', 'del', 'elif', 'else',
# 'except', 'finally', 'for', 'from', 'global',
# 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']
# Python中所有保留字是区分字母大小写的。
import keyword
print(keyword.kwlist)

# 标识符
# 命名规则如下：
# 由字母、下划线“_”和数字组成，并且第一个字符不能是数字。目前Python中只允许使用ISO-Latin字符集中的字符A~Z和a~z
#     Python的标识符中不能包含空格、@、%和$等特殊字符
# 不能使用Python中的保留字
# 区分字母大小写
# Python中以下划线开头的标识符有特殊意义，一般应避免使用相似的标识符。
#     以单下划线开头的标识符（如_width）表示不能直接访问的类属性，另外，也不能通过from xxx import *导入
#     以双下划线开头的标识符（如__add）表示类的私有成员
#     以双下划线开头和结尾的是Python里专用的标识，例如，init()表示构造函数

# 变量就是程序运行过程中，值能改变的量
# 在Python中，严格意义上变量应该称为“名字”，也可以理解为标签。当把一个值赋给一个名字(i=6)时，i就称为变量
# 对于变量的命名应遵循以下几条规则：
# 变量名必须是一个有效的标识符
# 变量名不能使用Python中的保留字
# 慎用小写字母l和大写字母O
# 应选择有意义的单词作为变量名
# 在Python中，不需要先声明变量名及其类型，直接赋值即可创建各种类型的变量
i = 6
f = 3.14
s = "hello"
# 在Python语言中，使用内置函数type()可以返回变量类型
print(type(i))
print(type(f))
print(type(s))
# Python是一种动态类型的语言，变量的类型可以随时变化
i = True
print(type(i))

# 在Python中，允许多个变量指向同一个值
# 将两个变量都赋值为数字2048，再分别应用内置函数id()获取变量的内存地址，将得到相同的结果
i1 = 2048
i2 = 2048
print(id(i1))
print(id(i2))

# 常量就是程序运行过程中，值不能改变的量
# 在PEP 8规范中定义了常量的命名规范为大写字母和下划线组成
