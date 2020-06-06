import json


class Vertex:
    def __init__(self, name, movie, type):  # 创建演员代表的节点，包含属性：演员名称；演员的合作者（连接的节点，字典，key为合作者顶点，value为合作电影的列表）；演员出演的电影列表
        self.name = name
        self.collaborators = {}
        self.movies = {movie: type}
        self.searched = False

    def addMovie(self, movie, type):  # 添加演员所出演的电影进入出演电影列表
        self.movies[movie] = type

    def addCollaborator(self, nbr, commom, type):  # 新增合作者
        self.collaborators[nbr] = {commom: type}

    def addCommon(self, nbr, common, type):  # 原有合作者，新增合作电影
        self.collaborators[nbr][common] = type

    def __str__(self):
        return str(self.name) + ' collaborated with ' + str([x.name for x in self.collaborators])

    def getCollaborators(self):
        return self.collaborators.keys()

    def getName(self):
        return self.name

    def getCommon(self, nbr):  # 返回与特定合作者合作的电影列表
        return self.collaborators[nbr]

    def setStatus(self, bo):
        self.searched = bo


class Graph:  # 基于邻接列表的图模型
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, name, movie, type):
        self.numVertices += 1
        newVertex = Vertex(name, movie, type)
        self.vertList[name] = newVertex
        return newVertex

    def getVertex(self, name):
        if name in self.vertList:
            return self.vertList[name]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertList

    def addEdge(self, f, t, movie):
        self.vertList[f].addCollaborator(self.vertList[t], movie)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


with open('Film.json', encoding='utf-8') as fp:
    filmLst = json.load(fp)  # 得到一个列表，其中各元素为一个包含电影信息的字典
    fp.close()


def construct(lst):  # 构建图数据结构
    g = Graph()
    for movieInfo in lst:
        actLst = movieInfo['actor'].split(',')
        title = movieInfo['title']
        type = movieInfo['type']
        for pos in range(len(actLst)):
            actor = actLst[pos]
            if actor not in g:  # 如果是图中没有的新演员则将其作为新的顶点加入
                g.addVertex(actor, title, type)
                # 对于后方的其他演员进行遍历，这样减少了操作次数，如果对每个演员都对其他所有演员遍历的话计算量较大
                for num in range(pos + 1, len(actLst)):
                    addCo(actor, actLst[num], title, type, g)
            else:  # 如果是已经在图中的演员
                g.getVertex(actor).addMovie(title, type)
                for num in range(pos + 1, len(actLst)):
                    addCo(actor, actLst[num], title, type, g)
    return g


def addCo(actor, co, title, type, graph):  # 添加合作者或者已有合作者之间的合作电影
    coVert = graph.getVertex(co) if co in graph else graph.addVertex(co, title, type)
    if coVert not in graph.vertList[actor].getCollaborators():  # 如果是新的合作者，则创建新的连接
        graph.vertList[actor].addCollaborator(coVert, title, type)
        graph.vertList[co].addCollaborator(graph.vertList[actor], title, type)
    else:  # 如果是原有的合作者,则在原合作电影列表中添加此电影
        graph.vertList[actor].addCommon(coVert, title, type)
        graph.vertList[co].addCommon(graph.vertList[actor], title, type)


print('========图的构建========')
graph = construct(filmLst)
print('共有 ' + str(graph.numVertices) + ' 名演员')

print('========连通分支========')


# 以某一个节点为起始进行深度优先搜索，找到其所在的连通分支，返回演员列表与所有合作的电影列表
def dfs(vert):
    nameLst, stack, movieDic = [], [], {}
    stack.append(vert)
    vert.setStatus(True)
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
        if stack[-1] == currentVert:
            stack.pop()
    if len(movieDic) == 0:
        for movie in vert.movies:
            movieDic[movie] = vert.movies[movie]
    return nameLst, movieDic


# 找到一个图中所有的连通分支，并输出连通分支的数目与节点名称列表
def ConnectedComponent(g):
    ccnum = 0
    cclst = []
    for vert in g:
        if not vert.searched:
            namelst, movlst = dfs(vert)
            ccnum += 1
            cclst.append([len(namelst), namelst, movlst])
    return ccnum, cclst  # 返回连通分支的数目以及连通分支的信息列表（分别是演员数目，演员列表，电影列表）


# 根据电影字典（名称：类型）得出其中电影类型出现的频数字典（类型：频数）
def searchType(g, movieDic):
    typeDic = {}
    for movie in movieDic:
        types = movieDic[movie].split(',')
        for ty in types:
            typeDic[ty] = 1 if ty not in typeDic else typeDic[ty] + 1
    return typeDic


ccNum, ccLst = ConnectedComponent(graph)
print(ccNum)  # 连通分支的数目
sortCC = sorted(ccLst, key=lambda x: x[0], reverse=True)  # 根据连通分支大小排序
infoLst = [[i[0]] for i in sortCC[:20]] + [[i[0]] for i in sortCC[-20:]]  # 连通分支中演员数的列表（按照连通分支大小排序，且取前20行与后20行）

seq = 0
for m in sortCC[:20] + sortCC[-20:]:
    typeDic = searchType(graph, m[2])
    typeLst = []
    for movie in typeDic:
        typeLst.append((movie, typeDic[movie]))
    sortLst = sorted(typeLst, key=lambda x: x[1], reverse=True)  # 将电影类型按照出现的频数排序
    types = [i[0] for i in sortLst[:3]]
    infoLst[seq].append(types)  # 表示出连通分支的大小，与其中电影所属类别的前三名（按连通分支大小排序）
    seq += 1
print(infoLst)
