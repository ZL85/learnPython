# 在Python中，类表示具有相同属性和方法的对象的集合。
# 在使用类时，需要先定义类，然后再创建类的实例，通过类的实例就可以访问类中的属性的方法。

# 定义类
# 在Python中，类的定义使用class关键字来实现
# class ClassName:
#     # 类文档字符串
#     '''
#     类的帮助信息
#     '''
#     statement  # 类体
# ClassName：用于指定类名，一般使用大写字母开头，如果类名中包括两个单词，第二个单词的首字母也大写，这种命名方法也称为“驼峰式命名法”，这是惯例。
# '''类的帮助信息'''：用于指定类的文档字符串，定义该字符串后，在创建类的对象时，输入类名和左侧的括号“(”后，将显示该信息。
# statement：类体，主要由类变量（或类成员）、方法和属性等定义语句组成。如果在定义类时，没想好类的具体功能，也可以在类体中直接使用pass语句代替。
class Demo:
    pass


# 创建类的实例
# class语句本身并不创建该类的任何实例。所以在类定义完成以后，可以创建类的实例，即实例化该类的对象。
# ClassName(parameterlist)
# ClassName是必选参数，用于指定具体的类；
# parameterlist是可选参数，当创建一个类时，没有创建__init__()方法，或者__init__()方法只有一个self参数时，parameterlist可以省略。
demo = Demo()
print(demo)


# 创建__init__()方法
# 在创建类后，通常会创建一个__init__()方法。该方法是一个特殊的方法，类似Java语言中的构造方法。
# 每当创建一个类的新实例时，Python都会自动执行它。
# init()方法必须包含一个self参数，并且必须是第一个参数。
# self参数是一个指向实例本身的引用，用于访问类中的属性和方法。在方法调用时会自动传递实际参数self。
# 因此，当__init__()方法只有一个参数时，在创建类的实例时，就不需要指定实际参数了。
# 在__init__()方法的名称中，开头和结尾处是两个下划线（中间没有空格），这是一种约定，旨在区分Python默认方法和普通方法。
class Demo1:
    def __init__(self):
        print("I'm Demo1 class")


demo1 = Demo1()
print()


# 在__init__()方法中，除了self参数外，还可以自定义一些参数，参数间使用逗号“,”进行分隔。
class Demo2:
    def __init__(self, param1, param2, param3):
        print("I'm Demo2 class")
        print(param1)
        print(param2)
        print(param3)


param1 = "I'm param1"
param2 = "I'm param2"
param3 = "I'm param3"
demo2 = Demo2(param1, param2, param3)
print()


# 创建类的成员并访问
# 类的成员主要由实例方法和数据成员组成。
# 在类中创建了类的成员后，可以通过类的实例进行访问。

# 创建实例方法并访问
# 实例方法是指在类中定义的函数。该函数是一种在类的实例上操作的函数。
# 同__init__()方法一样，实例方法的第一个参数必须是self，并且必须包含一个self参数。
# def functionName(self,parameterlist):
#     block
# functionName：用于指定方法名，一般使用小写字母开头；
# self：必要参数，表示类的实例，其名称可以是self以外的单词，使用self只是一个习惯而已；
# parameterlist：用于指定除self参数以外的参数，各参数间使用逗号“,”进行分隔；
# block：方法体，实现的具体功能。
# 实例方法和Python中的函数的主要区别就是，函数实现的是某个独立的功能，而实例方法是实现类中的一个行为，是类的一部分。
# 实例方法创建完成后，可以通过类的实例名称和点（.）操作符进行访问。
# instanceName.functionName(parametervalue)
# instanceName为类的实例名称；
#   functionName为要调用的方法名称；
# parametervalue表示为方法指定对应的实际参数，其值的个数与创建实例方法中parameterlist的个数相同。
class Demo3:
    def __init__(self, param4, param5, param6):
        print("I'm Demo3 class")
        print(param4)
        print(param5)
        print(param6)

    def testfunc(self, param7):
        print(param7)


