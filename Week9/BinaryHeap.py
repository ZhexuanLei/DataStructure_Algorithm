class BinHeap():
    def __init__(self):
        self.heapList = [0]  # 为了将二叉推的根节点从下标1开始计算
        self.size = 0

    def percUp(self, i):  # 可以改进为不发生交换了就停止比较,增强性能
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                current = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = current
            i = i // 2

    def percDown(self, i):
        while (i * 2) < self.size:
            minChild = self.minChild(i)
            if self.heapList[i] > self.heapList[minChild]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[minChild]
                self.heapList[minChild] = temp
            i = minChild

    def minChile(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        elif self.heapList[i * 2] < self.heapList[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def insert(self, k):
        self.heapList.append(k)
        self.size += 1
        self.percUp(self.size)

    def delMin(self):  # 移除二叉堆中最小的元素
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.percDown(1)
        return retVal

    def buildHeap(self, alist):
        i = len(alist) // 2 # 从最后一个父节点开始进行下沉,因为叶节点不需要下沉
        self.size = len(list)
        self.heapList = [0] + alist
        print(len(self.heapList), i)
        while i > 0:
            print(self.heapList, i)
            self.percDown(i)
            i -= 1
        print(self.heapList, i)