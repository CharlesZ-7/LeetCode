class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


class Solution:
    def Kruskal(self, n: int, indexed_edges: List[List[int]], join_index: int = -1, split_index: int = -1) -> int:
        disjoint_set = DisjointSet(n)
        cost = 0
        edge_counts = 0

        if join_index != -1:
            _, src, dst, weight = indexed_edges[join_index]
            disjoint_set.union(src, dst)
            cost += weight
            edge_counts += 1

        for index, (_, src, dst, weight) in enumerate(indexed_edges):
            if index == split_index:
                continue
            
            if disjoint_set.find(src) != disjoint_set.find(dst):
                disjoint_set.union(src, dst)
                cost += weight
                edge_counts += 1

        if edge_counts == n - 1:
            return cost

        return float("inf")

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indexed_edges = [(edge, src, dst, weight) for edge, (src, dst, weight) in enumerate(edges)]
        indexed_edges.sort(key=lambda x: x[-1])
        min_cost = self.Kruskal(n, indexed_edges)
        critical_edges, pseudo_critical_edges = [], []

        for index, (edge, _, _, _) in enumerate(indexed_edges):
            if self.Kruskal(n, indexed_edges, -1, index) > min_cost:
                critical_edges.append(edge)
            elif self.Kruskal(n, indexed_edges, index, -1) == min_cost:
                pseudo_critical_edges.append(edge)

        return [critical_edges, pseudo_critical_edges]