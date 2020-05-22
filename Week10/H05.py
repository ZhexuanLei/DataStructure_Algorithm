# uuid_share#  2ab430a7-276d-4893-85d0-38d92bc77a65  #
# SESSDSA20课程上机作业
# 【H5】AVL树作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中指定部位编写代码
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业代码部分在4月29日18:00之前提交到PyLn编程学习系统，班级码见Canvas系统

# ---- 用AVL树实现字典类型 ----
# 用AVL树来实现字典类型，使得其put/get/in/del操作均达到对数性能
# 采用如下的类定义，至少实现下列的方法
# key至少支持整数、浮点数、字符串
# 请调用hash(key)来作为AVL树的节点key
# 【注意】涉及到输出的__str__, keys, values这些方法的输出次序是AVL树中序遍历次序
#    也就是按照hash(key)来排序的，这个跟Python 3.7中的dict输出次序不一样。

# 请在此编写你的代码


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = hash(key)
        self.name = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def getLeft(self):  # 获取左子树 (不存在时返回None)
        return self.leftChild

    def getRight(self):
        return self.rightChild

    def isLeftChild(self):  # 判断是否为其父节点的左子节点(因此要求存在父节点,用and)
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):  # 判断是否是根节点,只需判断其是否存在父节点即可
        return not self.parent

    def isLeaf(self):  # 判断是否是叶节点,只需判断其是否存在左子节点或右子节点
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def height(self):
        if self.isLeaf():
            return 1
        elif self.getLeft() and self.getRight():
            return 1 + max(self.getLeft().height(), self.getRight().height())
        elif not self.getRight():
            return 1 + self.getLeft().height()
        else:
            return 1 + self.getRight().height()

    def balanceFactor(self):
        if self.isLeaf():
            return 0
        elif self.getLeft() and self.getRight():
            return self.getLeft().height() - self.getRight().height()
        elif not self.getRight() == None:
            return self.getLeft().height()
        else:
            return self.getRight().height() * -1

    def replaceNodeData(self, key, val, lc, rc):  # 重新定义某个节点,为其各属性赋值
        self.key = hash(key)
        self.name = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        if self.getLeft():
            self.leftChild.parent = self
        if self.getRight():
            self.rightChild.parent = self

    def replaceNodeValue(self, key, val):
        self.key = hash(key)
        self.name = key
        self.payload = val

    def __iter__(self):
        if self:
            if self.getLeft():
                for item in self.leftChild:
                    yield item
            yield self.name
            if self.getRight():
                for item in self.rightChild:
                    yield item

    def findSuccessor(self):  # 找到一个节点的右子树中key最小的节点
        succ = None
        if self.getRight():
            succ = self.rightChild.findMin()
        else:  # 这一段在下面BST类中不会用到,因此此寻找后继函数只在同时有两个子节点的情况下用到了
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccesor()
                    self.parent.rightChild = self

        return succ

    def findMin(self):
        current = self
        while current.getLeft():
            current = current.leftChild
        return current

    def sliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        else:
            if self.getLeft():
                if self.isLeftChild():  # 同理,这段条件分支在下方BST类中也不会引用到
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def treePrint(self):  # 是AVL树类__str__方法的辅助函数,不过没用了
        dict1 = {}
        if self.height() < 2:
            if self.getLeft():
                dict1[self.leftChild.name] = self.leftChild.payload
            dict1[self.name] = self.payload
            if self.getRight():
                dict1[self.rightChild.name] = self.rightChild.payload
            return dict1
        else:
            if self.getLeft():
                dict1.update(self.leftChild.treePrint())
            dict1[self.name] = self.payload
            if self.getRight():
                dict1.update(self.rightChild.treePrint())
            return dict1


