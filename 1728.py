class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        MOUSE_TURN = 0
        CAT_TURN = 1
        m, n = len(grid), len(grid[0])
        dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'C':
                    cat_start = i * n + j
                elif grid[i][j] == 'M':
                    mouse_start = i * n + j
                elif grid[i][j] == 'F':
                    food = i * n + j

        def canMove(pos, jumps):
            moves = [pos]
            x, y = divmod(pos, n)
            for dx, dy in dirc:
                for jump in range(1, jumps + 1):
                    next_x, next_y = x + jump * dx, y + jump * dy
                    if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] != '#':
                        next_pos = next_x * n + next_y
                        moves.append(next_pos)
                    else:
                        break
            return moves

        mouse_moves = [canMove(i * n + j, mouseJump) for i in range(m) for j in range(n)]
        cat_moves = [canMove(i * n + j, catJump) for i in range(m) for j in range(n)]
       
        @lru_cache(None)
        def dfs(mouse_pos, cat_pos, turns):
            if turns >= 2 * m * n:
                return False
            if cat_pos == mouse_pos or cat_pos == food:
                return False
            if mouse_pos == food:
                return True

            if turns % 2 == MOUSE_TURN:
                return any(dfs(mouse_next_pos, cat_pos, turns + 1) for mouse_next_pos in mouse_moves[mouse_pos])
            else:
                return all(dfs(mouse_pos, cat_next_pos, turns + 1) for cat_next_pos in cat_moves[cat_pos])

        return dfs(mouse_start, cat_start, MOUSE_TURN)