class Solution:
    def minWindow(self, s: str, t: str) -> str:

        memo = Counter(t)
        missing = len(t)

        start = end = 0
        left = 0
        for right, char in enumerate(s, 1):
            if memo[char] > 0:
                missing -= 1
            memo[char] -= 1

            if missing == 0:
                while memo[s[left]] < 0:
                    memo[s[left]] += 1
                    left += 1
                if end == 0 or right - left < end - start:
                    start, end = left, right

        return s[start: end]