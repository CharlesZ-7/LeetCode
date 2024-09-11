class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_num = float("-inf")

        for row in range(len(nums)):
            heappush(heap, (nums[row][0], row, 0))
            max_num = max(max_num, nums[row][0])

        smallest_range = [heap[0][0], max_num]

        while heap:
            min_num, row, col = heappop(heap)
            if max_num - min_num < smallest_range[1] - smallest_range[0]:
                smallest_range = [min_num, max_num]

            if col + 1 == len(nums[row]):
                break

            next_num = nums[row][col + 1]
            max_num = max(max_num, next_num)
            heappush(heap, (next_num, row, col + 1))

        return smallest_range