class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))
        # (city, stops + 1): cost
        cost = {(src, 0): 0} 
        # (cost, city, stops + 1)
        heap = [(0, src, 0)]

        while heap:
            cur_cost, cur_city, cur_stops = heappop(heap)

            if cur_city == dst:
                return cur_cost

            if cur_stops <= k:
                for next_city, price in graph[cur_city]:
                    alt_cost = cur_cost + price
                    if (next_city, cur_stops + 1) not in cost or alt_cost < cost[(next_city, cur_stops + 1)]:
                        cost[(next_city, cur_stops + 1)] = alt_cost
                        heappush(heap, (alt_cost, next_city, cur_stops + 1))

        return -1