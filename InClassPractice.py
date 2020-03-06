# 数算课程上的一些小练习，在PyLn平台上保存后在canvas上提交代码文件分享链接

#输入一个奇数n，输出一个由#组成的、底边含n个#的、空心的等腰三角形
'''
n = int(input("Please input a odd number:"))
print(" "*int((n-1)/2)+"#")
for i in range(int((n-1)/2)-1):
    print(" "*(int((n-3-2*i)/2))+"#"+" "*(2*i+1)+"#")
if n>1:
    print("#"*n)
'''

#输入一个英文字母组成的字符串，将其中的e替换为3，ee替换为E3，输出替换后的字符串
'''
orilst=list(input("Please input a word:"))
orilst.append(" ")
chalst = []
for i in range(len(orilst)-1):
    if orilst[i] == "e":
        if orilst[i+1] == "e":
            chalst.append("E3")
            orilst[i+1]=" "
        else:
            chalst.append("3")
    else:
        chalst.append(orilst[i])
print("".join(chalst).replace(" ",""))
'''

# 判断list两个添加值得操作的时间复杂度
'''
from timeit import Timer

for i in range(100000,1000001,100000):
    lst = [j for j in range(i)]
    t1 = Timer('lst.insert(0, None)','from __main__ import lst')
    t2 = Timer('lst.append(None)','from __main__ import lst')
    res1, res2 = t1.timeit(number=1000), t2.timeit(number=1000)
    print('%.7f' %res1, '%.7f' %res2)
'''
