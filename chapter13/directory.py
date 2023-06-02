# 目录也称文件夹，用于分层保存文件。
# 通过目录可以分门别类地存放文件。我们也可以通过目录快速找到想要的文件。

# 在Python中，并没有提供直接操作目录的函数或者对象，而是需要使用内置的os模块及其子模块os.path实现。
# os模块是Python内置的与操作系统功能和文件系统相关的模块。
# 该模块中的语句的执行结果通常与操作系统有关，在不同操作系统上运行，可能会得到不一样的结果。
import os
import shutil

# 导入os模块后，可以使用该模块提供的通用变量获取与系统有关的信息。
# name：用于获取操作系统类型。
print(os.name)
# 如果os.name的输出结果为nt，则表示是Windows操作系统；如果是posix，则表示是Linux、UNIX或Mac OS操作系统。

# linesep：用于获取当前操作系统上的换行符。
print(os.linesep)

# sep：用于获取当前操作系统所使用的路径分隔符。
print(os.sep)

# os模块还提供了一些操作目录的函数
# 函数                              说明
# getcwd()                          返回当前的工作目录
# listdir(path)                     返回指定路径下的文件和目录信息
# mkdir(path [,mode])               创建目录
# makedirs(path1/path2...[ ,mode])  创建多级目录
# rmdir(path)                       删除目录
# removedirs(path1/path2...)        删除多级目录
# chdir(path)                       把path设置为当前工作目录
# walk(top[,topdown[,onerror]])     遍历目录树，该方法返回一个元组，包括所有路径名、所有目录列表和文件列表3个元素

# os.path模块也提供了一些操作目录的函数
# 函数              说明
# abspath(path)     用于获取文件或目录的绝对路径
# exists(path)      用于判断目录或者文件是否存在，如果存在则返回True，否则返回False
# join(path,name)   将目录与目录或者文件名拼接起来
# splitext()        分离文件名和扩展名
# basename(path)    从一个目录中提取文件名
# dirname(path)     从一个路径中提取文件路径，不包括文件名
# isdir(path)       用于判断是否为有效路径

# 路径
# 用于定位一个文件或者目录的字符串被称为一个路径。

# 相对路径
# 当前工作目录是指当前文件所在的目录。
# 在Python中，可以通过os模块提供的getcwd() 函数获取当前工作目录。
print(os.getcwd())
# 相对路径就是依赖于当前工作目录的。
# 如果在当前工作目录下有一个名称为test.txt的文件，那么在打开这个文件时，就可以直接写上文件名，这时采用的就是相对路径。
# 在Python中，指定文件路径时需要对路径分隔符“\”进行转义， 即将路径中的“\” 替换为“\\” 。
# 在指定文件路径时，也可以在表示路径的字符串前面加上字母r（或R），那么该字符串将原样输出，这时路径中的分隔符就不需要再转义了。
with open('test.txt', 'r') as t:
    print(t.read())

# 绝对路径
# 绝对路径是指在使用文件时指定文件的实际路径。它不依赖于当前工作目录。
# 在Python中，可以通过os.path模块提供的abspath()函数获取一个文件的绝对路径。
print(os.path.abspath('test.txt'))
with open(r'D:\JetBrains\PyCharm Projects\learnPython\chapter13\test.txt', 'r') as t:
    print(t.read())

# 拼接路径
# 如果想要将两个或者多个路径拼接到一起组成一个新的路径，可以使用os.path模块提供的join()函数实现。
# os.path.join(path1[,path2[,...]])
# path1、path2用于代表要拼接的文件路径，这些路径间使用逗号进行分隔。
# 如果在要拼接的路径中没有一个绝对路径，那么最后拼接出来的将是一个相对路径。
# 使用os.path.join()函数拼接路径时，并不会检测该路径是否真实存在。
print(os.path.join("E:\\PyCharm Projects", "test.txt"))
# 把两个路径拼接为一个路径时，不要直接使用字符串拼接，而是使用os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。

