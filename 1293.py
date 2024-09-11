class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[[float("inf")] * (k + 1) for _ in range(n)] for _ in range(m)]
        queue = deque([(0,0,0)]) # (x, y, eliminations)
        steps = -1

        while queue:
            steps += 1
            for _ in range(len(queue)):
                cur_x, cur_y, elims = queue.popleft()
                if cur_x == m - 1 and cur_y == n - 1:
                    return steps
                for dx, dy in dirc:
                    next_x, next_y = cur_x + dx, cur_y + dy
                    if 0 <= next_x < m and 0 <= next_y < n:
                        next_elims = elims + grid[next_x][next_y]
                        if next_elims <= k and steps + 1 < visited[next_x][next_y][next_elims]:
                            visited[next_x][next_y][next_elims] = steps + 1
                            queue.append((next_x, next_y, next_elims))

        return -1