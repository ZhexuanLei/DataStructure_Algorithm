# 在一个非负整数构成的列表中，对于每一个元素k找出列表中处于k-10000与k之间的元素个数，两端都包括

def func(mylist):
    output = []
    lst = []
    for i in mylist:
        lst.append(i)
        while i - lst[0] > 10000:
            lst.pop(0)
        output.append(len(lst))
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[j] == mylist[i]:
                output[i] += 1

    return output

# mylist = list(input())
# print(func(mylist))
print(func([0,0,0]))
