class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def computePrefix(s: str) -> str:
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

        rev_s = s[::-1]
        new_s = s + '#' + rev_s
        prefix = computePrefix(new_s)
        max_prefix = prefix[-1]
        to_add = rev_s[: len(s) - max_prefix]
        min_palindrome = to_add + s

        return min_palindrome