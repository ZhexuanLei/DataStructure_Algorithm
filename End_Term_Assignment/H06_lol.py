import json
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes


class Vertex:
    # 创建演员代表的节点，包含属性：演员名称；；
    def __init__(self, name, movie, typ, star):
        self.name = name  # 演员名称
        self.collaborators = {}  # 演员的合作者（连接的节点，字典，key为合作者顶点，value为合作电影的列表）
        self.movies = {movie: (typ, star)}  # 演员出演的电影列表，为一个字典
        self.searched = False  # 搜索用到的属性
        self.distance = 0  # 计算直径中用到的属性

    def addMovie(self, movie, typ, star):  # 添加演员所出演的电影进入出演电影列表
        self.movies[movie] = (typ, star)

    def addCollaborator(self, nbr, commom, typ, star):  # 新增合作者
        self.collaborators[nbr] = {commom: (typ, star)}

    def addCommon(self, nbr, common, typ, star):  # 原有合作者，新增合作电影
        self.collaborators[nbr][common] = (typ, star)

    def __str__(self):
        return str(self.name) + ' collaborated with ' + str([x.name for x in self.collaborators])

    def getCollaborators(self):
        return self.collaborators.keys()

    def getName(self):
        return self.name

    def getCommon(self, nbr):  # 返回与特定合作者合作的电影列表
        return self.collaborators[nbr]

    def setStatus(self, bo):  # 用于搜索
        self.searched = bo


class Graph:  # 基于邻接列表的图模型
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, name, movie, typ, star):
        self.numVertices += 1
        newVertex = Vertex(name, movie, typ, star)
        self.vertList[name] = newVertex
        return newVertex

    def getVertex(self, name):
        if name in self.vertList:
            return self.vertList[name]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, f, t, movie, star):
        self.vertList[f].addCollaborator(self.vertList[t], movie, star)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


# 读入数据
with open('Film.json', encoding='utf-8') as fp:
    filmLst = json.load(fp)  # 得到一个列表，其中各元素为一个包含电影信息的字典
    fp.close()


def construct(lst):  # 构建图数据结构
    g = Graph()
    for movieInfo in lst:
        actLst = movieInfo['actor'].split(',')
        title = movieInfo['title']
        typ = movieInfo['type']
        star = movieInfo['star']
        for pos in range(len(actLst)):
            actor = actLst[pos]
            if actor not in g:  # 如果是图中没有的新演员则将其作为新的顶点加入
                g.addVertex(actor, title, typ, star)
                # 对于后方的其他演员进行遍历，这样减少了操作次数
                for num in range(pos + 1, len(actLst)):
                    addCo(actor, actLst[num], title, typ, star, g)
            else:  # 如果是已经在图中的演员
                g.getVertex(actor).addMovie(title, typ, star)
                for num in range(pos + 1, len(actLst)):
                    addCo(actor, actLst[num], title, typ, star, g)
    return g


# 添加合作者或者已有合作者之间的合作电影
def addCo(actor, co, title, typ, star, graph):
    coVert = graph.getVertex(co) if co in graph else graph.addVertex(co, title, typ, star)
    if coVert not in graph.vertList[actor].getCollaborators():  # 如果是新的合作者，则创建新的连接
        graph.vertList[actor].addCollaborator(coVert, title, typ, star)
        graph.vertList[co].addCollaborator(graph.vertList[actor], title, typ, star)
    else:  # 如果是原有的合作者,则在原合作电影列表中添加此电影
        graph.vertList[actor].addCommon(coVert, title, typ, star)
        graph.vertList[co].addCommon(graph.vertList[actor], title, typ, star)


# 以某一个节点为起始进行深度优先搜索，找到其所在的连通分支，返回演员列表与所有合作的电影列表
def dfs(vert):
    nameLst, stack, movieDic = [], [], {}
    stack.append(vert)
    vert.setStatus(True)  # 此处设定状态为True代表已搜索
    nameLst.append(vert.name)
    while len(stack) > 0:
        currentVert = stack[-1]
        coLst = currentVert.getCollaborators()
        for co in coLst:
            if not co.searched:
                stack.append(co)
                nameLst.append(co.name)
                movie = currentVert.collaborators[co]
                for name in movie:
                    movieDic[name] = movie[name]
                co.setStatus(True)
        if stack[-1] == currentVert:  # 没有新的顶点入栈，说明搜到最底层
            stack.pop()
    if len(movieDic) == 0:
        for movie in vert.movies:
            movieDic[movie] = vert.movies[movie]
    return nameLst, movieDic


