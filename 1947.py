from scipy.optimize import linear_sum_assignment
import numpy as np

class Solution:
    def compatibilityScore(self, student: List[int], mentor: List[int]) -> int:
        return sum(std == mnt for std, mnt in zip(student, mentor))
    
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = min(len(students), len(mentors))
        cost = np.zeros((m, m))

        for i in range(m):
            for j in range(m):
                cost[i, j] = - self.compatibilityScore(students[i], mentors[j])

        assigned_row, assigned_col = linear_sum_assignment(cost)
        max_score = int( - sum(cost[assigned_row, assigned_col]))
        return max_score