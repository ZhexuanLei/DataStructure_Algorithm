# 由于OJ提交时不能import，所以此处每一个脚本中都定义一个栈类型
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return(self.items == [])

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

# 输入一个含字母的字符串，消去相邻的相同字母（消除后空格两侧相邻的也算），输出消除后的字符串，如果消完，输出None

def OneDAniPop(str):
    s = Stack()
    for i in range(len(str)):
        if s.isEmpty():
            s.push(str[i])
        elif str[i] == s.peek():
            s.pop()
        else:
            s.push(str[i])
    if s.isEmpty():
        return None
    else:
        s1 = Stack()
        while not s.isEmpty():
            s1.push(s.pop())
        lst1 = []
        while not s1.isEmpty():
            lst1.append(s1.pop())
        return ''.join(lst1)

inputstr = input()
print(OneDAniPop(inputstr))