# 找到一个图中所有的连通分支，输出连通分支的数目与连通分支的信息列表
def ConnectedComponent(g):
    ccnum = 0
    cclst = []
    for vert in g:
        if not vert.searched:
            namelst, movlst = dfs(vert)
            ccnum += 1
            cclst.append([len(namelst), namelst, movlst])
    # 返回连通分支的数目以及连通分支的信息列表（分别是演员数目，演员列表，电影列表）
    return ccnum, cclst


# 根据电影字典（名称：类型）计算其中电影类型出现的频数字典（类型：频数），返回按频数排序的列表
def searchType(g, movieDic):
    typeDic = {}
    for movie in movieDic:
        types = movieDic[movie][0].split(',')
        for ty in types:
            typeDic[ty] = 1 if ty not in typeDic else typeDic[ty] + 1
    typeLst = []
    for movie in typeDic:
        typeLst.append((movie, typeDic[movie]))
    sortLst = sorted(typeLst, key=lambda x: x[1], reverse=True)
    return sortLst


# 以某个节点为起点，对一个连通无向图作广度优先搜索
def bfs(vert, bo):
    vert.distance = 0
    vertQueue = []
    vertQueue.append(vert)
    lastVert = vert
    while len(vertQueue) > 0:
        currentVert = vertQueue.pop(0)
        for co in currentVert.collaborators.keys():
            # 由于之前进行过dfs，因此所有节点现在的搜索状态都是True，此处把True看成未搜索即可
            if co.searched == bo:
                co.setStatus(not bo)
                co.distance = currentVert.distance + 1
                lastVert = co
                vertQueue.append(co)
    # 返回最末端的顶点与其距离
    return lastVert.distance, lastVert


# 计算一节点所在连通分支的直径
def diameter(vert):
    # 从任意一节点出发进行广度优先搜索，得到的最远节点一定是直径对应的一端
    last = bfs(vert, True)[1]
    # 再次进行bfs搜索，即可得到连通分支的直径
    dia = bfs(last, False)[0]
    return dia


# 计算电影星级
def star(movieDic):
    sum = 0
    infos = movieDic.values()
    for info in infos:
        sum += info[1]
    return round(sum / len(infos), 2)


print('================图的构建================')
graph = construct(filmLst)
print('共有 ' + str(graph.numVertices) + ' 名演员')

print('================连通分支================')

ccNum, ccLst = ConnectedComponent(graph)
print('共有' + str(ccNum) + '个连通分支')  # 连通分支的数目
sortCC = sorted(ccLst, key=lambda x: x[0], reverse=True)  # 根据连通分支大小排序
# 连通分支信息列表（先加入大小数据，按照连通分支大小排序，且取前20行与后20行）
infoLst = [[i[0]] for i in sortCC[:20]] + [[i[0]] for i in sortCC[-20:]]
partLst = sortCC[:20] + sortCC[-20:]
seq = 0
for m in partLst:
    # 计算电影分类
    typeLst = searchType(graph, m[2])
    types = [i[0] for i in typeLst[:3]]
    infoLst[seq].append(types)  # 加入其中电影所属类别的前三名（按连通分支大小排序）
    # 计算直径
    if m[0] < 100:
        infoLst[seq].append(diameter(graph.getVertex(m[1][0])))
    else:  # 不对最大的连通分支进行直径的计算
        infoLst[seq].append(-1)
    # 计算电影平均星级
    infoLst[seq].append(star(m[2]))
    seq += 1

print('按照大小进行排序，排名前20和后20的连通分支的：大小、电影类型前三名、直径以及电影平均星级为：')
for i in infoLst:
    print(', '.join(str(j) for j in i))

print('================连通分支信息柱状图================')

