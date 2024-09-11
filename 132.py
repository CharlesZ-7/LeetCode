class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        dp = [[False] * length for _ in range(length)]

        for i in range(length):
            dp[i][i] = True

        for i in range(length - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])

        for l in range(3, length + 1):
            for i in range(length - l + 1):
                j = i + l - 1
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

        min_cuts = [float("inf")] * length

        for i in range(length):
            if dp[0][i]:
                min_cuts[i] = 0
            else:
                for j in range(i):
                    if dp[j + 1][i]:
                        min_cuts[i] = min(min_cuts[i], min_cuts[j] + 1)

        return min_cuts[-1]