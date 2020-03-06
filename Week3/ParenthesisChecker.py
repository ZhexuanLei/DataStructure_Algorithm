# 利用python的列表容器类型。实现栈的定义
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

#利用栈，实现判断输入的含各种括号的字符串是否满足括号的正确性（正确对应、正确嵌套）
#输入一个只含有“(){}[]”六种字符的字符串，输出其排列是否正确
def match(par1,par2):
    opens = '([{'
    closers = ')]}'
    if opens.index(par1) == closers.index(par2):
        return True
    else:
        return False

def ParChecker(parstr):
    Match = True
    parstack = Stack()
    for i in range(len(parstr)):
        if parstr[i] in '([{':
            parstack.push(parstr[i])
        elif not parstack.isEmpty():
            if match(parstack.peek(),parstr[i]):
                parstack.pop()
            else:
                return False
        else:
            Match = False
    if Match and parstack.isEmpty():
        return True
    else:
        return False

par = input()
print(ParChecker(par))
