class Solution:
    def minKnightMoves(self, x, y):
        x, y = abs(x), abs(y)
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        queue = deque([(0, 0, 0)]) # (x, y, step)
        visited = set()
        visited.add((0, 0)) # (x, y)

        while queue:
            cur_x, cur_y, step = queue.pop()
            if cur_x == x and cur_y == y:
                return step
            for dx, dy in moves:
                new_x, new_y = cur_x + dx, cur_y + dy
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, step + 1))

        return -1 