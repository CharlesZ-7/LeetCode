class Solution:
    def rob_linear(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        money_1 = self.rob_linear(nums[:-1])
        money_2 = self.rob_linear(nums[1:])

        return max(money_1, money_2)