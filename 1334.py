class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for from_city, to_city, weight in edges:
            dist[from_city][to_city] = dist[to_city][from_city] = weight

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        target_city = -1
        min_count = n

        for i in range(n):
            cur_count = sum((1 if dist[i][j] <= distanceThreshold else 0) for j in range(n))
            if min_count > cur_count or (min_count == cur_count and i > target_city):
                min_count = cur_count
                target_city = i

        return target_city