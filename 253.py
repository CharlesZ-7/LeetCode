class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        heap = []
        max_heap = 0
        
        for interval in intervals:
            while heap and interval[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            max_heap = max(max_heap, len(heap))

        return max_heap