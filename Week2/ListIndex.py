# 验证列表按索引取值的大O复杂度是O(1)
from timeit import Timer
import random

tlst = []
for i in range(10000, 100001, 10000):
    lst = [j for j in range(i)]
    t1 = Timer('lst[random.randrange(i)]', 'from __main__ import lst,random,i')
    res = t1.timeit(number=1000)*1000
    print(res)
    tlst.append(res)

import matplotlib.pyplot as plt
import numpy as np
x = [i for i in range(1, 11)]
y = tlst
plt.xlabel("list length/10000")
plt.ylabel("time consumed / ms")
plt.ylim((0,3))
plt.plot(x,y)
plt.yticks(np.linspace(0,3,9))
plt.xticks(np.linspace(1,10,10))
plt.show()



