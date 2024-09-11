class Solution:
    def dfs(self, src: str):
        while self.graph[src]:
            dst = heappop(self.graph[src])
            self.dfs(dst)
        self.itinerary.append(src)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = defaultdict(list)
        self.itinerary = []

        for src, dst in tickets:
            heappush(self.graph[src], dst)
        
        self.dfs("JFK")
        return self.itinerary[::-1]