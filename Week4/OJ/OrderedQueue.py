# 通过有序队列实现字符串的重组，得到最小的字符串

def func(S):
    output = S
    Prev = S
    for i in range(len(S)):
        Prev = Prev[1:] + Prev[0]
        if Prev < output:
            output = Prev
        else:
            pass
    return output


S = input()
print(func(S))
