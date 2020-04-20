class LinkedListTree():
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = LinkedListTree(newNode)
        else:
            t = LinkedListTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = LinkedListTree(newNode)
        else:
            t = LinkedListTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRootValue(self):
        return self.key

    def setRootValue(self, newRoot):
        self.key = newRoot

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


print('========树的应用:全括号表达式解析========')


def buildParseTree(fpexp):
    fpList = list(fpexp)
    pStack = Stack()
    expTree = LinkedListTree('')
    pStack.push(expTree)
    currentTree = expTree
    for i in fpList:  # 遍历操作数与操作符
        if i == '(':  # 如果读到左括号,则创建左子树,当前节点下降
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i in ['+', '-', '*', '/']:  # 读到操作符,则将当前节点的根值设为操作符,创建右子树,当前节点下降
            currentTree.setRootValue(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':  # 读到右括号,当前节点上升,回到父节点
            currentTree = pStack.pop()
        else:  # 读到数字,设定当前节点根值为该数,当前节点上升,回到父节点
            currentTree.setRootValue(int(i))
            currentTree = pStack.pop()
    return expTree


# 使用递归函数求解表达式解析树的值
import operator


def evaluate(expTree):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    leftChild = expTree.getLeftChild()
    rightChild = expTree.getRightChild()
    if leftChild and rightChild:
        op = operators[expTree.getRootValue()]
        return op(evaluate(leftChild), evaluate(rightChild))
    else:
        return expTree.getRootValue()


print(evaluate(buildParseTree('(3-(4*5))')))  # 这个问题就在于最外层只能有一个操作符,毕竟是基于二叉树的

print('========树的遍历========')


# 相比于线性数据结构,树的遍历更加困难


def preorder(tree):  # 前序遍历
    if tree:
        print(tree.getRootValue())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def inorder(tree):  # 中序遍历
    if tree:
        preorder(tree.getLeftChild())
        print(tree.getRootValue())
        preorder(tree.getRightChild())


def postorder(tree):  # 后序遍历
    if tree:
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRootValue())


def printexp(tree): # 生成中缀表达式
    sVal = ''
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal += str(tree.getRootValue())
        sVal += printexp(tree.getRightChild()) + ')'
    return sVal