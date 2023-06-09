# 正则表达式（Regular Expression，简写为regex），又称规则表达式，是计算机科学的一个概念，通常被用来检索和替换符合某些规则的文本。
# 在Python中，可以使用正则表达式进行与字符串相关的一些匹配。
# 正则表达式就是记录文本规则的代码。

# 行定位符
# 行定位符就是用来描述字符串的边界。
# “^”表示行的开始；“$”表示行的结尾。
# ^tm
# 表示要匹配字符串tm的开始位置是行头，如tm equal Tomorrow Moon就可以匹配，而Tomorrow Moon equal tm则不匹配。
# tm$
# 后者可以匹配，而前者不能匹配。如果要匹配的字符串可以出现在字符串的任意部分，那么可以直接写成：
# tm
# 这样，两个字符串就都可以匹配了。

# 元字符
# 代码	说明
# .	    匹配除换行符以外的任意字符
# \w	匹配字母或数字或下划线或汉字
# \s	匹配任意的空白符
# \d	匹配数字
# \b	匹配单词的开始或结束
# ^	    匹配字符串的开始
# $	    匹配字符串的结束

# \bmr\w*\b
# 该表达式可以匹配“mrsoft” 、“mrbook” 和“mr123456”等

# 重复
# 上面用“\w*”匹配任意数量的字母或数字。如果想匹配特定数量的数字，该如何表示呢？
# 正则表达式为我们提供了限定符（指定数量的字符）来实现该功能。
# 匹配8位QQ号可用如下表达式：
# ^\d{8}$

# 限定符	说明	                        举例
# ?	        匹配前面的字符零次或一次	        colou?r，该表达式可以匹配color和colour
# +	        匹配前面的字符一次或多次	        go+gle，该表达式可以匹配的范围从gogle到goo…gle
# *	        匹配前面的字符零次或多次	        go*gle，该表达式可以匹配的范围从ggle到goo…gle
# {n}	    匹配前面的字符n次	            go{2}gle，该表达式只匹配google
# {n,}	    匹配前面的字符最少n次	            go{2,}gle，该表达式可以匹配的范围从google到goo…gle
# {n,m}	    匹配前面的字符最少n次，最多m次	employe{0,2}，该表达式可以匹配employ、employe和employee3种情况。

# 字符类
# 如果要匹配没有预定义元字符的字符集合（比如元音字母a, e, i, o, u），应该怎么办？
# 只需要在方括号里列出它们就行了，像[aeiou]就匹配任何一个英文元音字母，[.?!]匹配标点符号“.”、“?”或“!”。
# 要想匹配给定字符串中任意一个汉字，可以使用[\u4e00-\u9fa5]； 如果要匹配连续多个汉字， 可以使用[\u4e00-\u9fa5]+。

# 排除字符(^)
# “^”字符放到方括号中，表示排除的意思。
# [^a-zA-Z]
# 该表达式用于匹配一个不是字母的字符。

# 选择字符(|)
# 如何匹配身份证号码呢？
# 身份证号码长度为15位或者18位。如果为15位，则全为数字；如果为18位，前17位为数字，最后一位是校验位，可能为数字或字符X。
# 使用选择字符（|）来实现。该字符可以理解为“或”，匹配身份证的表达式可以写成如下方式：
# (^\d{15}$)|(^\d{18}$)|(^\d{17})(\d|X|x)$
# 该表达式的意思是可以匹配15位数字，或者18位数字，或者17位数字和最后一位。最后一位可以是数字或者是X或者是x。

# 转义字符(\)
# 正则表达式中的转义字符（\）和Python中的大同小异，都是将特殊字符（如“.”“?”“\”等）变为普通的字符。

# 分组
# 小括号字符的第一个作用就是可以改变限定符的作用范围，如“|”“*”“^”等。
# (thir|four)th
# 这个表达式的意思是匹配单词thirth或fourth，如果不使用小括号，那么就变成了匹配单词thir和fourth了。
# 小括号的第二个作用是分组，也就是子表达式。
# 例如(\.[0-9]{1,3}){3}，就是对分组(\.[0-9]{1,3})进行重复操作。

# 在Python中使用正则表达式时，是将其作为模式字符串使用的。
# 例如，将匹配不是字母的一个字符的正则表达式表示为模式字符串，可以使用下面的代码：
# '[^a-zA-Z]'
# 而如果将匹配以字母m开头的单词的正则表达式转换为模式字符串，则不能直接在其两侧添加引号定界符，例如，下面的代码是不正确的。
# '\bm\w*\b'
# 而是需要将其中的“\”进行转义，转换后的代码为：
# '\\bm\\w*\\b'
# 由于模式字符串中可能包括大量的特殊字符和反斜杠，所以需要写为原生字符串，即在模式字符串前加r或R。
# 例如，上面的模式字符串采用原生字符串表示就是：
# r'\bm\w*\b'
# 在编写模式字符串时，并不是所有的反斜杠都需要进行转换。
# 为了编写方便，建议正则表达式都采用原生字符串表示。

# 使用re模块实现正则表达式操作
# Python提供了re模块，用于实现正则表达式的操作。
import re

# 匹配字符串
# 匹配字符串可以使用re 模块提供的match() 、search() 和findall()等方法。

