from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


# 词梯问题用字典构造"桶",将有n-1个字符相同的长n的单词进行分类,方便以更低的复杂度建立连接
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


# 广度优先搜索(BFS)来解决词梯问题
def bfs(graph, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()  # 利用队列储存邻接的顶点
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()  # 对出列的顶点进行操作
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':  # 这是pythonds中写好的初始化属性,为白色,代表了此顶点未被探索过
                nbr.setColor('gray')  # 一个顶点第一次被发现,则被标记为灰色
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')  # 一个顶点的所有邻接顶点都被探索后会被标记为黑色


# 此bfs算法保证可以得到最短词梯的关键是顶点的颜色,被探索过的顶点被标注为灰色,而只有白色顶点才会被探索
# 而这保证了顶点之间的Pred指向关系是最短的

def traverse(vert):  # 回溯算法打印出词梯的过程
    currentVert = vert
    while currentVert.getPred():
        print(currentVert.getId())
        currentVert = currentVert.getPred()
    print(currentVert.getId())


wordGraph = buildGraph('fourletterwords.txt')  # 根据词表构建图(依据"桶"来构建)
bfs(wordGraph, wordGraph.getVertex('FOOL'))  # bfs过程中记录了关键的"父顶点"信息,用于下面的回溯过程得出最短词梯
traverse(wordGraph.getVertex('SAGE')) # 找到最短的词梯