class mydict:
    def __init__(self):  # 创建一个空字典
        self.root = None
        self.size = 0

    def getRoot(self):  # 返回内部的AVL树根
        return self.root

    def __setitem__(self, key, value):  # 将key:value保存到字典
        if self.root:
            self.put(key, value, self.root)  # 辅助函数,向非空的AVL树中插入节点
        else:
            self.root = TreeNode(key, value)
            self.size = 1

    def put(self, key, value, currentNode):
        if hash(key) < currentNode.key:
            if currentNode.getLeft():
                self.put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)
                self.size += 1
                self.updateBalance(currentNode.leftChild)
        elif hash(key) > currentNode.key:
            if currentNode.getRight():
                self.put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)
                self.size += 1
                self.updateBalance(currentNode.rightChild)
        else:
            currentNode.payload = value

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):  # 这是为了平衡新的树而写的方法,通过调整节点位置实现,为下面的rebalance函数服务
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():  # 此时rotRoot的父节点还没有变
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor += 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor += 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):  # 右旋是类似的
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor += -1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor += -1 + min(rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def __getitem__(self, key):  # 从字典中根据key获取value
        if self.root:
            res = self.get(key, self.root)
            if res:
                return res.payload
            else:
                raise KeyError('Error, key not in tree')
        else:
            raise KeyError('Error, key not in tree')

    def get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == hash(key):
            return currentNode
        elif currentNode.key < hash(key):
            return self.get(key, currentNode.rightChild)
        else:
            return self.get(key, currentNode.leftChild)

    def __delitem__(self, key):  # 删除字典中的key
        if self.size > 1:
            nodeToRemove = self.get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)  # 这里移除之后似乎还需要update平衡情况
                # self.updateBalance(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == hash(key):
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, currentNode):
        if currentNode.isLeaf():  # 无子节点
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
                currentNode.parent.balanceFactor -= 1
            else:
                currentNode.parent.rightChild = None
                currentNode.parent.balanceFactor += 1
            self.updateBalanceRemove(currentNode.parent)  # 针对删除的更新平衡
        elif not currentNode.hasBothChildren():  # 有一个子节点
            if currentNode.getLeft():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.parent.balanceFactor -= 1
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.parent.balanceFactor += 1
                else:
                    currentNode.leftChild.parent = None
                    self.root = currentNode.leftChild
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.parent.balanceFactor -= 1
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.parent.balanceFactor += 1
                else:
                    currentNode.rightChild.parent = None
                    self.root = currentNode.rightChild
            if currentNode.parent:
                self.updateBalanceRemove(currentNode.parent)
        else:  # 有两个子节点,这种情况的复杂之处在于需要找到一个合适的节点来替换被移除的节点:这个节点就是被删除节点的右子树中最小的节点
            succ = currentNode.findSuccessor()  # 两个TreeNode类的辅助函数
            if succ.isLeftChild():
                succ.parent.balanceFactor -= 1
            else:
                succ.parent.balanceFactor += 1
            succ.sliceOut()  # 将该后继节点提出来
            currentNode.replaceNodeValue(succ.name, succ.payload)
            self.updateBalanceRemove(succ.parent)

    def updateBalanceRemove(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            node = node.parent
        if node.parent != None and node.balanceFactor == 0:
            if node.isLeftChild():
                node.parent.balanceFactor -= 1
            elif node.isRightChild():
                node.parent.balanceFactor += 1
            self.updateBalanceRemove(node.parent)

    def __len__(self):  # 获取字典的长度
        return self.size

    def __contains__(self, key):  # 判断字典中是否存在key
        if self.get(key, self.root):
            return True
        else:
            return False

    def clear(self):  # 清除字典
        self.root = None
        self.size = 0

    def __iter__(self):
        if self.root:
            return iter(self.root)
        return iter([])

    def __str__(self):  # 输出字符串形式，参照内置dict类型，输出按照AVL树中序遍历次序
        lstr = ', '.join([f"{repr(key)}: {repr(self[key])}" for key in self])
        return f"{{{lstr}}}"

    __repr__ = __str__

    def keys(self):  # 返回所有的key，类型是列表，按照AVL树中序遍历次序
        klst = []
        if not self.root:
            return []
        else:
            for name in self.root:
                klst.append(name)
        return klst

    def values(self):  # 返回所有的value，类型是列表，按照AVL树中序遍历次序
        vlst = []
        if not self.root:
            return []
        else:
            for name in self.root:
                vlst.append(self[name])
        return vlst


# 代码结束

# mydict=dict
# 检验

print("========= AVL树实现字典 =========")
md = mydict()
md['hello'] = 'world'
md['name'] = 'sessdsa'
print(md)  # {'name': 'sessdsa', 'hello': 'world'}

for f in range(1000):
    md[f ** 0.5] = f

for i in range(1000, 2000):
    md[i] = i ** 2

print(len(md))  # 2002
print(md[2.0])  # 4
print(md[1000])  # 1000000
print(md['hello'])  # world
print(20.0 in md)  # True
print(99 in md)  # False

del md['hello']
print('hello' in md)  # False
for i in range(1000, 2000):
    del md[i]
print(len(md))  # 1001
for f in range(1000):
    del md[f ** 0.5]
print(len(md))  # 1
print(md.keys())  # ['name']
print(md.values())  # ['sessdsa']
for a in md.keys():
    print(md[a])  # sessdsa
md.clear()
print(md)  # {}
