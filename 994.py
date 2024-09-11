class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        fresh = 0

        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        time = 0
        dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        if fresh == 0:
            return time

        while queue:
            time += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirc:
                    next_x, next_y = x + dx, y + dy
                    is_valid = 0 <= next_x < m and 0 <= next_y < n
                    if is_valid and grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 2
                        fresh -= 1
                        queue.append((next_x, next_y))

        return time - 1 if fresh == 0 else -1