# 陈斌老师的Python基础与应用课程的学习笔记

# 输入某年某月某日，输出这一天是这一年的第几天
'''
import datetime

dtstr = input("Please input the daytime(yyyymmdd):")
dt = datetime.datetime.strptime(dtstr, "%Y%m%d") # .strptime是python的内置函数，可以按照第二个参数给出的格式将一段字符串提取成时间元组的模式
# print(dt,type(dt))
dtstr2 = dtstr[:4]+'0101' # 创建一个该年第一天对应的字符串
dt2 = datetime.datetime.strptime(dtstr2,'%Y%m%d')
print(int((dt-dt2).days)+1)
'''

# 数据类型：数值
'''
# 1.整数int：python本身试别加了前缀的二进制、八进制、十六进制数，前缀分别为0b、0o、0x。例如：
print(0b100 == 4) # 输出结果为True，这说明了进制只是人用来表示数的方式。
# 2.浮点数float：与整数不同的是，浮点数收到17位有效数字的限制，不像int类型可以是无限大的整数。
print(0.123123123123123123123123) #输入的浮点数有18位有效数字，输出后自动转化为17位有效数字。
print(1.1 + 1.1 == 2.2, 1.1 + 2.2 == 3.3) #用十进制的方法输入数，计算机运算时转化为二进制，可能会出现无限循环小数，加上17位的限制，计算结果会有误差
# 所以对浮点数进行比较的时候最好不要用相等判断，而是判断二者的差是否小于一个很小的值。
# 3.复数complex：支持常见的复数运算，可以提取出复数的实部和虚部。面向复数计算的模块‘cmath’（‘math’的计算面向整数和浮点数）
print(type(1+1j), (2+3j)**2, (2+3j).imag, (2+3j).real)
'''

# 数据类型：逻辑值Boolean
# 逻辑运算：与and、或or、非not（特殊的运算，对单一逻辑值）。优先级：not > and > or
# 各种数据类型对应的逻辑值：对于数值类型，0为False，非0为True；对于序列类型（如字符串、容器类型等），空为False，非空为True。

# 数据类型：字符串String
'''
# 转义符“\”：转义符后面的符号不起原本的作用，只是作为字符出现，例如：
print('Let\'s go!', '\n This is the second line.\n This is the third line.')  # 字符串中的'在转义符后，不会干扰字符串外部引号的判断；\n表示换行
# 字符串的一些操作：获取长度；切片；加法与乘法；判断相等；判断某个字符是否处于字符串中；删除空格；判断字符串的每个符号是否是字母或数字；
print('Hello World!'.split(' '), ' '.join(['Hello', 'World!']))  # 分割split与合并join
print('abs'.upper(), 'ABS'.lower(), 'Hello World!'.swapcase())  # 有关字母大小写的变化
print('Hello World!'.replace('l','L')) # 替换字符串的子串
# 上面的许多操作都反映了字符串序列的特征
'''

