class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def ManhattanDistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        if n == 0:
            return 0

        heap = [(0, 0)] # (cost, index)
        vertex_visited = [False] * n
        edge_counts = 0
        min_cost = 0

        while edge_counts < n:
            cur_cost, cur_vertex = heappop(heap)

            if vertex_visited[cur_vertex]:
                continue
            
            vertex_visited[cur_vertex] = True
            edge_counts += 1
            min_cost += cur_cost

            for neighbor_vertex in range(n):
                if not vertex_visited[neighbor_vertex]:
                    heappush(heap, (ManhattanDistance(points[cur_vertex], points[neighbor_vertex]), neighbor_vertex))

        return min_cost