class DisjointSet:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        
        return self.root[u]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.root[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.root[root_v] = root_u
            else:
                self.root[root_v] = root_u
                self.rank[root_u] += 1

            return True
        
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        disjoint_set = DisjointSet(n + 1)
        
        for a, b in edges:
            if not disjoint_set.union(a, b):
                return [a, b]

        return []