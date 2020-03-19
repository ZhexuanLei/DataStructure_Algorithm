# ======= 2 基数排序 =======
# 实现一个基数排序算法，用于10进制的正整数从小到大的排序。
#
# 思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
# 第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
# 第三趟放百位，再合并；第四趟放千位，再合并。
# 直到最多的位数放完，合并完，这样main队列里就是排好序的数列了。
#
# 创建一个函数，接受参数为一个列表，为需要排序的一系列正整数，
# # 返回排序后的数字列表。
# 输入样例1：
# [1, 2, 4, 3, 5]
# 输出样例1：
# [1, 2, 3, 4, 5]
# 输入样例2：
# [8, 91, 34, 22, 65, 30, 4, 55, 18]
# 输出样例2：
# [4, 8, 18, 22, 30, 34, 55, 65, 91]


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def radix_sort(s) -> list:
    s.sort()  # 得到输入的数据中位数最大的数的位数
    m = len(str(s[-1]))

    qlst = [Queue() for i in range(11)]
    for i in s:
        qlst[10].enqueue(i)  # 初始化main队列
    for j in range(1, m + 1):  # 排序的主体循环
        while not qlst[10].isEmpty():
            top = qlst[10].dequeue()
            if len(str(top)) < j:
                qlst[0].enqueue(top)
            else:
                qlst[int(str(top)[-j])].enqueue(top)
        for i in range(10):
            while not qlst[i].isEmpty():
                qlst[10].enqueue(qlst[i].dequeue())

    sorted = []  # 将最后的main队列转化为列表输出
    while not qlst[10].isEmpty():
        sorted.append(qlst[10].dequeue())
    return sorted


# 调用检验
print("======== 2-radix_sort ========")
print(radix_sort([1, 2, 4, 3, 5]))
print(radix_sort([8, 91, 34, 22, 65, 30, 4, 55, 18]))
