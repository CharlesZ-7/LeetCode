class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end_time = intervals[0][1]
        remove_counter = 0

        for current in intervals[1:]:
            if current[0] < last_end_time:
                remove_counter += 1
            else:
                last_end_time = current[1]

        return remove_counter