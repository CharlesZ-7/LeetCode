class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]
        trapped_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped_water += right_max - height[right]

        return trapped_water


class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        stack = []

        for index in range(len(height)):
            while stack and height[index] > height[stack[-1]]:
                base = height[stack.pop()]
                if stack:
                    top = min(height[index], height[stack[-1]])
                    relative_height = top - base
                    width = index - stack[-1] - 1
                    trapped_water += relative_height * width
            stack.append(index)

        return trapped_water