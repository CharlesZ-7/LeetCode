class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        gardens = defaultdict(list)
        for x, y in paths:
            gardens[x].append(y)
            gardens[y].append(x)

        plants = [0] * n

        for i in range(1, n + 1):
            neighbor_plants = {plants[neighbor - 1] for neighbor in gardens[i] if plants[neighbor - 1] != 0}
            for flower in range(1, 5):
                if flower not in neighbor_plants:
                    plants[i - 1] = flower
                    break

        return plants 
