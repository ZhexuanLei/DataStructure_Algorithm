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

# 数据类型：数据容器列表与元组
'''
lst1 = [2, 1, 2, 3]
print(list(reversed(lst1)), lst1)  # reversed与.reverse()不同，会生成一个新的列表，而原列表不变，reverse则会把作用的列表倒序
print(lst1.count(2))  # 根据元素的值进行计数
lst1.remove(2)
print(lst1)  # remove会移除列表种第一次出现的该元素
lst2 = [0, 0, 0]
print(lst1+lst2, lst1, lst2) # 加法合并列表，会生成一个新的列表，参与合并的两个列表不变
lst1.extend(lst2)
print(lst1, lst2) # extend合并列表会改变被加长的列表，另一个加上去的列表不变
print(lst2 * 3) # 乘法合并列表
lst2.clear() # 清空列表
print(lst2) 
# 元组的许多操作与列表类似，唯一的区别是元组是不可变容器类型，一些重组、合并、赋值对于元组来说是不可行的
'''

# 数据类型：字典
'''
dic1 = dict.fromkeys([1,2,1],10) # 批量向字典种添加数据项，注意字典中不会有重复的key，同时key应该是不可变类型
dic1[3] = 10 # 通过创建新的键值对并赋值的方法更新字典
print(dic1)
dic2 = {4:10, 5:11}
dic1.update(dic2) # 合并两个字典并更新（如果键有重复，则其值会更新）
print(dic1)
print(dic1.pop(5)) # 弹出指定key的数据项，返回数据值
print(dic1)
print(dic1.popitem()) # 弹出并返回任意一个数据项（似乎会返回字典中的最后一个键值对，但实际上不存在顺序关系）
print(3 in dic1, 10 in dic1) # 单纯的in字典是对key进行判断，如果要对数据值进行判断则需要使用in字典.values()
print(10 in dic1.values())
'''

# 数据类型：集合（不可变key的无需组合）
'''
set1 = set('123') # 创建集合
set2 = set('234')
print(set1|set2, set1&set2, set1-set2) # 集合的运算：并交差
print(set1.isdisjoint(set2), set1&set2 == set()) # 判断交集是否为空。返回False表明交集不为空
# 生成集合可以快速去重；判断一个元素是否处于一个集合中的性能很高，比列表的判断更快
'''

# 扩展模块
'''
import time, datetime # 时间、日期模块
today = datetime.date.today()
print(today,datetime.datetime.now(),datetime.datetime.now().isoformat())
print(today.timetuple()) # 结构化的时间
print(time.mktime(today.timetuple())) # 从1970年1月1日0时开始计算的时间戳
yesterday = today - datetime.timedelta(days=1)
onehourago = datetime.datetime.now() - datetime.timedelta(hours=1)
print(yesterday, onehourago)
'''
'''
import calendar
calendar.prmonth(2020,3)
calendar.prcal(2020) # 两个用来显示日历的函数
print(calendar.monthcalendar(2020,3)) # 输出嵌套的列表
print(calendar.isleap(2020)) # 判断闰年
print(calendar.monthrange(2020,3)) # 返回一个二元组，分别表示该月起始的星期数，第二个表示天数
'''
'''
import time

print(time.time())  # 获取当前的时间戳
print(time.asctime(), time.ctime(), time.asctime((2020,3,11,14,29,30,0,0,0))) # 获取当前的时间，把元组转化成时间的类型
t1 = time.time()
time.sleep(1) # 让程序暂停运行一段时间
t2 = time.time()
print(t2-t1)
'''
'''
# math, cmath, decimal模块
from decimal import Decimal
print(0.1+0.1+0.1-0.3, Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')) # Decimal生成精确精度的小数
'''
'''
# random模块
import random

print(random.random())  # 生成0-1间的随机浮点数
print(random.uniform(1, 10))  # 生成指定范围之间的随机浮点数
print(random.randint(1, 10))  # 生成指定范围内的随机整数
print(random.randrange(2, 11, 2))  # 生成指定集合内的随机数
print(random.getrandbits(10))  # 生成指定位数的随机二进制数（输出为十进制）
lst = ['a', 'b', 'c', 'd', 'e']
print(random.choice(lst)) # 从指定序列中随机选出一个元素
print(random.sample(lst,2)) # 从指定序列中随机选取指定个数的元素
random.shuffle(lst) # 将指定序列随机排序
print(lst)
'''
'''
# 数据持久化模块
import pickle, shelve  # pickle将python对象格式化便于储存, shelve进行储存
# shelve通过key的方式建立一个数据库，使得程序可以对保存的python对象进行标准化的访问和操作
d = shelve.open('testfile') # 创建一个shelve对象，可以将其他的对象存储在该shelve对象中
d['num'] = 0 # 写入对象，键值对的操作与字典类似，赋值、读取、删除等
d.close() # 关闭shelve文件
'''
