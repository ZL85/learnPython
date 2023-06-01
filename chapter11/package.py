# 使用模块可以避免函数名和变量名重名引发的冲突。那么，如果模块名重复应该怎么办呢？在Python中，提出了包（Package）的概念。
# 包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下。这样，既可以起到规范代码的作用，又能避免模块名重名引起的冲突。
# 包简单理解就是“文件夹”，只不过在该文件夹下必须存在一个名称为“init.py”的文件。

# 创建包
# 创建包实际上就是创建一个文件夹，并且在该文件夹中创建一个名称为“__init__.py”的Python文件。
# 在__init__.py文件中，可以不编写任何代码，也可以编写一些Python代码。
# 在__init__.py文件中所编写的代码，在导入包时会自动执行。
# init.py文件是一个模块文件，模块名为对应的包名。

# 使用包
# 创建包以后，就可以在包中创建相应的模块，然后再使用import语句从包中加载模块。

# 通过“import 完整包名.模块名”形式加载指定模块
# 通过该方式导入模块后，在使用时需要使用完整的名称。
import package.info

print("your name:", package.info.name)
print("your gender:", package.info.gender)
print("your age:", package.info.age)
print()

# 通过“from 完整包名 import 模块名”形式加载指定模块
# 通过该方式导入模块后，在使用时不需要带包前缀，但是需要带模块名。
from package import info

print("your name:", info.name)
print("your gender:", info.gender)
print("your age:", info.age)
print()

# 通过“from 完整包名.模块名 import 定义名”形式加载指定模块
# 通过该方式导入模块的函数、变量或类后，在使用时直接使用函数、变量或类名即可。
from package.info import name, gender, age

print("your name:", name)
print("your gender:", gender)
print("your age:", age)
print()

# 在通过“from 完整包名.模块名 import 定义名”形式加载指定模块时，可以使用星号“*”代替定义名，表示加载该模块下的全部定义。
from package.info import *

print("your name:", name)
print("your gender:", gender)
print("your age:", age)
