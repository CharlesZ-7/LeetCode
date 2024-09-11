class Solution:
    def longestPalindrome(self, s: str) -> str:

        t = "#".join(f"^{s}$")
        length = len(t)
        C = R = 0
        p = [0] * length

        for i in range(1, length - 1):
            mirror = 2 * C - i

            if i < R:
                p[i] = min(R - i, p[mirror])

            while t[i - 1 - p[i]] == t[i + 1 + p[i]]:
                p[i] += 1

            if i + p[i] > R:
                C = i
                R = i + p[i]

        max_len, center = max((n, i) for i, n in enumerate(p))
        start = (center - max_len) // 2
        return s[start: start + max_len]