class QuickFind:
    def __init__(self, size: int):
        self.root = [ind for ind in range(size)]

    def union(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            for ind, parent in enumerate(self.root):
                if parent == root_b:
                    self.root[ind] = root_a

    def find(self, a: int):
        return self.root[a]
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class QuickUnion:
    def __init__(self, size: int):
        self.root = [ind for ind in range(size)]

    def union(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.root[root_b] = root_a

    def find(self, a: int):
        while a != self.root[a]:
            a =  self.root[a]
        return a
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class UnionByRank:
    def __init__(self, size: int):
        self.root = [ind for ind in range(size)]
        self.rank = [1 for ind in range(size)]

    def union(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.root[root_b] = root_a
            elif self.rank[root_b] > self.rank[root_a]:
                self.root[root_a] = root_b
            else:
                self.root[root_b] = root_a
                self.rank[root_a] += 1

    def find(self, a: int):
        while a != self.root[a]:
            a =  self.root[a]
        return a
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)


class QuickUnionPathCompression:
    def __init__(self, size: int):
        self.root = [ind for ind in range(size)]

    def union(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.root[root_b] = root_a

    def find(self, a: int):
        stack = []
        while a != self.root[a]:
            stack.append(a)
            a =  self.root[a]
        while stack:
            node = stack.pop()
            self.root[node] = a
        return a
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)



    

# Test Case
uf = QuickFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
print(uf.root)


# Test Case
uf = QuickUnion(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
print(uf.root)


# Test Case
uf = UnionByRank(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
print(uf.root)



# Test Case
uf = QuickUnionPathCompression(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
print(uf.root)
