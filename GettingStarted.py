import numpy as np
import pandas as pd

#numpy：array的属性，更多见 https://numpy.org/devdocs/reference/routines.array-manipulation.html
'''
ar1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(ar1, type(ar1))
print("The number of dimension:", ar1.ndim)
print("The shape of the array:", ar1.shape)
print("The number of elements in the array:", ar1.size)
'''

#numpy：创建array时的性质，更多见 https://numpy.org/doc/1.18/reference/routines.array-creation.html
'''
ar2 = np.array([[1,0,0],[0,1,0],[0,0,1]], dtype=np.int64) #其他的类型有int32，float32、64等
print(ar2.dtype)
ar3 = np.zeros((3,3)) #创建一个零矩阵，中间的参数为array的shape
ar4 = np.ones((3,3)) #创建一个元素全为1的array，参数同理
ar5 = np.empty((3,3)) #创建一个元素随机的array，参数同理
print(ar3,ar4,ar5)
ar6 = np.arange(12).reshape((3,4)) #创建一个有序的array，该array的size应与arange中的参数相同
print(ar6)
ar7 = np.linspace(1,5,6).reshape(2,3) #创建一个有序的array，第三个参数为分段数目加1，reshape中的参数同理
print(ar7)
'''

#numpy：