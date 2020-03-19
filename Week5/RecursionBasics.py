# 递归Recursion，三定律：存在最小规模问题的解法；具有朝问题规模减小的方向发展的趋势；调用自身

# 列表求和：使用递归而不使用迭代循环
def ListSum(lst):
    if len(lst) == 1:  # 最小规模问题的解法
        return lst[0]
    else:
        return lst[0] + ListSum(lst[1:])  # 将问题规模减小，通过调用自身的方法实现


print('========列表求和========')
print(ListSum([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 十进制数向2-16任意进制转换
def toStr(num, base):
    char = '0123456789ABCDEF'
    if num < base:  # 最小规模问题的解法
        return char[num]
    else:
        return toStr(num // base, base) + char[num % base]  # 调用自身，减小问题规模


# 从这个调用自身就可以看出，想要完全想清楚调用自身的过程，在某些问题上有些麻烦，只需要知道调用自身减小问题规模就行

print('========进制转换========')
print(toStr(315, 16))

# 递归的实现过程中存在一个调用栈，调用（调用的函数存在栈帧中）和返回的顺序是相反的，先进后出
# 调用栈溢出：递归太慢或者无限递归会导致RecursionError
# sys模块：可以查看与更改栈帧的限制深度

# 递归可视化：海龟作图，分形树的绘制
import turtle

t = turtle.Turtle()
t.pencolor('brown')
t.pensize(2)


def DrawSpiral(t, len):  # 利用递归调用绘制螺旋线
    if len > 0:  # 这里相当于限制了最小规模问题的解法
        t.forward(len)
        t.right(90)
        DrawSpiral(t, len - 5)  # 调用自身减小规模


# DrawSpiral(t, 200)
# turtle.done()

# 绘制分形树
def Tree(len):
    if len > 5:  # 最小规模的限制
        t.forward(len)  # 画树干
        t.right(20)
        Tree(len - 15)  # 调用自身，减小规模，调整角度画右树枝
        t.left(40)
        Tree(len - 15)  # 调用自身，减小规模，调整角度画左树枝
        t.right(20)
        t.backward(len)  # 回到出发点（这很重要，否则无法画其他的树枝）


print('========分形树的绘制========')
t.left(90)
t.penup()
t.backward(100)
t.pendown()
Tree(75)
t.hideturtle()
turtle.done()


# 汉诺塔问题，通过递归调用很简单就能实现
def MoveTower(num, pole1, pole2, pole3):
    if num >= 1:
        MoveTower(num-1, pole1, pole3, pole2)
        Move(num, pole1, pole3)
        MoveTower(num-1, pole2, pole1, pole3)

moves = 0
def Move(num, pole1, pole2):
    global moves
    moves += 1
    print(f'Moved disk[{num}] from {pole1} to {pole2}') # 用打印字符串的方法来表示移动的过程
# 这太神奇了，这个模拟完全是虚拟的，甚至没有对应三个柱子的数据对象，太神奇了
print('========汉诺塔问题========')
MoveTower(5, 'pole1', 'pole2', 'pole3')
print('Moves needed:'+str(moves)) # 可以发现，需要的移动次数为2^num-1，恐怖的指数级增长

# 运用递归实现的圆括号检查
def ParCheck(s, n=0):
    if s:
        if s[0] == '(':
            n += 1 # 这个n实际上是储存了有多少个左括号的信息
        else:
            n -= 1
            if n < 0:
                return False
        return ParCheck(s[1:], n)
    else:
        return n == 0


print('========圆括号匹配检验========')
print(ParCheck('(((())))'), ParCheck('((((())))())'))