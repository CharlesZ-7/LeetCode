class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for dst, src in prerequisites:
            graph[src].append(dst)
            in_degree[dst] += 1

        topo_order = []
        queue = deque([vertex for vertex in range(numCourses) if in_degree[vertex] == 0])

        while queue:
            cur_vertex = queue.popleft()
            topo_order.append(cur_vertex)
            for next_vertex in graph[cur_vertex]:
                in_degree[next_vertex] -= 1
                if in_degree[next_vertex] == 0:
                    queue.append(next_vertex)

        return topo_order if len(topo_order) == numCourses else []