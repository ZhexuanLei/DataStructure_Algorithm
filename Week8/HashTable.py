class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        return key % self.size  # 简单的求余散列函数

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size  # 线性探测解决冲突问题

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == None: # 如果槽位空闲，将数据填入
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] == key: # 如果槽位被占据且关键码重复，则替换数据
            self.data[hashvalue] = data
        else: # 如果槽位被占据且关键码不重复，则需要进行向后的探测解决冲突
            nextslot = self.rehash(hashvalue)
            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot)
            if self.slots[nextslot] == key:
                self.data[nextslot] = data
            else:
                self.slots[nextslot] = key
                self.data[nextslot] = data

    def get(self, key):
        startslot = self.hashfunction(key)
        data, stop, found, position = None, False, False, startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return data

# 散列表在最好的情况下可以达到O(1)级别的查找性能；而当负载因子较大时，冲突可能较多，性能有所下降（rehash次数通常需要更多）
