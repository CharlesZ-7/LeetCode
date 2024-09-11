class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        n = len(gas)
        start = 0
        fuel = 0

        for i in range(n):
            fuel += gas[i] - cost[i]

            if fuel < 0:
                start = i + 1
                fuel = 0

        return start