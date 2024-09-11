class DisjointSet:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.root[x], self.root[y]
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

class Solution:
    def minimumCost(self, N, connections):
        disjoint_set = DisjointSet(N + 1)
        connections.sort(key=lambda x: x[2])

        total_cost = 0
        edge_used = 0

        for a, b, cost in connections:
            if disjoint_set.union(a, b):
                total_cost += cost
                edge_used += 1
                if edge_used == N - 1:
                    break

        return total_cost if edge_used == N - 1 else -1