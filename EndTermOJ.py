print('========二叉树路径========')


class BinaryTreeNode:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, val):
        if val > self.value:
            if not self.rightChild:
                self.rightChild = BinaryTreeNode(val)
            else:
                self.rightChild.insert(val)
        else:
            if not self.leftChild:
                self.leftChild = BinaryTreeNode(val)
            else:
                self.leftChild.insert(val)


def buildPath(node, path):
    if node:
        path += str(node.value)
        if (not node.leftChild and not node.rightChild):
            pathList.append(path)
        else:
            path += '->'
            buildPath(node.leftChild, path)
            buildPath(node.rightChild, path)
    else:
        pass


# numList = list(map(int, input().split()))
pathList = []
numList = [5, 2, 6, 1, 3, 7, 4]
oriTreeNode = BinaryTreeNode(numList[0])
for vals in numList[1:]:
    oriTreeNode.insert(vals)
buildPath(oriTreeNode, '')
for path in pathList:
    print(path)

print('========入室抢劫========')

# numList = list(map(int, input().split()))
numList = [2, 1, 2, 3]
if not numList:
    print(0)
dpList = [0] * (len(numList) + 1)  # 第i个元素表示输入列表前i个对应的可能最大收益
dpList[1] = numList[0]
for index in range(2, len(numList) + 1):
    dpList[index] = max(dpList[index - 1], dpList[index - 2] + numList[index - 1])
print(dpList[-1])  # 返回可能的最大收益
