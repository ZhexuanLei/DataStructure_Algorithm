class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, items):
        self.items.insert(0, items)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

def HotPotato(lst, num):
    simq = Queue()  # 这种算法是用模拟的方式，直接计算是比较难的
    for name in lst:
        simq.enqueue(name)
    while simq.size() > 1:
        for i in range(num):
            simq.enqueue(simq.dequeue)
        simq.dequeue()
    return simq.dequeue()