# 使用match()方法进行匹配
# match()方法用于从字符串的开始处进行匹配，如果在起始位置匹配成功，则返回Match对象，否则返回None。
# re.match(pattern, string, [flags])
# pattern：表示模式字符串，由要匹配的正则表达式转换而来。
# string：表示要匹配的字符串。
# flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。常用的标志如下所示。
# 标志                  说明
# A或ASCII              对于\w、lW、b、\B、ld、\D、ls 和\S只进行ASCII匹配（仅适用于Python 3.x）
# I或IGNORECASE         执行不区分字母大小写的匹配
# M或MULTILINE          将^和S用于包括整个字符串的开始和结尾的每一行(默认情况下，仅适用于整个字符串的开始和结尾处)
# S或DOTALL             使用“.”字符匹配所有字符，包括换行符
# X或VERBOSE            忽略模式字符串中未转义的空格和注释

pattern = r'lj_\w+'  # 模式字符串
str1 = 'LJ_SHOP lj_shop'  # 要匹配的字符串
match1 = re.match(pattern, str1, re.I)  # 匹配字符串，不区分大小写
print(match1)  # 输出匹配结果
str2 = 'hahaha LJ_SHOP lj_shop'
match2 = re.match(pattern, str2, re.I)  # 匹配字符串，不区分大小写
print(match2)  # 输出匹配结果

# 从上面的执行结果中可以看出，字符串“MR_SHOP”是以“mr_”开头，所以返回一个Match对象，而字符串“项目名称MR_SHOP”不是以“mr_”开头，所以返回None。
# 这是因为match()方法从字符串的开始位置开始匹配，当第一个字母不符合条件时，则不再进行匹配，直接返回None。

# Match对象中包含了匹配值的位置和匹配数据。
# 其中，要获取匹配值的起始位置可以使用Match对象的start()方法；
print('匹配值的起始位置：', match1.start())
# 要获取匹配值的结束位置可以使用end()方法；
print('匹配值的结束位置：', match1.end())
# 通过span()方法可以返回匹配位置的元组；
print('匹配位置的元组: ', match1.span())
# 通过string属性可以获取要匹配的字符串。
print('要匹配的字符串: ', match1.string)
print('匹配数据: ', match1.group())

# 使用search()方法进行匹配
# earch()方法用于在整个字符串中搜索第一个匹配的值，如果在起始位置匹配成功，则返回Match对象，否则返回None。
# re.search(pattern, string, [flags])
# pattern：表示模式字符串，由要匹配的正则表达式转换而来。
# string：表示要匹配的字符串。
# flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。
pattern = r'lj_\w+'  # 模式字符串
str1 = 'LJ_SHOP lj_shop'  # 要匹配的字符串
match1 = re.search(pattern, str1, re.I)  # 匹配字符串，不区分大小写
print(match1)  # 输出匹配结果
str2 = 'hahaha LJ_SHOP lj_shop'
match2 = re.search(pattern, str2, re.I)  # 匹配字符串，不区分大小写
print(match2)  # 输出匹配结果

# 从上面的运行结果中可以看出，search()方法不仅仅是在字符串的起始位置搜索，其他位置有符合的匹配也可以。

# 使用findall()方法进行匹配
# findall()方法用于在整个字符串中搜索所有符合正则表达式的字符串，并以列表的形式返回。如果匹配成功，则返回包含匹配结构的列表，否则返回空列表。
# re.findall(pattern, string, [flags])
# pattern：表示模式字符串，由要匹配的正则表达式转换而来。
# string：表示要匹配的字符串。
# flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。
pattern = r'lj_\w+'  # 模式字符串
str1 = 'LJ_SHOP lj_shop'  # 要匹配的字符串
match1 = re.findall(pattern, str1, re.I)  # 匹配字符串，不区分大小写
print(match1)  # 输出匹配结果
str2 = 'hahaha LJ_SHOP lj_shop'
match2 = re.findall(pattern, str2, re.I)  # 匹配字符串，不区分大小写
print(match2)  # 输出匹配结果

# 替换字符串
# sub()方法用于实现字符串替换。
# re.sub(pattern, repl, string, count, flags)
# pattern：表示模式字符串，由要匹配的正则表达式转换而来。
# repl：表示替换的字符串。
# string：表示要被查找替换的原始字符串。
# count：可选参数，表示模式匹配后替换的最大次数，默认值为0，表示替换所有的匹配。
# flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。
pattern = r'1[34578]\d{9}'  # 定义要替换的模式字符串
str3 = '中奖号码为：84978981 联系电话为：13611111111'
result = re.sub(pattern, '1XXXXXXXXXX', str3)  # 替换字符串
print(result)

# 使用正则表达式分割字符串
# split()方法用于实现根据正则表达式分割字符串，并以列表的形式返回。
# 其作用字符串对象的split()方法类似，所不同的就是分割字符由模式字符串指定。
# re.split(pattern, string, [maxsplit], [flags])
# pattern：表示模式字符串，由要匹配的正则表达式转换而来。
# string：表示要匹配的字符串。
# maxsplit：可选参数，表示最大的拆分次数。
# flags：可选参数，表示标志位，用于控制匹配方式，如是否区分字母大小写。
pattern = r'[?|&]'  # 定义分隔符
url = 'https://www.learnjava.com/?username="zl"&pwd="learnjava"'
result = re.split(pattern, url)  # 分割字符串
print(result)
