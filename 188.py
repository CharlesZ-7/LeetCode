class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0] * (2 * k + 1)
        for j in range(1, k + 1):
            dp[2 * j - 1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k, 0, -1):
                dp[2 * j] = max(dp[2 * j], dp[2 * j - 1] + prices[i])
                dp[2 * j - 1] = max(dp[2 * j - 1], dp[2 * j - 2] - prices[i])

        return dp[2 * k]