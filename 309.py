class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days == 1:
            return 0
        dp = [0] * 3
        dp[1] = -prices[0]

        for i in range(1, days):
            dp[1] = max(dp[1], dp[2] - prices[i])
            dp[2] = dp[0]
            dp[0] = max(dp[0], dp[1] + prices[i])

        return dp[0]