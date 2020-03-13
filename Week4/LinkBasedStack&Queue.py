# ======== 4 链表实现栈和队列 ========
# 用链表实现ADT Stack与ADT Queue的所有接口
class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev


class LinkStack():
    def __init__(self, name = None):
        self.head = name

    def isEmpty(self):
        return self.head == None

    def push(self, item):
        node = Node()
        node.setData(item)
        node.setNext(self.head)
        self.head = node

    def pop(self):
        if self.head == None:
            return 'You cannot pop an empty Stack'
        else:
            item = self.head.data
            self.head = self.head.getNext()
            return item

    def peek(self):
        return self.head.getData()

    def size(self):
        now = self.head
        size = 0
        while now != None:
            size += 1
            now = now.getNext()
        return size


class LinkQueue():
    def __init__(self, name = None):
        self.head = name

    def isEmpty(self):
        return self.head == None

    def enqueue(self, item):
        node = Node()
        node.setData(item)
        node.setNext(self.head)
        self.head = node

    def dequeue(self):
        now = self.head
        if now == None:
            return 'You cannot dequeue an empty Queue'
        elif now.getNext() == None:
            self.head = None
            return now.getData()
        else:
            while now.getNext().getNext() != None:
                now = now.getNext()
            res = now.getNext().getData()
            now.setNext(None)
            return res

    def size(self):
        now = self.head
        size = 0
        while now != None:
            size += 1
            now = now.getNext()
        return size




# 检验
print("======== 4-Link Stack & Link Queue ========")
s = LinkStack()
q = LinkQueue()
for i in range(10):
    s.push(i)
    q.enqueue(i)
print(s.peek(), q.dequeue())  # 9 0
print(s.pop(), q.size())  # 9 9
while not s.isEmpty():
    s.pop()
print(s.size(), q.isEmpty())  # 0 False

a = LinkQueue()
a.enqueue(0)
print(a.isEmpty())
a.enqueue(12)
print(a.isEmpty())
print(a.dequeue())
print(a.isEmpty())
a.enqueue(13)
print(a.isEmpty())
print(a.dequeue())
print(a.size())