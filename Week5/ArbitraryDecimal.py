# 给定一个M进制的数，请将其转换为N进制并输出
# 输入格式:
# 两行，第一行为空格分隔的两个数字，分别为10进制表示的M与N；其中M, N均满足2 ≤ M、N ≤ 36
# 第二行为待转换的数字，其中每位超过9的部分从10至36分别用大写字母A-Z表示；输入数据保证其中最大位数对应数字不超过M
# 输出格式：
# 一行字符串，表示转换后的N进制数

# 先尝试一下把待转换的数转化成十进制，然后再用原来的算法转化成需要的进制

def Trans(num, d):
    char = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if num < d:
        return char[num]
    else:
        return Trans(num // d, d) + char[num % d]


def toDec(num, d):
    dnum = 0
    for i in range(len(num)):
        dnum += int(num[i]) * d ** (len(num)-1-i)
    return dnum


lst = input().split(' ')
num = input()
d1, d2 = int(lst[0]), int(lst[1])
print(Trans(toDec(num,d1), d2))
