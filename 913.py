class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        MOUSE_WIN = MOUSE_TURN = 1
        CAT_WIN = CAT_TURN = 2
        DRAW = HOLE = 0
        dp = [[[DRAW] * 3 for _ in range(n)] for _ in range(n)]
        queue = deque()

        for i in range(1, n):
            for turn in range(1, 3):
                dp[0][i][turn] = MOUSE_WIN
                queue.append((0, i, turn, MOUSE_WIN))
                dp[i][i][turn] = CAT_WIN
                queue.append((i, i, turn, CAT_WIN))

        while queue:
            mouse, cat, turn, state = queue.popleft()

            if turn == MOUSE_TURN:
                for prev_mouse in graph[mouse]:
                    if dp[prev_mouse][cat][CAT_TURN] == DRAW:
                        if state == MOUSE_WIN:
                            dp[prev_mouse][cat][CAT_TURN] = MOUSE_WIN
                            queue.append((prev_mouse, cat, CAT_TURN, MOUSE_WIN))
                        elif all(dp[possible_mouse][cat][MOUSE_TURN] == CAT_WIN for possible_mouse in graph[prev_mouse]):
                            dp[prev_mouse][cat][CAT_TURN] = CAT_WIN
                            queue.append((prev_mouse, cat, CAT_TURN, CAT_WIN))

            else:
                for prev_cat in graph[cat]:
                    if prev_cat == HOLE:
                        continue
                    if dp[mouse][prev_cat][MOUSE_TURN] == DRAW:
                        if state == CAT_WIN:
                            dp[mouse][prev_cat][MOUSE_TURN] = CAT_WIN
                            queue.append((mouse, prev_cat, MOUSE_TURN, CAT_WIN))
                        elif all(dp[mouse][possible_cat][CAT_TURN] == MOUSE_WIN for possible_cat in graph[prev_cat] if possible_cat != HOLE):
                            dp[mouse][prev_cat][MOUSE_TURN] = MOUSE_WIN
                            queue.append((mouse, prev_cat, MOUSE_TURN, MOUSE_WIN))

        return dp[1][2][CAT_TURN]