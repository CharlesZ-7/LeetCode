class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        queue = deque()
        indegree = [0] * (n + 1)
        dp = [0] * (n + 1)

        graph = defaultdict(list)
        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            indegree[nextCourse] += 1
        
        for index in range(1, n + 1):
            if indegree[index] == 0:
                dp[index] = time[index - 1]
                queue.append(index)
        
        while queue:
            curCourse = queue.popleft()
            for nextCourse in graph[curCourse]:
                indegree[nextCourse] -= 1
                dp[nextCourse] = max(dp[nextCourse], dp[curCourse] + time[nextCourse - 1])
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)

        return max(dp)
        