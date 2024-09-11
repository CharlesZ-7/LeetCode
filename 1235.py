class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # 0, 1, ..., n-1
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        def binarySearch(j: int) -> int:
            left, right = 0, j
            while left < right:
                mid = (left + right) // 2
                if jobs[mid][1] <= jobs[j][0]:
                    left = mid + 1
                else:
                    right = mid

            return left
        # 0, 1, 2, ..., n
        dp = [0] * (len(jobs) + 1)
        for j in range(len(jobs)):
            i = binarySearch(j)
            dp[j + 1] = max(dp[j], dp[i] + jobs[j][2])

        return dp[len(jobs)]