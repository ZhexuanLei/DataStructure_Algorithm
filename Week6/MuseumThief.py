# =========== 1 博物馆大盗问题 ===========
# 给定一个宝物列表treasureList = [{'w': 2,'v': 3}, {'w': 3,'v': 4}, ...]
# 注意：每样宝物只有1个。
# 这样treasureList[0]['w']就是第一件宝物的重量，等等
# 给定包裹最多承重maxWeight > 0
# 实现一个函数，根据以上条件得到最高总价值以及对应的宝物
# 参数：宝物列表treasureList，背包最大承重maxWeight
# 返回值：最大总价值maxValue，选取的宝物列表choosenList(格式同treasureList)

# 这种方法完全套用了课程中的动态规划算法
def dpMuseumThief(treasureList, maxWeight):
    chosenList = []
    Table = {(i, w): 0 for i in range(len(treasureList)) for w in range(maxWeight + 1)}
    for w in range(maxWeight + 1):
        if w >= treasureList[0]['w']:
            Table[(0, w)] = treasureList[0]['v']
    for i in range(1, len(treasureList)):
        for w in range(maxWeight + 1):
            if treasureList[i]['w'] > w:
                Table[(i, w)] = Table[(i - 1, w)]
            else:
                Table[(i, w)] = max(Table[(i - 1, w)], Table[(i - 1, w - treasureList[i]['w'])] + treasureList[i]['v'])
    maxValue = Table[(len(treasureList) - 1, maxWeight)]

    seqnum = len(treasureList)-1
    load = maxWeight
    while seqnum > 0:
        if treasureList[seqnum]['w'] > load:
            pass
        elif Table[(seqnum - 1, load - treasureList[seqnum]['w'])] + treasureList[seqnum]['v'] < Table[(seqnum - 1, load)]:
            pass
        else:
            chosenList.insert(0, treasureList[seqnum])
            load -= treasureList[seqnum]['w']
        seqnum -= 1
    seqnum -= 1
    if load >= treasureList[0]['w']:
        chosenList.insert(0, treasureList[0])
    return maxValue, chosenList


# 检验
print("=========== 1 博物馆大盗问题 ============")
treasureList = [[{'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]]
treasureList.append(
    [{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 4, 'v': 5}, {'w': 4, 'v': 6}, {'w': 4, 'v': 7},
     {'w': 5, 'v': 7},
     {'w': 5, 'v': 8}, {'w': 6, 'v': 8}, {'w': 6, 'v': 10}, {'w': 7, 'v': 10}, {'w': 7, 'v': 12}, {'w': 8, 'v': 12},
     {'w': 8, 'v': 13}, {'w': 9, 'v': 14}, {'w': 9, 'v': 16}])
treasureList.append(
    [{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 4, 'v': 6},
     {'w': 4, 'v': 7},
     {'w': 5, 'v': 7}, {'w': 5, 'v': 8}, {'w': 6, 'v': 8}, {'w': 6, 'v': 10}, {'w': 7, 'v': 11}, {'w': 7, 'v': 12},
     {'w': 8, 'v': 13},
     {'w': 8, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 9, 'v': 17}, {'w': 10, 'v': 17}, {'w': 10, 'v': 18},
     {'w': 11, 'v': 18}])
treasureList.append(
    [{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 4, 'v': 5},
     {'w': 4, 'v': 6},
     {'w': 5, 'v': 6}, {'w': 5, 'v': 7}, {'w': 6, 'v': 8}, {'w': 6, 'v': 9}, {'w': 7, 'v': 10}, {'w': 7, 'v': 11},
     {'w': 8, 'v': 12},
     {'w': 8, 'v': 13}, {'w': 9, 'v': 14}, {'w': 9, 'v': 15}, {'w': 9, 'v': 16}, {'w': 10, 'v': 16}, {'w': 10, 'v': 17},
     {'w': 11, 'v': 18},
     {'w': 12, 'v': 18}, {'w': 12, 'v': 19}, {'w': 13, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 21},
     {'w': 14, 'v': 22}])
treasureList.append(
    [{'w': 1, 'v': 2}, {'w': 2, 'v': 2}, {'w': 2, 'v': 3}, {'w': 3, 'v': 4}, {'w': 3, 'v': 5}, {'w': 4, 'v': 5},
     {'w': 4, 'v': 6},
     {'w': 5, 'v': 6}, {'w': 5, 'v': 7}, {'w': 6, 'v': 8}, {'w': 6, 'v': 9}, {'w': 7, 'v': 9}, {'w': 7, 'v': 10},
     {'w': 8, 'v': 11},
     {'w': 8, 'v': 12}, {'w': 9, 'v': 13}, {'w': 9, 'v': 14}, {'w': 9, 'v': 15}, {'w': 10, 'v': 16}, {'w': 10, 'v': 17},
     {'w': 11, 'v': 18},
     {'w': 11, 'v': 19}, {'w': 12, 'v': 20}, {'w': 13, 'v': 20}, {'w': 13, 'v': 21}, {'w': 14, 'v': 21},
     {'w': 14, 'v': 22},
     {'w': 14, 'v': 23}, {'w': 15, 'v': 24}, {'w': 15, 'v': 25}, {'w': 16, 'v': 26}, {'w': 17, 'v': 27},
     {'w': 18, 'v': 28}])

maxWeightList = [20, 50, 80, 100, 150]
for i in range(len(treasureList)):
    maxValue, choosenList = dpMuseumThief(treasureList[i], maxWeightList[i])
    print(maxValue)
    print(choosenList)
