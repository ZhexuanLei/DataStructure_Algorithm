# ======= 1 中缀表达式求值 =======
# 通过把“中缀转后缀”和“后缀求值”两个算法功能集成在一起（非简单的顺序调用），
# 实现对中缀表达式直接求值，新算法还是从左到右扫描中缀表达式，
# 但同时使用两个栈，一个暂存操作符，一个暂存操作数，来进行求值。
#
# 创建一个函数，接受参数为一个字符串，即一个中缀表达式，
# 其中每个数字或符号间由一个空格隔开；
# 返回一个整数，即求值的结果。（支持 + - * / ^ 五种运算）
#   其中“ / ”定义为真除True DIV，结果是浮点数类型
# 输入样例1：
# ( 2 + 3 ) * 6 + 4 / 2
# 输出样例1：
# 32.0
# 输入样例2：
# 2 ^ 3 + 4 * 5 - 16 / 2
# 输出样例2：
# 20.0
# 输入样例3：
# ( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6
# 输出样例3：
# 1.0


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __repr__(self):
        s = '|'
        for i in self.items:
            s += str(i)
            s += ' '
        return s

    __str__ = __repr__


def calculate(s) -> float:
    oplst = s.split()
    OpStack = Stack()
    priority = {'+': 1, '-': 2, '*': 3, '/': 3, '^': 4} # 规定操作符的优先级

    # 定义计算用的函数
    def cal(op1, op2, opt):
        if opt == '+':
            return op1 + op2
        elif opt == '-':
            return op1 - op2
        elif opt == '*':
            return op1 * op2
        elif opt == '/':
            return op1 / op2
        else:
            return op1 ** op2

    # 定义了一个计算不含括号的中缀表达式的函数，其中使用了两个栈分别暂存操作数与操作符
    def getvalue(opstack):
        lst = []
        S1 = Stack()
        while not opstack.isEmpty():
            S1.push(opstack.pop())
        while not S1.isEmpty():
            lst.append(S1.pop())
        optStack = Stack()
        opdStack = Stack()
        for op in lst:
            if type(op) == float:
                opdStack.push(int(op))
            elif optStack.isEmpty():
                optStack.push(op)
            elif priority[optStack.peek()] < priority[op]:
                optStack.push(op)
            else:
                while not optStack.isEmpty() and not opdStack.isEmpty() \
                        and priority[optStack.peek()] >= priority[op]:
                    # 计算中缀表达式的核心部分，比较新读到的操作符与栈顶操作符的优先级关系，如果栈顶的更大，
                    # 则需要先行计算出结果；继续如此比较至                读到的操作符优先级大于栈顶的操作符，此时读到的操作符入栈
                    opd2 = opdStack.pop()
                    opd1 = opdStack.pop()
                    opt = optStack.pop()
                    opdStack.push(cal(opd1, opd2, opt))
                optStack.push(op)
        while not optStack.isEmpty():
            opd2 = opdStack.pop()
            opd1 = opdStack.pop()
            opt = optStack.pop()
            opdStack.push(cal(opd1, opd2, opt))
        return float(opdStack.pop())

    # 包含了括号后的中缀表达式求值
    for op in oplst:
        if op.isdigit():
            OpStack.push(float(op))
        elif op == '(':
            OpStack.push(op)
        elif op == ')':
            opttop = OpStack.pop()
            s1, s2 = Stack(), Stack()
            s1.push(OpStack.pop())
            while opttop != '(':
                s1.push(opttop)
                opttop = OpStack.pop()
            while not s1.isEmpty():
                s2.push(s1.pop())
            OpStack.push(getvalue(s2))
        else:
            OpStack.push(op)
    return getvalue(OpStack)


# 调用检验
print("======== 1-calculate ========")
print(calculate("( 2 + 3 ) * 6 + 4 / 2"))
print(calculate("2 ^ 3 + 4 * 5 - 16 / 2"))
print(calculate("( 5 + 1 ) * 2 / 3 - 3 ^ ( 2 + 8 / 4 ) / 9 + 6"))
