from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = 0
        sorted_prefix_sum = SortedList([0])
        counts = 0

        for num in nums:
            prefix_sum += num
            low_index = sorted_prefix_sum.bisect_left(prefix_sum - upper)
            high_index = sorted_prefix_sum.bisect_right(prefix_sum - lower)
            counts += high_index - low_index
            sorted_prefix_sum.add(prefix_sum)

        return counts