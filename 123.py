class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        dp = [[0] * 4 for _ in range(days)]

        dp[0][1] = dp[0][3] = -prices[0]

        for i in range(1, days):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][3] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][0] - prices[i])

        return max(dp[-1][0], dp[-1][2])