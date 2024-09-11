class FenwickTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index

        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []

        sorted_nums = sorted(set(nums))
        ranks = {num: rank for rank, num in enumerate(sorted_nums, 1)}
        tree = FenwickTree(len(ranks))

        for num in reversed(nums):
            rank = ranks[num]
            counts.append(tree.query(rank - 1))
            tree.update(rank, 1)

        return counts[::-1]
        