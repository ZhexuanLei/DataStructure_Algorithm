# ======== 5 双链无序表 ========
# 实现双向链表版本的UnorderedList，接口同ADT UnorderedList
# 在节点Node中增加prev变量，引用前一个节点
# 在UnorderedList中增加tail变量，引用列表中最后一个节点
# 增加getTail方法

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

class DoublyLinkedList():
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.setNext(self.tail)
        self.tail.setPrev(self.head) # 此处创建的两个头尾节点是不变的，单纯用来指示无序表的首末

    def isEmpty(self):
        return self.head.getNext() == self.tail

    def size(self):
        now = self.head
        count = 0
        while now.getNext() != self.tail:
            now = now.getNext()
            count += 1
        return count

    def getTail(self):
        if self.isEmpty():
            return 'GetTail failed! The list is empty.'
        else:
            return self.tail.getPrev() # getTail是取tail节点的前一个，因为如上所述，head与tail是不含数据的用于指示首末的节点

    def append(self, item):
        node = Node(item)
        LastTail = self.tail.getPrev() # append进入的数据节点在最靠近tail节点的地方
        LastTail.setNext(node)
        node.setPrev(LastTail)
        node.setNext(self.tail)
        self.tail.setPrev(node)

    def add(self, item):
        node = Node(item)
        LastHead = self.head.getNext() # 同样可以看到，head不含数据，表的第一个数据在head节点的下一个节点中
        LastHead.setPrev(node)
        node.setNext(LastHead)
        node.setPrev(self.head)
        self.head.setNext(node)

    def search(self, item):
        now = self.head
        found = now.getData() == item
        while not found and now != self.tail:
            now = now.getNext()
            found = now.getData() == item
        return found

    def index(self, item):
        now = self.head
        count = -1
        while now.getData() != item:
            now = now.getNext()
            count += 1
        return count

    def remove(self, item):
        now = self.head
        while now.getData() != item:
            now = now.getNext()
        now.getPrev().setNext(now.getNext())
        now.getNext().setPrev(now.getPrev())
        now.setNext(None)
        now.setPrev(None)

    def pop(self, item=None):
        if item == None:
            now = self.getTail()
        else:
            now = self.head.getNext()
            for i in range(item):
                now = now.getNext()
        now.getPrev().setNext(now.getNext())
        now.getNext().setPrev(now.getPrev())
        now.setNext(None)
        now.setPrev(None)
        return now.getData()

    def insert(self, pos, item):
        node = Node(item)
        now = self.head
        count = 0
        while count != pos:
            now = now.getNext()
            count += 1
        node.setNext(now.getNext())
        now.getNext().setPrev(node)
        now.setNext(node)
        node.setPrev(now)

    def __len__(self):
        return self.size()

    def __getitem__(self, item):
        lst = []
        now = self.head.getNext()
        while now != self.tail:
            lst.append(now.getData())
            now = now.getNext()
        return lst.__getitem__(item)

    def __repr__(self):
        lst = []
        now = self.head.getNext()
        while now != self.tail:
            lst.append(now.getData())
            now = now.getNext()
        return str(lst)

    def __eq__(self, other):
        pass

    def __iter__(self, other):
        pass





# 检验
print("======== 5-DoublyLinkedList ========")
mylist = DoublyLinkedList()
for i in range(0, 20, 2):
    mylist.append(i)
mylist.add(3)
mylist.remove(6)
print(mylist.getTail().getPrev().getData())  # 16
print(mylist.isEmpty())  # False
print(mylist.search(5))  # False
print(mylist.size())  # 10
print(mylist.index(2))  # 2
print(mylist.pop())  # 18
print(mylist.pop(2))  # 2
print(mylist)  # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(len(mylist))  # 9
print(mylist[4])  # 8
print(mylist[3:8:2])  # ['10', 10, 14]

a = DoublyLinkedList()
a.add(1)
a.add(2)
a.remove(1)
print(a, a.size())
