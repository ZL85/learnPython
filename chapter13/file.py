# 在变量、序列和对象中存储的数据是暂时的，程序结束后就会丢失。
# 为了能够长时间地保存程序中的数据，需要将程序中的数据保存到磁盘文件中。
# Python提供了内置的文件对象和对文件，以及目录进行操作的内置模块。
import os

# 基本文件操作
# 在Python中，内置了文件（File）对象。
# 在使用文件对象时，首先需要通过内置的open()方法创建一个文件对象，然后通过该对象提供的方法进行一些基本文件操作。

# 创建和打开文件
# 在Python中，想要操作文件需要先创建或者打开指定的文件并创建文件对象。
# 这可以通过内置的open()函数实现。
# file = open(filename[,mode[,buffering]])
# file：被创建的文件对象。
# filename：要创建或打开文件的文件名称，需要使用单引号或双引号括起来。如果要打开的文件和当前文件在同一个目录下，那么直接写文件名即可，否则需要指定完整路径。
# mode：可选参数，用于指定文件的打开模式。默认的打开模式为只读（即r）。
# buffering：可选参数，用于指定读写文件的缓冲模式，值为0表示不缓存；值为1表示缓存；如果大于1，则表示缓冲区的大小。默认为缓存模式。

# 值  说明                                                                                               注意
# r   以只读模式打开文件。文件的指针将会放在文件的开头
# rb  以二进制格式打开文件，并且采用只读模式。文件的指针将会放在文件的开头。一般用于非文本文件，如图片、声音等
# r+  打开文件后，可以读取文件内容，也可以写入新的内容覆盖原有内容（从文件开头进行覆盖)
# rb+ 以二进制格式打开文件，并且采用读写模式。文件的指针将会放在文件的开头。一般用于非文本文件，如图片、声音等   文件必须存在
# w   以只写模式打开文件
# wb  以二进制格式打开文件，并且采用只写模式。一般用于非文本文件，如图片、声音等                               文件存在，则将其覆盖,否则创建新文件

# open()方法经常实现以下几个功能。

# 打开一个不存在的文件时先创建该文件
# 以二进制形式打开文件
# 打开文件时指定编码方式

# 关闭文件
# 打开文件后，需要及时关闭，以免对文件造成不必要的破坏。
# 关闭文件可以使用文件对象的close()方法实现。
# file.close()
# file为打开的文件对象
# close()方法先刷新缓冲区中还没有写入的信息，然后再关闭文件，这样可以将没有写入文件的内容写入文件中。

# 打开文件时使用with语句
# 打开文件后，要及时将其关闭。如果忘记关闭，可能会带来意想不到的问题。
# 如果在打开文件时抛出了异常，那么将导致文件不能被及时关闭。
# 使用Python提供的with语句，从而实现在处理文件时，无论是否抛出异常，都能保证with语句执行完毕后关闭已经打开的文件。
# with expression as target:
#     with-body
# expression：用于指定一个表达式，这里可以是打开文件的open()函数。
# target：用于指定一个变量，并且将expression的结果保存到该变量中。
# with-body：用于指定with语句体，其中可以是执行with语句后相关的一些操作语句。
# 如果不想执行任何语句，可以直接使用pass语句代替。

# 写入文件内容
# Python的文件对象提供了write()方法，可以向文件中写入内容。
# file.write(string)
# file为打开的文件对象；
# string为要写入的字符串。
file = open('test.txt', 'w')
file.write('hello world!')
file.close()
# 在写入文件后，一定要调用close()方法关闭文件，否则写入的内容不会保存到文件中。
# 这是因为当我们在写入文件内容时，操作系统不会立刻把数据写入磁盘，而是先缓存起来。
# 在向文件中写入内容后，如果不想马上关闭文件，也可以调用文件对象提供的flush()方法，把缓冲区的内容写入文件。
file = open('test.txt', 'a+')
file.write('\nhello ahu!')
file.flush()
file.close()
# 向文件中写入内容时，如果打开文件采用w（写入）模式，则先清空原文件的内容，再写入新的内容；
# 而如果打开文件采用a（追加）模式，则不覆盖原有文件的内容，只是在文件的结尾处增加新的内容。

# 读取文件

# 读取指定字符
# 文件对象提供了read()方法读取指定个数的字符。
# file.read([size])
# file为打开的文件对象；
# size为可选参数，用于指定要读取的字符个数，如果省略则一次性读取所有内容。
with open('test.txt', 'r') as t:
    str1 = t.read()
    print(str1)
# 在调用read()方法读取文件内容的前提是，打开文件时，指定的打开模式为r（只读）或者r＋（读写），否则，将抛出异常。

