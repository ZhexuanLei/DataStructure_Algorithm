# 不完美的贪心算法解决找零兑换

# 支付1美元购买1美元以下的产品，使找零的硬币个数最少
value = [25, 10, 5, 1]


def GreedyChange(n):
    numlst = []
    for i in value:
        numlst.append(n // i)
        n = n % i
    return '25 cents:{0[0]}; 10 cents:{0[1]}; 5 cents:{0[2]}; 1 cents:{0[3]}; total: {1}' \
        .format(numlst, sum(numlst))


print(GreedyChange(63))


# 然而贪心算法是否能得到最优解与硬币体系和找零数量有很大的关系，例如如果存在21美分面值的硬币，硬币数目最少是3
# 一种无论什么硬币体系都一定能找到最优解的方法是递归解法


def RecursionChange(coinlist, n):
    MinCoin = n  # 初始化一个最大的硬币数目
    if n in coinlist:  # 基本结束条件，问题最小规模
        return 1
    else:
        for i in [j for j in coinlist if j <= n]:
            CoinNum = 1 + RecursionChange(coinlist, n - i)  # 降低问题规模，递归调用
            if CoinNum < MinCoin:
                MinCoin = CoinNum
    return MinCoin

# print(RecursionChange([1,5,10,21,25], 63))

# 这种算法的问题是效率非常低，因为进行了多次的重复计算
# 优化这个递归算法的方法就是防止重复计算，将算过的部分找零结果存在一个容器中，每次递归调用前先查表


def BetterRC(coinlist, n, known):
    MinCoin = n
    if n in coinlist:
        known[n] = 1
        return 1
    elif known[n] != 0: # 在递归调用之前查表，会大幅提升效率，这种保存中间结果的方法在递归算法中非常重要
        return known[n]
    else:
        for i in [j for j in coinlist if j <= n]:
            CoinNum = 1 + BetterRC(coinlist, n - i, known)  # 降低问题规模，递归调用
            if CoinNum < MinCoin:
                MinCoin = CoinNum
                known[n] = MinCoin
    return MinCoin


print(BetterRC([1,5,10,21,25], 63, [0]*64)) #效率大增，结果瞬间返回


# 更有条理的动态规划解法