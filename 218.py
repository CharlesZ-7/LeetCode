class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # event: (x, -height, end/None)
        events = [] # replay buffer
        for left, right, height in buildings:
            events.append((left, -height, right)) # start event
            events.append((right, 0, None)) # end event

        events.sort()

        heap = [(0, float("inf"))] # live show
        result = [[0, 0]]

        for x, negative_height, end in events:
            if negative_height < 0:
                heappush(heap, (negative_height, end))
            else:
                while heap and heap[0][1] <= x:
                    heappop(heap)
            
            cur_height = -heap[0][0]
            if cur_height != result[-1][1]:
                result.append([x, cur_height])

        return result[1:]
