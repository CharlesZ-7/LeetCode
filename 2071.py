from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def canAssign(k: int) -> bool:
            tasks_todo = reversed(tasks[:k])
            workers_available = SortedList(workers[-k:])
            pills_available = pills

            for task in tasks_todo:
                place = workers_available.bisect_left(task)

                if place < len(workers_available):
                    workers_available.pop(place)
                elif pills_available > 0:
                    stake = workers_available.bisect_left(task - strength)
                    if stake < len(workers_available):
                        workers_available.pop(stake)
                        pills_available -=1
                    else:
                        return False
                else:
                    return False
            
            return True

        left, right = 0, min(len(tasks), len(workers))
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            if canAssign(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
