class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # Path Compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ds = DisjointSet(n)
        result = []

        for u, v in requests:
            rootU = ds.find(u)
            rootV = ds.find(v)
            can_be_friends = True

            for x, y in restrictions:
                rootX = ds.find(x)
                rootY = ds.find(y)

                if (rootU == rootX and rootV == rootY) or (rootU == rootY and rootV == rootX):
                    can_be_friends = False
                    break
            
            result.append(can_be_friends)
            if can_be_friends:
                ds.union(rootU, rootV)
            
        return result