X = [i for i in range(1, 21)] + [i for i in range(ccNum - 19, ccNum + 1, 1)]
sizes = [i[0] for i in infoLst]
dias = [i[2] for i in infoLst]
stars = [i[3] for i in infoLst]

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
fig = plt.figure(figsize=(10, 4))
print('各连通分支的大小如图所示')
bax = brokenaxes(xlims=((0, 21), (4556, 4578)), ylims=((0, 50), (84682, 84692)))
bax.bar(X, sizes, facecolor='midnightblue')
plt.savefig('size.png')
plt.show()
fig = plt.figure(figsize=(10, 4))
print('各连通分支的直径如图所示')
bax = brokenaxes(xlims=((0, 21), (4556, 4578)))
bax.bar(X, dias, facecolor='midnightblue')
plt.savefig('diameter.png')
plt.show()
fig = plt.figure(figsize=(10, 4))
print('各连通分支的电影平均星级如图所示')
bax = brokenaxes(xlims=((0, 21), (4556, 4578)))
bax.bar(X, stars, facecolor='midnightblue')
plt.savefig('star.png')
plt.show()

print('================周星驰================')
sum1 = 0
vert = graph.getVertex('周星驰')
movies = vert.movies
for m in movies:
    sum1 += movies[m][1]
print('周星驰出演电影的平均星级为' + str(round(sum1 / len(movies), 2)))

coS = vert.getCollaborators()
print('周星驰与共同合作者共' + str(len(coS) + 1) + '人')

moviesum, starsum = 0, 0
movieInfo = {}
for co in vert.collaborators:
    movieDic = co.movies
    for mo in movieDic:
        if mo not in movieInfo:
            movieInfo[mo] = movieDic[mo]
            moviesum += 1
            starsum += movieDic[mo][1]
print('他们各自出演的电影一共有' + str(moviesum) + '部，平均星级为' + str(round(starsum / moviesum, 2)))

types = searchType(graph, movieInfo)
print('电影所属类别前三名为' + str(types[0][0].strip()) + ',' + str(types[1][0].strip()) + ',' + str(types[2][0].strip()))

print('================不同类型演员出演电影的平均星级================')
actorLst1 = ['张子枫', '赵丽颖', '郑爽', '景甜', '迪丽热巴', '关晓彤', '杨颖', '古力娜扎', '鹿晗', '陈学冬', '吴亦凡', '王源', '易烊千玺', '王俊凯', '柯震东',
             '黄子韬', '肖战']
actorLst2 = ['章子怡', '周迅', '赵薇', '刘亦菲', '巩俐', '高圆圆', '黄圣依', '姚晨', '徐峥', '姜文', '冯小刚', '葛优', '周星驰', '黄渤', '梁朝伟', '甄子丹',
             '李连杰', '陈道明', '孙红雷']
aveLst1, aveLst2 = [], []
numLst1, numLst2 = [], []
for actor in actorLst1:
    mov = graph.getVertex(actor).movies
    typeLst = searchType(graph, mov)
    starLst = [i[1] for i in list(mov.values())]
    aveStar = star(mov)
    aveLst1.append(aveStar)
    numLst1.append(len(mov))
    print(
        actor + '出演了' + str(len(mov)) + '部电影,主要是' + str(typeLst[0][0]) + '类型的电影,平均星级为' + str(aveStar) + ',最高星级为' + str(
            max(starLst)) + ',最低星级为' + str(min(starLst)))
print('***以上新生代演员出演的电影的平均数目为' + str(round(sum(numLst1) / len(numLst1))) + ',平均星级为' + str(
    round(sum(aveLst1) / len(actorLst1), 2)))
for actor in actorLst2:
    mov = graph.getVertex(actor).movies
    typeLst = searchType(graph, mov)
    starLst = [i[1] for i in list(mov.values())]
    aveStar = star(mov)
    aveLst2.append(aveStar)
    numLst2.append(len(mov))
    print(
        actor + '出演了' + str(len(mov)) + '部电影,主要是' + str(typeLst[0][0]) + '类型的电影,平均星级为' + str(aveStar) + ',最高星级为' + str(
            max(starLst)) + ',最低星级为' + str(min(starLst)))
print('***以上老一辈演员出演的电影的平均数目为' + str(round(sum(numLst2) / len(numLst2))) + ',平均星级为' + str(
    round(sum(aveLst2) / len(actorLst1), 2)))
