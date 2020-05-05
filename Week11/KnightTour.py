from pythonds.graphs import Graph, Vertex


def genLegalMoves(x, y, bdsize):  # 生成合理的新位置(走日以及在棋盘内)
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]  # "马走日"的八个位置
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdsize) and legalCoord(newY, bdsize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdsize):  # 保证在棋盘内
    if x >= 0 and x < bdsize:
        return True
    else:
        return False


def knightGraph(bdSize):  # 生成骑士周游图
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph


def posToNodeId(row, col, bdSize):  # 为每个顶点提供一个特征的id,用于作为图中的顶点id
    return row * bdSize + col


# 上面函数实现了骑士周游图的建立,下面对骑士周游问题进行实现
# 采用广度优先搜索

def knighTour(n, path, u, limit):  # n表示走过的顶点数;path记录了走过的顶点;u表示当前顶点;limit表示搜索总深度(由棋盘大小决定)
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        # 这里取出了所有的合法移动(注:要采用优化的Warnsdorff算法,将此nbrList改为用orderByAvail函数排出的列表即可)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knighTour(n + 1, path, nbrList[i], limit)  # 递归调用,对未探索的顶点深入,即把当前顶点设为该未探索的顶点
            i += 1
        if not done:  # 此处表示如果当前顶点之后的所有路径都无法完成总深度,则回到同层的下一个顶点继续尝试
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


# 上述的算法是指数级复杂度的,很恐怖,但有一种改进的算法:Warnsdorff算法.
# 通过对下一步八个位置的排序,使骑士尽量先访问下一步合理位置最少的顶点,保证骑士先在棋盘外围移动,最后来到中心,减少不合格路径消耗的时间
# 这是一种利用对问题存在的先验性知识所制定的"启发式规则".
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]

# 所以应该怎么调用骑士周游函数?输出是啥?难道不是输出一个路径吗?还是只能判断某个路径行不行?