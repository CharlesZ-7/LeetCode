class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def computePrefix(s):
            n = len(s)
            prefix = [0] * n
            j = 0

            for i in range(1, n):
                while j > 0 and s[i] != s[j]:
                    j = prefix[j - 1]
                if s[i] == s[j]:
                    j += 1
                prefix[i] = j

            return prefix

        m = len(haystack)
        n = len(needle)
        j = 0

        prefix = computePrefix(needle)

        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = prefix[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i - n + 1

        return -1