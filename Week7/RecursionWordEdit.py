# ========= 2 单词最小编辑距离问题 =========
# 实现一个函数，给定两个单词，得出从源单词变到目标单词所需要的最小编辑距离，返回总得分与编辑操作过程
# 可以进行的操作有：
# 从源单词复制一个字母到目标单词
# 从源单词删除一个字母
# 在目标单词插入一个字母
# 参数：两个字符串，即源单词original与目标单词target，以及不同操作对应的分值，即一个字典
# 返回值：一个整数与一个列表，最低的分数与操作过程，示例见检验
## 编辑操作过程不一定唯一，给出一种满足条件的操作过程即可
def RCWordEdit(original, target, oplist):
    score = 0
    operations = []
    if len(original) == 0: # 基本结束条件
        return len(target) * oplist['insert'], ['insert {0}'.format(i) for i in target]
    elif len(target) == 0: # 基本结束条件
        return len(original) * oplist['delete'], ['delete {0}'.format(i) for i in original]
    else:
        if original[-1] == target[-1]:
            s = oplist['copy']
        else:
            s = oplist['delete'] + oplist['insert']
        # 递归部分
        op1,op2,op3 = RCWordEdit(original[:-1], target[:-1], oplist), RCWordEdit(original, target[:-1], oplist),\
                      RCWordEdit(original[:-1], target, oplist)
        addscore, addop = op1[0]+s, op1[1]
        addop.append('copy {0}'.format(original[-1]))
        # 判断最小值，写的这么复杂只是因为想要把操作也同时记录下来，我不知道有什么其他的方法，而且我觉得回溯的比较麻烦
        if op2[0] + oplist['insert'] <= addscore:
            addscore = op2[0] + oplist['insert']
            addop = op2[1]
            addop.append('insert {0}'.format(target[-1]))
        if op3[0] + oplist['delete'] <= addscore:
            addscore = op3[0] + oplist['delete']
            addop = op3[1]
            addop.append('delete {0}'.format(original[-1]))
        score += addscore
        operations.extend(addop)
    return score, operations


# 检验
print("========= 2 单词最小编辑距离问题 =========")
oplist = {'copy': 5, 'delete': 20, 'insert': 20}
originalWords = ["cane", "sheep", "algorithm", "debug", "difficult", "directory", "wonderful"]
targetWords = ["new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"]
for i in range(len(originalWords)):
    score, operations = RCWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
    print(operations)

