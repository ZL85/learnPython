# 在程序运行过程中，经常会遇到各种各样的错误，这些错误统称为“异常”。

# Python中常见的异常。
# 异常              描述
# NameError         尝试访问一个没有声明的变量引发的错误
# IndexError        索引超出序列范围引发的错误
# IndentationError  缩进错误
# ValueError        传入的值错误
# KeyError          请求一个不存在的字典关键字引发的错误
# IOError           输入输出错误（如要读取的文件不存在)
# ImportError       当import 语句无法找到模块或from无法在模块中找到相应的名称时引发的错误
# AttributeError    尝试访问未知的对象属性引发的错误
# TypeError         类型不合适引发的错误
# MemoryError       内存不足
# ZeroDivisionError 除数为0引发的错误

# 异常处理语句
# try…except语句
# 在Python中，提供了try…except语句捕获并处理异常。
# 在使用时，把可能产生异常的代码放在try语句块中，把处理结果放在except语句块中，
# 这样，当try语句块中的代码出现错误，就会执行except语句块中的代码，如果try语句块中的代码没有错误，那么except语句块将不会执行。
# try:
#     block1
# except [ExceptionName [as alias]]：
#     block2
# block1：表示可能出现错误的代码块。
# ExceptionName[as alias]：可选参数，用于指定要捕获的异常，如果需要同时处理多个异常，可以将异常放入括号内并用逗号隔开。
# 其中，ExceptionName表示要捕获的异常名称，如果在其右侧加上asalias，则表示为当前的异常指定一个别名，通过该别名，可以记录异常的具体内容。
# 在使用try…except语句捕获异常时，如果在except后面不指定异常名称，则表示捕获全部异常。
# block2：表示进行异常处理的代码块。在这里可以输出固定的提示信息，也可以通过别名输出异常的具体内容。
# 使用try…except语句捕获异常后，当程序出错时，输出错误信息后，程序会继续执行。

# try…except…else语句
# 在原来try…except语句的基础上再添加一个else子句，用于指定当try语句块中没有发现异常时要执行的语句块。

# try…except…finally语句
# 完整的异常处理语句应该包含finally代码块，通常情况下，无论程序中有无异常产生，finally代码块中的代码都会被执行。
# try:
#     block1
# except [ExceptionName [as alias]]：
#     block2
# finally:
#     block3

# 如果程序中有一些在任何情形中都必须执行的代码，那么就可以将它们放在finally语句的区块中。
# 使用except子句是为了允许处理异常。无论是否引发了异常，使用finally子句都可以执行清理代码。
# 如果分配了昂贵或有限的资源（如打开文件），则应将释放这些资源的代码放置在finally块中。

# 使用raise语句抛出异常
# 如果某个函数或方法可能会产生异常，但不想在当前函数或方法中处理这个异常，则可以使用raise语句在函数或方法中抛出异常。
# raise [ExceptionName[(reason)]]
# ExceptionName[(reason)]为可选参数，用于指定抛出的异常名称，以及异常信息的相关描述。如果省略，就会把当前的错误原样抛出。
# ExceptionName(reason)参数中的“(reason)”也可以省略，如果省略，则在抛出异常时，不附带任何描述信息。
# 在应用raise抛出异常时，要尽量选择合理的异常对象，而不应该抛出一个与实际内容不相关的异常。

# 程序调试
# 作为一名程序员，掌握一定的程序调试方法，可以说是一项必备技能。
# 使用assert语句调试程序
# 在程序开发过程中，除了使用开发工具自带的调试工具进行调试外，还可以在代码中通过print()函数把可能出现问题的变量输出进行查看，但是这种方法会产生很多垃圾信息。所以调试之后还需要将其删除，比较麻烦。
# assert的中文意思是断言，它一般用于对程序某个时刻必须满足的条件进行验证。
# assert expression [,reason]
# expression：条件表达式，如果该表达式的值为真，什么都不做，如果为假，则抛出AssertionError异常。
# reason：可选参数，用于对判断条件进行描述，为了以后更好地知道哪里出现了问题。
# 通常情况下，assert语句可以和异常处理语句结合使用。
# assert语句只在调试阶段有效。我们可以通过在执行python命令时加入-O（大写）参数来关闭assert语句。
