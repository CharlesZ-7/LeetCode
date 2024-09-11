class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]

        for current in intervals[1:]:
            if current[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], current[1])
            else:
                merged_intervals.append(current)
        
        return merged_intervals