# 判断目录是否存在
# 在Python中，有时需要判断给定的目录是否存在，这时可以使用os.path模块提供的exists()函数实现。
# os.path.exists(path)
# path为要判断的目录，可以采用绝对路径，也可以采用相对路径。
# 返回值：如果给定的路径存在，则返回True，否则返回False。
print(os.path.exists('E:\\PyCharm Projects'))

# os.path.exists()函数除了可以判断目录是否存在，还可以判断文件是否存在。
print(os.path.exists('E:\\PyCharm Projects\\test.txt'))

# 创建目录

# 创建一级目录
# 创建一级目录是指一次只能创建一级目录。
# 在Python中，可以使用os模块提供的mkdir()函数实现。
# 通过该函数只能创建指定路径中的最后一级目录，如果该目录的上一级不存在，则抛出FileNotFoundError异常。
# os.mkdir(path, mode=0o777)
# path：用于指定要创建的目录，可以使用绝对路径，也可以使用相对路径。
# mode：用于指定数值模式，默认值为0777。该参数在非UNIX系统上无效或被忽略。
# 如果创建的路径已经存在，则将抛出FileExistsError异常，可以在创建目录前，先判断指定的目录是否存在，只有当目录不存在时才创建。
os.mkdir('D:\\JetBrains\\PyCharm Projects\\learnPython\\chapter13\\test1')

# 创建多级目录
# 如果想创建多级，可以使用os模块提供的makedirs()函数，该函数用于采用递归的方式创建目录。

# os.makedirs(name, mode=0o777)
# name：用于指定要创建的目录，可以使用绝对路径，也可以使用相对路径。
# mode：用于指定数值模式，默认值为0777。该参数在非UNIX系统上无效或被忽略。
os.makedirs('D:\\JetBrains\\PyCharm Projects\\learnPython\\chapter13\\test2\\mak\\dir')

# 删除目录
# 删除目录可以使用os模块提供的rmdir()函数实现。
# 通过rmdir()函数删除目录时，只有当要删除的目录为空时才起作用。
# os.rmdir(path)
# path为要删除的目录，可以使用相对路径，也可以使用绝对路径。
os.rmdir('D:\\JetBrains\\PyCharm Projects\\learnPython\\chapter13\\test1')
os.rmdir('D:\\JetBrains\\PyCharm Projects\\learnPython\\chapter13\\test2\\mak\\dir')
os.rmdir('D:\\JetBrains\\PyCharm Projects\\learnPython\\chapter13\\test2\\mak')
os.rmdir('D:\\JetBrains\\PyCharm Projects\\learnPython\\chapter13\\test2')

# 使用rmdir()函数只能删除空的目录，如果想要删除非空目录，则需要使用Python内置的标准模块shutil的rmtree()函数实现。
os.makedirs('D:\\JetBrains\\PyCharm Projects\\learnPython\\chapter13\\test2\\mak\\dir')
shutil.rmtree('D:\\JetBrains\\PyCharm Projects\\learnPython\\chapter13\\test2')

# 遍历目录
# 在Python中，遍历就是对指定的目录下的全部目录（包括子目录）及文件运行一遍。
# 在Python中，os模块的walk()函数用于实现遍历目录的功能。
# os.walk(top[, topdown][, onerror][, followlinks])
# top：用于指定要遍历内容的根目录。
# topdown：可选参数，用于指定遍历的顺序，如果值为True，表示自上而下遍历（即先遍历根目录）；如果值为False，表示自下而上遍历（即先遍历最后一级子目录）。默认值为True。
# onerror：可选参数，用于指定错误处理方式，默认为忽略，如果不想忽略，也可以指定一个错误处理函数。通常情况下采用默认。
# followlinks：可选参数，默认情况下，walk()函数不会向下转换成解析到目录的符号链接，将该参数值设置为True，表示用于指定在支持的系统上访问由符号链接指向的目录。
# 返回值： 返回一个包括3 个元素（ dirpath, dirnames, filenames）的元组生成器对象。其中，dirpath表示当前遍历的路径，是一个字符串；dirnames表示当前路径下包含的子目录，是一个列表；filenames表示当前路径下包含的文件，也是一个列表。
