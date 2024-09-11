class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for src, dst in redEdges:
            red_graph[src].append(dst)
        for src, dst in blueEdges:
            blue_graph[src].append(dst)

        # (node, color, step)
        queue = deque([(0, 'R', 0), (0, 'B', 0)])
        # (node, color)
        visited = {(0, 'R'), (0, 'B')}
        answer = [-1] * n

        while queue:
            node, color, step = queue.popleft()

            if answer[node] == -1:
                answer[node] = step
            
            if color == 'R':
                next_color = 'B'
                next_graph = blue_graph
            else:
                next_color = 'R'
                next_graph = red_graph
            
            for next_node in next_graph[node]:
                if (next_node, next_color) not in visited:
                    visited.add((next_node, next_color))
                    queue.append((next_node, next_color, step + 1))

        return answer