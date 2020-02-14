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
# ar7 = np.linspace(1,5,6).reshape(2,3) #创建一个有序的array，第三个参数为分段数目加1，reshape中的参数同理
# print(ar7)
# print(np.random.random((3,3))) #创建一个给定shape的array，元素为0至1之间的随机值


# numpy：array的基础运算
# ar8 = np.array([1, 2, 3, 4])
# ar9 = np.arange(4)
# print(ar8 - ar9, ar8 + ar9, ar8 * ar9, ar9 / ar8)  # 相同shape的array可以相加减乘除，得到每个元素分别相加减乘除后的array
# print(ar8 == 4, ar8 < 4, type(ar8 < 4), type((ar8 < 4)[0]))  # 判断array中各元素的大小，输出一个各元素为布尔型的array
#ar10 = np.arange(6).reshape((2, 3))
#ar11 = np.arange(6).reshape((3, 2))
# print(np.dot(ar10,ar11)) #np.dot(a,b)可以对两个可乘的二维array（矩阵）a与b进行矩阵乘法，输出得到的矩阵
# print(ar10.dot(ar11)) #a.dot(b)是完全相同的操作
# print(np.transpose(ar10), ar10.T) #输出转置后的array
# print(ar10, np.sum(ar10), np.max(ar10),np.min(ar10)) #输出某一array中元素的和、最大值、最小值、平均值
# print(np.mean(ar10), ar10.mean(axis = 1), np.median(ar10)) #输出某一array中元素的平均值、中位数
# print(np.sum(ar10, axis = 0), np.sum(ar10, axis = 1), np.max(ar10, axis = 0)) #axis参数代表行列，1对应行，0对应列，输出array
# print(np.argmin(ar10),np.argmax(ar10, axis = 1)) #arg表示索引，输出极值的索引
