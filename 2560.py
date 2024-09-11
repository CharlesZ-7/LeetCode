class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def canRob(capability: int) -> bool:

            l = len(nums)
            dp = [0] * l

            for i in range(l):
                if nums[i] > capability:
                    rob = 0
                else:
                    rob = (dp[i - 2] if i >= 2 else 0) + 1
                dp[i] = max(dp[i - 1], rob)

            return (dp[-1] >= k)

        
        left, right = min(nums), max(nums)
        best = right

        while left <= right:
            mid = (left + right) // 2
            if canRob(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1

        return best