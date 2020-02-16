import numpy as np
import pandas as pd

# 更多的语法见：https://numpy.org/doc/1.18/reference
# numpy：array的属性
# ar1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
# print(ar1, type(ar1))
# print("The number of dimension:", ar1.ndim)
# print("The shape of the array:", ar1.shape)
# print("The number of elements in the array:", ar1.size)


# numpy：创建array时的性质
# ar2 = np.array([[1,0,0],[0,1,0],[0,0,1]], dtype=np.int64) #其他的类型有int32，float32、64等
# print(ar2.dtype)
# ar3 = np.zeros((3,3)) #创建一个零矩阵，中间的参数为array的shape
# ar4 = np.ones((3,3)) #创建一个元素全为1的array，参数同理
# ar5 = np.empty((3,3)) #创建一个元素随机的array，参数同理
# print(ar3,ar4,ar5)
# ar6 = np.arange(12).reshape((3,4)) #创建一个有序的array，该array的size应与arange中的参数相同
# print(ar6)
# print(ar6.flatten()) #将二维的array转化为一维
# ar7 = np.linspace(1,5,6).reshape(2,3) #创建一个有序的array，第三个参数为分段数目加1，reshape中的参数同理
# print(ar7)
# print(np.random.random((3,3))) #创建一个给定shape的array，元素为0至1之间的随机值


# numpy：array的基础运算
# ar8 = np.array([1, 2, 3, 4])
# ar9 = np.arange(4)
# print(ar8 - ar9, ar8 + ar9, ar8 * ar9, ar9 / ar8)  # 相同shape的array可以相加减乘除，得到每个元素分别相加减乘除后的array
# print(ar8 == 4, ar8 < 4, type(ar8 < 4), type((ar8 < 4)[0]))  # 判断array中各元素的大小，输出一个各元素为布尔型的array
# ar10 = np.arange(6).reshape((2, 3))
# ar11 = np.arange(6).reshape((3, 2))
# print(np.dot(ar10,ar11)) #np.dot(a,b)可以对两个可乘的二维array（矩阵）a与b进行矩阵乘法，输出得到的矩阵
# print(ar10.dot(ar11)) #a.dot(b)是完全相同的操作
# print(np.transpose(ar10), ar10.T) #输出转置后的array
# print(ar10, np.sum(ar10), np.max(ar10),np.min(ar10)) #输出某一array中元素的和、最大值、最小值、平均值
# print(np.mean(ar10), ar10.mean(axis = 1), np.median(ar10)) #输出某一array中元素的平均值、中位数
# print(np.sum(ar10, axis = 0), np.sum(ar10, axis = 1), np.max(ar10, axis = 0)) #axis参数代表行列，1对应行，0对应列，输出array
# print(np.argmin(ar10),np.argmax(ar10, axis = 1)) #arg表示索引，输出极值的索引

# numpy：array的索引
# ar12 = np.arange(12).reshape(3, 4)
# print(ar12, ar12[2], ar12[2,0], ar12[2][0], ar12[2][0:1]) # array索引的方式
# print(type(ar12[2,0]), type(ar12[2]), type(ar12[2][0:1]))
# for i in ar12:
# print(i) # 对array进行迭代时默认迭代行，这是显然的
# for i in ar12.T:
# print(i) # 对列进行迭代的方法，是对原array进行转置再迭代，机智
# for i in ar12.flatten():
# print(i) # 对array中所有元素进行迭代，可以把array转化为一维

# numpy：array的合并与分割
# ar13 = np.array([1, 1, 1]).reshape(3, 1)
# ar14 = np.array([2, 2, 2]).reshape(3, 1)
# print(np.vstack((ar13, ar14)), np.hstack((ar13, ar14))) # array的合并可以在水平方向与竖直方向进行
# print(np.concatenate((ar13, ar14), axis = 1)) # 使用concatenate可以设定axis参数表明合并的方向
# ar15 = np.arange(12).reshape(3,4)
# print(np.vsplit(ar15,3), np.hsplit(ar15, 2)) # np.split的第二个参数表示分割得到的份数，无法进行不对称的分割
# print(np.split(ar15, 2, axis = 1)) # 可以用axis定义分割的方向
# print(np.array_split(ar15, (1,1,2), axis = 1))
# np.array_split可以进行不对称的分割，分割模式可以由一个tuple型的参数在第二位规定
# numpy中array的复制与深复制与python中其他的变量相同
# a = np.arange(5)
# b = a # 如此定义b并未创建新的变量，在内存中与a指向同一位置，b只是a的别名
# c = a.copy() # 如此定义c为深复制，创建了一个新的变量
# print(a, b, c)
# a[0] = 1 # 在改变a的同时，b被改变，但新变量c不变
# print(a, b, c)

# pandas：序列Series与结构Dataframe
# se1 = pd.Series([1, 2, 3])
# print(se1, type(se1))  # 根据列表创建序列
# df1 = pd.DataFrame(np.random.randn(4, 5), index = ['w','x','y','z'], columns=['a', 'b', 'c', 'd', 'e'])
# 创建dataframe，可以定义行与列的名称，缺省的名称是自然数
# print(df1)
# df2 = pd.DataFrame({'a': [1, 2], 'b': 2, 'c': 3, 'x': 100, 'y': 11})
# 根据字典创建dataframe，字典的key为column名称。如果各列行数不同，则会在自动补齐
# print(df2, df2.dtypes, df2.index, df2.columns, df2.values) # dataframe的各种属性
# print(df2)
# print(df2.describe()) # 对于dataframe中的数进行简单的统计描述，其他type的数据会在统计中被舍弃
# print(df2.T) # 输出dataframe的转置
# print(df2.sort_index(axis=0, ascending=False)) # 对dataframe按照index进行排序，两个参数分别规定行以及升降
# print(df2.sort_values(by='a', ascending=False)) # 对dataframe按照数据的值进行排序，同样两个参数

# pandas：数据抽取
# dates = pd.date_range('20200216', periods=4) # 生成日期类型的index
# print(dates, type(dates))
# df3 = pd.DataFrame((np.arange(12).reshape(4,3)), index=dates, columns=['a', 'b','c'])
# print(df3)
# print(df3[0:2], df3.loc['a']) #[]内输入index或者column可以选择出对应的数据，df[:]是对于行进行选取
# print(type(df3['a'],type(df3[0:2]))) # 输出的类型为序列或结构，取决于维度
# print(df3['b']['20200218'], df3.loc['20200218','b']) # 使用.loc根据label对数据进行选择
# print(df3.loc['20200218',['a','b']]) # 使用.loc也可以选取多行多列
# print(df3, df3.loc['20200218','b'], df3.iloc[2,1]) # 使用.iloc可以根据数据的位置进行选择
# print(df3[df3['a']>0], df3[df3.a>0][df3.b>4]) # 布尔型抽取，似乎只能按照列中的数据来筛选

# pandas：dataframe中的赋值与插入
# df4 = pd.DataFrame((np.arange(12).reshape(3, 4)), index=['a', 'b', 'c'], columns=['w', 'x', 'y', 'z'])
# print(df4)
# df4.loc['a','w']=100 # 简单的赋值方式
# print(df4)
# df4[df4.x>4] = 9 # 取出一部分进行赋值
# print(df4)
# df4.x[df4.x>4] = 9
# print(df4)
# df4['s'] = [1, 2, 3] # 附加新的一列
# print(df4)