# 使用read(size)方法读取文件时，是从文件的开头读取的。
# 如果想要读取部分内容，可以先使用文件对象的seek()方法将文件的指针移动到新的位置，然后再应用read(size)方法读取。
# file.seek(offset[,whence])
# file：表示已经打开的文件对象。
# offset：用于指定移动的字符个数，其具体位置与whence有关。
# whence：用于指定从什么位置开始计算。值为0表示从文件头开始计算，1表示从当前位置开始计算，2表示从文件尾开始计算，默认为0。
with open('test.txt', 'r') as t:
    t.seek(13)
    str2 = t.read()
    print(str2)
    print()
# 在使用seek()方法时，offset的值是按一个汉字占两个字符、英文和数字占一个字符计算的。

# 读取一行
# 在使用read()方法读取文件时，如果文件很大，一次读取全部内容到内存，容易造成内存不足，所以通常会采用逐行读取。
# 文件对象提供了readline()方法用于每次读取一行数据。
# file.readline()
# file为打开的文件对象。
# 同read()方法一样，打开文件时，也需要指定打开模式为r（只读）或者r＋（读写）。
with open('test.txt', 'r') as t:
    str3 = t.readline()
    str4 = t.readline()
    print(str3, end='')
    print(str4)
    print()
# 读取全部行
# 读取全部行的作用与调用read()方法时不指定size类似，只不过读取全部行时，返回的是一个字符串列表，每个元素为文件的一行内容。
# 使用的是文件对象的readlines()方法
# file.readlines()
# file为打开的文件对象。同read()方法一样，打开文件时，也需要指定打开模式为r（只读）或者r＋（读写）。
with open('test.txt', 'r') as t:
    str5 = t.readlines()
    print(str5)
    print()
# 从该运行结果中可以看出，readlines()方法的返回值为一个字符串列表。在这个字符串列表中，每个元素记录一行内容。
with open('test.txt', 'r') as t:
    str6 = t.readlines()
    for item in str6:
        print(item, end='')
    print()

# 删除文件
# Python没有内置删除文件的函数，但是在内置的os模块中提供了删除文件的函数remove()
# os.remove(path)
# path为要删除的文件路径，可以使用相对路径，也可以使用绝对路径。
# 一般在删除文件时先判断文件是否存在，只有存在时才执行删除操作。

# 重命名文件和目录
# os模块提供了重命名文件和目录的函数rename()，如果指定的路径是文件，则重命名文件，如果指定的路径是目录，则重命名目录。
# os.rename(src,dst)
# src用于指定要进行重命名的目录或文件；
# dst用于指定重命名后的目录或文件。
# 在进行文件或目录重命名时，也建议先判断文件或目录是否存在，只有存在时才进行重命名操作。
# 在使用rename()函数重命名目录时，只能修改最后一级的目录名称。

# 获取文件基本信息
# 在计算机上创建文件后，该文件本身就会包含一些信息。
# 通过os模块的stat()函数可以获取到文件的这些基本信息。
# os.stat(path)
# path为要获取文件基本信息的文件路径，可以是相对路径，也可以是绝对路径。
print()
info = os.stat('test.txt')
print(os.path.abspath('test.txt'))
print(info.st_ino)
print(info.st_dev)
print(info.st_size)
print(info.st_atime_ns)
print(info.st_mtime)
print(info.st_ctime)


# 由于上面的结果中的时间和字节数都是一长串的整数，与我们平时见到的有所不同，所以一般情况下，为了让显示更加直观，还需要对这样的数值进行格式化。

def formattime(longtime):
    """
    :param longtime:要格式化的时间
    :return:None
    """
    import time  # 导入时间模块
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(longtime))


def formatbyte(number):
    """
    :param number:要格式化的字节数
    :return:
    """
    for (scale, label) in [(1024 * 1024 * 1024, "GB"), (1024 * 1024, "MB"), (1024, "KB")]:
        if number >= scale:  # 如果文件大小大于等于1KB
            return "%.2f %s" % (number * 1.0 / scale, label)
        elif number == 1:  # 如果文件大小为1字节
            return "1 byte"
        else:  # 处理小于1KB的情况
            byte = "%.2f" % (number or 0)
    return (byte[:-3] if byte.endswith('.00') else byte) + " byte"  # 去掉结尾的.00，并且加上单位“字节”


if __name__ == '__main__':
    print()
    info = os.stat('test.txt')
    print(os.path.abspath('test.txt'))
    print(info.st_ino)
    print(info.st_dev)
    print(formatbyte(info.st_size))
    print(formattime(info.st_atime))
    print(formattime(info.st_mtime))
    print(formattime(info.st_ctime))
