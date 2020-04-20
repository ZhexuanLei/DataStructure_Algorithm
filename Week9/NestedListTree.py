def NestedListTree(root):  # 嵌套列表表示的二叉树（当然也可以是多叉的），每个列表第一个元素表示树或者子树的根，后面的列表表示该根的子树
    return [root, [], []]


def insertLeft(subtree, newBranch):  # 在选定的根下插入左子树，则将原左子树下推一层
    t = subtree.pop(1)
    if len(t) > 1:
        subtree.insert(1, [newBranch, t, []])
    else:
        subtree.insert(1, [newBranch, [], []])


def insertRight(subtree, newBranch):
    t = subtree.pop(2)
    if len(t) > 1:
        subtree.insert(2, [newBranch, [], t])
    else:
        subtree.insert(2, [newBranch, [], []])


def getRootValue(subtree): # 读取某个子树的根值
    return subtree[0]


def setRootValue(subtree, newValue): # 改变某个子树的根值
    subtree[0] = newValue


def getLeftChild(subtree): # 读取某个子树的左子树
    return subtree[1]


def getRightChild(subtree):
    return subtree[2]

T = NestedListTree(1)
print(T)
insertLeft(T, 2)
print(T)
insertLeft(T[1], 3)
print(T)
insertLeft(T[1], 4)
print(T)
insertRight(T[1], 5)
print(T)