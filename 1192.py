class Solution:
    def StrongConnectedComponents(self, vertex: int, prev_vertex: int, graph: List[List[int]]):
        self.visited_time[vertex] = self.low_link[vertex] = self.time
        self.time += 1

        for next_vertex in graph[vertex]:
            if self.visited_time[next_vertex] == -1:
                self.StrongConnectedComponents(next_vertex, vertex, graph)
                self.low_link[vertex] = min(self.low_link[vertex], self.low_link[next_vertex])
                if self.low_link[next_vertex] > self.visited_time[vertex]:
                    self.critical_edges.append([vertex, next_vertex])
            elif next_vertex != prev_vertex:
                self.low_link[vertex] = min(self.low_link[vertex], self.visited_time[next_vertex])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.critical_edges = []
        self.time = 0
        self.visited_time = [-1] * n
        self.low_link = [-1] * n

        graph = defaultdict(list)
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)

        for vertex in range(n):
            if self.visited_time[vertex] == -1:
                self.StrongConnectedComponents(vertex, -1, graph)

        return self.critical_edges
