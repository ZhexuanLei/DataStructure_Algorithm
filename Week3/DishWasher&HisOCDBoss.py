class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def DishJudge(seq):
    s = Stack()
    for i in range(seq[0]):
        s.push(i)
    for i in range(1, 10):
        if seq[i] > seq[i - 1]:
            for j in range(seq[i - 1] + 1, seq[i]):
                s.push(j)
        elif seq[i] == s.peek():
            s.pop()
        else:
            return 'No'
    return 'Yes'


inputseq = list(map(int, input()))
print(DishJudge(inputseq))