param4 = "I'm param4"
param5 = "I'm param5"
param6 = "I'm param6"
demo3 = Demo3(param4, param5, param6)
demo3.testfunc("I'm param7")
print()


# 创建数据成员并访问
# 数据成员是指在类中定义的变量，即属性，根据定义位置，又可以分为类属性和实例属性。

# 类属性
# 类属性是指定义在类中，并且在函数体外的属性。类属性可以在类的所有实例之间共享值，也就是在所有实例化的对象中公用。
# 类属性可以通过类名称或者实例名访问。
class Demo4:
    param8 = "I'm param8"
    param9 = "I'm param9"
    param10 = "I'm param10"

    def __init__(self):
        print("I'm Demo4 class")
        print(self.param8)
        print(self.param9)
        print(self.param10)


demo4 = Demo4()
# 在Python中除了可以通过类名称访问类属性，还可以动态地为类和对象添加属性。
Demo4.param11 = "I'm param11"
print(demo4.param11)
# 除了可以动态地为类和对象添加属性，也可以修改类属性。修改结果将作用于该类的所有实例。
Demo4.param10 = "I'm modified param10"
print(demo4.param10)
print()


# 实例属性
# 实例属性是指定义在类的方法中的属性，只作用于当前实例中。
class Demo5:
    def __init__(self):
        self.param12 = "I'm param12"
        self.param13 = "I'm param13"
        self.param14 = "I'm param14"

        print("I'm Demo5 class")
        print(self.param12)
        print(self.param13)
        print(self.param14)


demo5 = Demo5()
# 实例属性只能通过实例名访问。如果通过类名访问实例属性，将抛出异常。
print()

# 对于实例属性也可以通过实例名称修改，与类属性不同，通过实例名称修改实例属性后，并不影响该类的另一个实例中相应的实例属性的值。
demo6 = Demo5()
print()
demo6.param12 = "I'm modified param12"
print(demo5.param12)
print(demo6.param12)
print()


# 访问限制
# 在类的内部可以定义属性和方法，而在类的外部则可以直接调用属性或方法来操作数据，从而隐藏了类内部的复杂逻辑。
# 但是，Python并没有对属性和方法的访问权限进行限制。
# 为了保证类内部的某些属性或方法不被外部访问，可以在属性或方法名前面添加单下划线（_name）、双下划线（__name）或首尾加双下划线（__name__），从而限制访问权限。

# _name：以单下划线开头的表示protected（保护）类型的成员，只允许类本身和子类进行访问，但不能使用“from module import *”语句导入。
class Demo7:
    _member = "I'm protected member"

    def __init__(self):
        print(self._member)


demo7 = Demo7()
print(demo7._member)
print()


# __name：双下划线表示private（私有）类型的成员，只允许定义该方法的类本身进行访问，而且不能通过类的实例进行访问，但是可以通过“类的实例名.类名__xxx”方式访问。
class Demo8:
    __member = "I'm private member"

    def __init__(self):
        print(self.__member)


demo8 = Demo8()
# print(demo8.__member) # 运行报错，无法通过类的实例进行访问

# __name__：首尾双下划线表示定义特殊方法，一般是系统定义名字，如__init__()。

# 属性（property）
# 这里介绍的属性是一种特殊的属性，访问它时将计算它的值。另外，该属性还可以为属性添加安全保护机制。

# 创建用于计算的属性
# 在Python中，可以通过@property（装饰器）将一个方法转换为属性，从而实现用于计算的属性。
# 将方法转换为属性后，可以直接通过方法名来访问方法，而不需要再添加一对小括号“()”，这样可以让代码更加简洁。
# @property
# def methodname(self):
#     block
# methodname：用于指定方法名，一般使用小写字母开头。该名称最后将作为创建的属性名。
# self：必要参数，表示类的实例。
# block：方法体，实现的具体功能。在方法体中，通常以return语句结束，用于返回计算结果。


