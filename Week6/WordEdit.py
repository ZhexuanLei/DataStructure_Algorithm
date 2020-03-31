# ========= 2 单词最小编辑距离问题 =========
# 实现一个函数，给定两个单词，得出从源单词变到目标单词所需要的最小编辑距离，返回总得分与编辑操作过程
# 可以进行的操作有：
# 从源单词复制一个字母到目标单词
# 从源单词删除一个字母
# 在目标单词插入一个字母
# 参数：两个字符串，即源单词original与目标单词target，以及不同操作对应的分值，即一个字典
# 返回值：一个整数与一个列表，最低的分数与操作过程，示例见检验
## 编辑操作过程不一定唯一，给出一种满足条件的操作过程即可
def dpWordEdit(original, target, oplist):
    score = 0
    operations = []
    # 创建一个二维表格，其中元素Table[(i,j)]的含义是将源单词的前i个字符编辑为目标单词的前j个字符所需要的最少分数
    # 这里的i、j为0不代表单词的子串，加入表中是为了方便后面索引i-1、j-1时不报错
    Table = {(i, j): 0 for i in range(len(original)+1) for j in range(len(target)+1)}
    for i in range(1, len(original)+1):
        Table[(i, 0)] = oplist['delete']*i
    for j in range(1, len(target)+1):
        Table[(0, j)] = oplist['insert']*j # 初始化表格
    # 用动态规划的算方法计算所需的最低分数
    for i in range(1, len(original)+1):
        for j in range(1, len(target)+1):
            if original[i-1] == target[j-1]:
                Table[(i, j)] = Table[(i - 1, j - 1)] + oplist['copy']
            else:
                Table[(i, j)] = min(Table[(i - 1, j)] + oplist['delete'], Table[(i,j - 1)] + oplist['insert'])
    score = Table[(len(original), len(target))] # 得到所需的最低分数
    # 下面一部分生成采取的操作
    i, j = len(original), len(target)
    while i > 0 and j > 0:
        if original[i-1] == target[j-1]:
            operations.insert(0, 'copy {0}'.format(original[i-1]))
            i -= 1
            j -= 1
        elif Table[(i - 1, j)] + oplist['delete'] > Table[(i,j - 1)] + oplist['insert']:
            operations.insert(0, 'insert {0}'.format(target[j-1]))
            j -= 1
        else:
            operations.insert(0, 'delete {0}'.format(original[i-1]))
            i -= 1
    if i == 0 and j != 0:
        for k in range(j-1, -1, -1):
            operations.insert(0, 'insert {0}'.format(target[k]))
    elif i != 0 and j == 0:
        for k in range(i-1, -1, -1):
            operations.insert(0, 'delete {0}'.format(original[k]))

    return score, operations


# 检验
print("========= 2 单词最小编辑距离问题 =========")
oplist = {'copy': 5, 'delete': 20, 'insert': 20}
originalWords = ["cane", "sheep", "algorithm", "debug", "difficult", "directory", "wonderful"]
targetWords = ["new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"]
for i in range(len(originalWords)):
    score, operations = dpWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
    print(operations)
