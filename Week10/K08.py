class BinaryTree():
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
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

    def __repr__(self):
        tlist = ['', [], []]
        if self:
            tlist[0] = self.getRootValue()
            if self.getLeftChild():
                tlist[1] = self.getLeftChild().__repr__()
            else:
                tlist[1] = []
            if self.getRightChild():
                tlist[2] = self.getRightChild().__repr__()
            else:
                tlist[2] = []
        return tlist

    def __str__(self):
        tlist = ['', [], []]
        if self:
            tlist[0] = self.getRootValue()
            if self.getLeftChild():
                tlist[1] = self.getLeftChild().__repr__()
            else:
                tlist[1] = []
            if self.getRightChild():
                tlist[2] = self.getRightChild().__repr__()
            else:
                tlist[2] = []
        return str(tlist)

    def height(self):
        if (not self.getRightChild()) and (not self.getLeftChild()):
            return 1
        elif self.getLeftChild() and self.getRightChild():
            return max(1 + self.getLeftChild().height(), 1 + self.getRightChild().height())
        elif not self.getRightChild():
            return 1 + self.getLeftChild().height()
        else:
            return 1 + self.getRightChild().height()


def buildTree():
    t = BinaryTree('a')
    t.insertLeft('b')
    t.insertRight('c')
    t.getLeftChild().insertRight('d')
    t.getRightChild().insertLeft('e')
    t.getRightChild().insertRight('f')
    return t


print(buildTree())
print(buildTree().height())
