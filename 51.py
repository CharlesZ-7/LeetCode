class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def backtrack(row, col_set, major_set, minor_set, state):
            if row == n:
                board = ["".join(state[row]) for row in range(n)]
                result.append(board)
                return

            for col in range(n):
                major = row - col
                minor = row + col
                is_not_valid = (col in col_set) or (major in major_set) or (minor in minor_set)

                if is_not_valid:
                    continue

                state[row][col] = "Q"
                col_set.add(col)
                major_set.add(major)
                minor_set.add(minor)

                backtrack(row + 1, col_set, major_set, minor_set, state)

                state[row][col] = "."
                col_set.remove(col)
                major_set.remove(major)
                minor_set.remove(minor)

        empty = [["."] * n for _ in range(n)]
        result = []

        backtrack(0, set(), set(), set(), empty)
        return result