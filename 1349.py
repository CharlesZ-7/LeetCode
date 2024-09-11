class Graph:
    def __init__(self, vertices: int):
        self.vertex = vertices
        self.graph = defaultdict(list)
        self.capacity = defaultdict(lambda: defaultdict(int))

    def addEdge(self, u: int, v: int, cap: int):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[u][v] = cap
        self.capacity[v][u] = 0

    # Find a new argmenting path
    def bfs(self, source: int, sink: int, parent: List[int]) -> bool:
        visited = [False] * self.vertex
        queue = deque([source])
        visited[source] = True

        while queue:
            node = queue.popleft()
            for next_node in self.graph[node]:
                if visited[next_node] == False and self.capacity[node][next_node] > 0:
                    queue.append(next_node)
                    visited[next_node] = True
                    parent[next_node] = node
                    if next_node == sink:
                        return True
                    
        return False

    # Find the maximum flow
    def Ford_Fulkerson(self, source: int, sink: int) -> int:  
        max_flow = 0
        parent = [-1] * self.vertex

        while self.bfs(source, sink, parent):
            min_cap = float("inf")
            node = sink
            while node != source:
                prev_node = parent[node]
                min_cap = min(min_cap, self.capacity[prev_node][node])
                node = prev_node
            
            max_flow += min_cap
            node = sink
            while node != source:
                prev_node = parent[node]
                self.capacity[prev_node][node] -= min_cap
                self.capacity[node][prev_node] += min_cap
                node = prev_node

        return max_flow

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        source = 0
        sink = m * n + 1
        g = Graph(m * n + 2)
        count = 0

        def getIndex(i: int, j: int) -> int:
            return i * n + j + 1

        for i in range(m):
            for j in range(n):
                idx = getIndex(i, j)
                if seats[i][j] == '.':
                    count += 1
                    if j % 2 == 0:
                        g.addEdge(source, idx, 1)
                        if j > 0:
                            if seats[i][j - 1] == '.':
                                g.addEdge(idx, getIndex(i, j - 1), 1)
                            if i > 0 and seats[i - 1][j - 1] == '.':
                                g.addEdge(idx, getIndex(i - 1, j - 1), 1)
                            if i < m - 1 and seats[i + 1][j - 1] == '.':
                                g.addEdge(idx, getIndex(i + 1, j - 1), 1)
                        if j < n - 1:
                            if seats[i][j + 1] == '.':
                                g.addEdge(idx, getIndex(i, j + 1), 1)
                            if i > 0 and seats[i - 1][j + 1] == '.':
                                g.addEdge(idx, getIndex(i - 1, j + 1), 1)
                            if i < m - 1 and seats[i + 1][j + 1] == '.':
                                g.addEdge(idx, getIndex(i + 1, j + 1), 1)
                    else:
                        g.addEdge(idx, sink, 1)

        max_std = count - g.Ford_Fulkerson(source, sink)
        return max_std