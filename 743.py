class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for src, dst, weight in times:
            graph[src].append((dst, weight))
        dist = {node: float("inf") for node in range(1, n + 1)}
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            curr_dist, curr_node = heappop(heap)
            for next_node, weight in graph[curr_node]:
                alt_dist = curr_dist + weight
                if alt_dist < dist[next_node]:
                    dist[next_node] = alt_dist
                    heappush(heap, (alt_dist, next_node))

        max_dist = max(dist.values())
        return max_dist if max_dist != float("inf") else -1