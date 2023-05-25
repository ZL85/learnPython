# coding:utf-8
# 一直重复，直到条件不满足时才结束的循环，称为条件循环。只要条件为真，这种循环会一直持续下去，如while循环
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
none = True  # 作为循环条件的变量
number = 0  # 计数的变量
while none:
    number += 1  # 计数加1
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:  # 判断是否符合条件
        print("答曰：这个数是", number)  # 输出符合条件的数
        none = False  # 将循环条件的变量赋值为否
'''
首先定义一个用于计数的变量number和一个作为循环条件的变量none（默认值为真），
然后编写while循环语句，在循环体中，将变量number的值加1，并且判断number的值是否符合条件，
当符合条件时，将变量none设置为假，从而退出循环。
'''
