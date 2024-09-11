class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        m, n = len(heights), len(heights[0])
        if not m or not n:
            return result
        
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def dfs(r, c, reachable):
            reachable[r][c] = True
            dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in dirc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable)

            return

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)

        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])

        return result