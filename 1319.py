class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        adj_list = defaultdict(list)
        for a, b in connections:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node: int, visited: Set[int]):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
            return

        components = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                components += 1
        
        return components - 1