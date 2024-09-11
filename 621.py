class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        heapify(heap)
        temp = []
        time = 0

        freq = Counter(tasks).values()

        for count in freq:
            heappush(heap, -count)

        while heap:
            for _ in range(n + 1):
                if heap or temp:
                    time += 1
                if heap:
                    count = -heappop(heap)
                    if count > 1:
                        temp.append(count - 1)
            while temp:
                heappush(heap, -temp.pop())

        return time
