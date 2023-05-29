# Python中的集合（set）与数学中的集合概念类似，也是用于保存不重复的元素。
# 它有可变集合（set）和不可变集合（frozenset）两种，这里介绍的set集合是无序可变序列
# 在形式上，集合的所有元素都放在一对大括号“{}”中，两个相邻元素间使用逗号“,”分隔。
# 集合最好的应用就是去重，因为集合中的每个元素都是唯一的。

# 创建集合
# 直接使用“{}”创建
# setname = {element 1,element 2,element 3,...,element n}
# setname表示集合的名称，可以是任何符合Python命名规则的标识符；
# element 1、element 2、element 3、element n表示集合中的元素，个数没有限制，并且只要是Python支持的数据类型就可以。
# 在创建集合时，如果输入了重复的元素，Python会自动只保留一个。
set1 = {'1', '2', '3', '4'}
print(type(set1))
print(set1)
set2 = {3, 1, 4, 1, 5, 9, 2, 6}
print(type(set2))
print(set2)
set3 = {'1', 66, ('1', '2')}
print(type(set3))
print(set3)
# 由于Python中的set集合是无序的，所以每次输出时元素的排列顺序可能不同

# 使用set()函数创建(推荐)
# 在Python中，可以使用set()函数将列表、元组等其他可迭代对象转换为集合。
# setname = set(iteration)
# setname：表示集合名称；
# iteration：表示要转换为集合的可迭代对象，可以是列表、元组、range对象等。另外，也可以是字符串，如果是字符串，返回的集合将是包含全部不重复字符的集合。
set1 = set(('1', '2', '3', '4'))
print(set1)
set2 = {3, 1, 4, 1, 5, 9, 2, 6}
print(set2)
set3 = set(('1', 66, ('1', '2')))
print(set3)
# 在创建空集合时，只能使用set()实现，而不能使用一对大括号“{}”实现，这是因为在Python中，直接使用一对大括号“{}”表示创建一个空字典。
emptyset = set()
print(emptyset)

# 向集合中添加和删除元素
# 向集合中添加元素
# setname.add(element)
# setname表示要添加元素的集合；
# element表示要添加的元素内容。这里只能使用字符串、数字及布尔类型的True或者False等，不能使用列表、元组等可迭代对象。
set3.add(True)
print(set3)

# 从集合中删除元素
# 在Python中，可以使用del命令删除整个集合，
del emptyset
# 也可以使用集合的pop()方法或者remove()方法删除一个元素，
# 使用集合的remove()方法时，如果指定的内容不存在，将抛出异常。所以在移除指定元素前，最好先判断其是否存在。
set3.remove(True)
print("set3 after remove:", set3)  # 移除指定元素
set3.pop()  # 删除一个元素
print("set3 after pop:", set3)
# 或者使用集合对象的clear()方法清空集合，即删除集合中的全部元素，使其变为空集合。
set3.clear()  # 清空集合
print("set3 after clear:", set3)

# 集合的交集、并集和差集运算
# 进行交集运算时使用“&”符号；
# 进行并集运算时使用“｜”符号；
# 进行差集运算时使用“-”符号；
# 进行对称差集运算时使用“^”符号。
python = set(['绮梦', '冷伊一', '香凝', '梓轩'])  # 保存选择Python语言的学生名字
c = set(['冷伊一', '零语', '梓轩', '圣博'])  # 保存选择C语言的学生名字
print('选择Python语言的学生有：', python)  # 输出选择Python语言的学生名字
print('选择C语言的学生有：', c)  # 输出选择C语言的学生名字
print('交集运算：', python & c)  # 输出既选择了Python语言又选择C语言的学生名字
print('并集运算：', python | c)  # 输出参与选课的全部学生名字
print('差集运算：', python - c)  # 输出选择了Python语言但没有选择C语言的学生名字
