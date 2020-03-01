from timeit import Timer
import random

# 验证字典按关键码取值和赋值是O(1)的
getlst = []
setlst = []
for i in range(10000, 100001, 10000):
    dict = {j: None for j in range(i)}
    t1 = Timer("dict[random.randrange(i)]", 'from __main__ import dict,random,i')
    t2 = Timer("dict[random.randrange(i)]=1", "from __main__ import dict,random,i")
    getres, setres = t1.timeit(number=1000) * 1000, t2.timeit(number=1000) * 1000
    print('%.7f' % getres, '%.7f' % setres)
    getlst.append(getres)
    setlst.append(setres)

import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(1, 11)]
plt.xlabel("dictionary scale/10000")
plt.ylabel("time consumed / ms")
plt.ylim((0, 3))
plt.plot(x, getlst, label='get_item')
plt.plot(x, setlst, label='set_item')
plt.yticks(np.linspace(0, 3, 9))
plt.xticks(np.linspace(1, 10, 10))
plt.legend()
plt.show()
