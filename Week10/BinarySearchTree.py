class TreeNode():
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):  # 判断是否为其父节点的左子节点(因此要求存在父节点,用and)
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):  # 判断是否是根节点,只需判断其是否存在父节点即可
        return not self.parent

    def isLeaf(self):  # 判断是否是叶节点,只需判断其是否存在左子节点或右子节点
        return not (self.leftChild and self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for item in self.leftChild:
                    yield item
            yield self.key
            if self.hasRightChild():
                for item in self.rightChild:
                    yield item

    def findSuccesor(self):  # 找到一个节点的右子树中最小的节点
        succ = None
        if self.hasRightChild():
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
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def sliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        else:
            if self.hasLeftChild():
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


class BianrySearcTree():
    def __init__(self):
        self.root = None  # 根引用TreeNode类
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):  # put函数的辅助函数,用于向非空的二叉查找树插入节点,是递归函数
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key < key:
            return self._get(key, currentNode.rightChild)
        else:
            return self._get(key, currentNode.leftChild)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delete__(self, instance):
        self.delete(instance)

    def remove(self, currentNode):
        if currentNode.isLeaf():  # 无子节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif not currentNode.hasBothChild():  # 有一个子节点
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)
        else:  # 有两个子节点,这种情况的复杂之处在于需要找到一个合适的节点来替换被移除的节点:这个节点就是被删除节点的右子树中最小的节点
            succ = currentNode.findSuccessor()  # 两个TreeNode类的辅助函数
            succ.sliceOut()  # 将该后继节点提出来
            currentNode.key = succ.key
            currentNode.payload = succ.payload


