# ======= 3 HTML标记匹配 =======
# 实现扩展括号匹配算法，用来检查HTML文档的标记是否匹配。
# HTML标记应该成对、嵌套出现，
# 开标记是<tag>这种形式，闭标记是</tag>这种形式。
#
# 创建一个函数，接受参数为一个字符串，为一个HTML文档中的内容，
# 返回True或False，表示该字符串中的标记是否匹配。
# 输入样例1：
# <html> <head> <title> Example </title> </head> <body> <h1>Hello, world</h1> </body> </html>
# 输出样例1：
# True
# 输入样例2：
# <html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>
# 输出样例2：
# False

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


def HTMLMatch(s) -> bool:
    signlst = s.split('<')
    signlst.remove('')
    for i in range(len(signlst)): # 从输入的字符串中分离出所有的标记，并去除文本，得到一个包含所有标记的列表
        splitstr = '<'
        j = 0
        while signlst[i][j] != '>':
            splitstr += signlst[i][j]
            j += 1
        splitstr += '>'
        signlst[i] = splitstr

    SignStack = Stack() # 用第一题定义过的栈类进行左标记的暂存
    match = True
    for sign in signlst:
        slst = [i for i in sign]
        if SignStack.isEmpty() or '/' not in sign:
            SignStack.push(sign)
        else:
            slst.remove('/')
            if ''.join(slst) == SignStack.peek():
                SignStack.pop()
            else:
                match = False
    if SignStack.isEmpty():
        pass
    else:
        match = False
    return match

# 调用检验
print("======== 3-HTMLMatch ========")
print(
    HTMLMatch(
        "<html> <head> <title>Example</title> </head> <body> <h1>Hello, world</h1> </body> </html>"
    ))
print(
    HTMLMatch(
        "<html> <head> <title> Test </title> </head> <body> <p>It's just a test.</p> <p>And this is for False.<p> </body> </html>"
    ))


