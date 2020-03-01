from timeit import Timer
import random

# 研究列表和字典del操作符的性能
llst, dlst = [], []
for i in range(1000000, 10000001, 1000000):
    lst = [j for j in range(i)]
    dic = {j: None for j in range(i)}
    tl = Timer('del lst[i//2]', 'from __main__ import lst,i,random')
    td = Timer('del dic[random.randrange(i)]', 'from __main__ import dic,i,random')
    lstres, dicres = tl.timeit(number=1000), td.timeit(number=100) * 1000
    llst.append(lstres)
    dlst.append(dicres)
    print(lstres, dicres)

import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(1, 11)]
plt.xlabel("list scale/10^7")
plt.ylabel("time consumed / s or ms")
plt.scatter(x, llst, label='del list')
plt.scatter(x, dlst, label='del dictionary')
reg = np.polyfit(x, llst, 1)
pred = np.polyval(reg, x)
plt.plot(x,pred,label='linear regression')
plt.yticks(np.linspace(0, 5, 11))
plt.xticks(np.linspace(1, 10, 10))
plt.legend(loc='upper left')
plt.show()
