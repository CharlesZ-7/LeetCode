class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def backtrack(row, col_set, major_set, minor_set):
            if row == n:

                return 1

            sol = 0

            for col in range(n):
                major = row - col
                minor = row + col
                is_not_valid = (col in col_set) or (major in major_set) or (minor in minor_set)

                if is_not_valid:
                    continue

                col_set.add(col)
                major_set.add(major)
                minor_set.add(minor)

                sol += backtrack(row + 1, col_set, major_set, minor_set)

                col_set.remove(col)
                major_set.remove(major)
                minor_set.remove(minor)

            return sol

        result = backtrack(0, set(), set(), set())
        return result