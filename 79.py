class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r: int, c: int, index: int) -> bool:

            if index == len(word):
                return True

            is_valid = (0 <= r < m) and (0 <= c < n)
            if (not is_valid) or board[r][c] != word[index]:
                return False

            dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            found = False
            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in dirc:
                nr, nc = r + dr, c + dc
                found |= dfs(nr, nc, index + 1)

            board[r][c] = temp

            return found

        m, n = len(board), len(board[0])

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False
