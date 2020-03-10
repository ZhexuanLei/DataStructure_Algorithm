# 数算课程上的一些小练习，在PyLn平台上保存后在canvas上提交代码文件分享链接

# 输入一个奇数n，输出一个由#组成的、底边含n个#的、空心的等腰三角形
'''
n = int(input("Please input a odd number:"))
print(" "*int((n-1)/2)+"#")
for i in range(int((n-1)/2)-1):
    print(" "*(int((n-3-2*i)/2))+"#"+" "*(2*i+1)+"#")
if n>1:
    print("#"*n)
'''

# 输入一个英文字母组成的字符串，将其中的e替换为3，ee替换为E3，输出替换后的字符串
'''
orilst=list(input("Please input a word:"))
orilst.append(" ")
chalst = []
for i in range(len(orilst)-1):
    if orilst[i] == "e":
        if orilst[i+1] == "e":
            chalst.append("E3")
            orilst[i+1]=" "
        else:
            chalst.append("3")
    else:
        chalst.append(orilst[i])
print("".join(chalst).replace(" ",""))
'''

# 判断list两个添加值得操作的时间复杂度
'''
from timeit import Timer

for i in range(100000,1000001,100000):
    lst = [j for j in range(i)]
    t1 = Timer('lst.insert(0, None)','from __main__ import lst')
    t2 = Timer('lst.append(None)','from __main__ import lst')
    res1, res2 = t1.timeit(number=1000), t2.timeit(number=1000)
    print('%.7f' %res1, '%.7f' %res2)
'''


# 后缀表达式求值
class Stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()


    def __repr__(self):
        s='|'
        for i in self.items:
            s += str(i)
            s += ' '
        return s
    __str__ = __repr__


def postfix(exp):
    opstack = Stack()
    lst = exp.split()
    for i in lst:
        if i in '0123456789':
            opstack.push(int(i))
        else:
            op2 = opstack.pop()
            op1 = opstack.pop()
            result = calc(i, op1, op2)
            opstack.push(result)
        print(opstack)
    return opstack.pop()


def calc(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

print(postfix('2 3 * 4 +'))
print(postfix('1 2 + 3 + 4 + 5 +'))
print(postfix('1 2 3 4 5 * + * +'))

