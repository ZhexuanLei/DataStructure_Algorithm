from timeit import Timer
import random
import math

timelst = []
for i in range(100000, 1000001, 100000):
    lst = [random.randrange(i * 10) for j in range(i)]
    t = Timer('lst.sort()', 'from __main__ import lst')
    res = t.timeit(number=1000) / math.log(i, 10)
    timelst.append(res)
    print(res)

import matplotlib.pyplot as plt
import numpy as np

x = range(1, 11)
plt.xlabel("list scale/10^5")
plt.ylabel("revised time / s")
plt.scatter(x, timelst)
reg = np.polyfit(x, timelst, 1)
pred = np.polyval(reg, x)
plt.plot(x,pred,label='Linear Regression')
plt.legend(loc='upper left')
plt.show()
