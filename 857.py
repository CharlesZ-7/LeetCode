class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        max_heap = []
        workers = sorted((w / q, q) for w, q in zip(wage, quality))
        min_cost = float("inf")
        quality_sum = 0

        for ratio, q in workers:
            heappush(max_heap, -q)
            quality_sum += q

            if len(max_heap) > k:
                quality_sum += heappop(max_heap)

            if len(max_heap) == k:
                min_cost = min(min_cost, ratio * quality_sum)

        return min_cost