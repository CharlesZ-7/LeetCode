class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        char_count = defaultdict(int)
        max_length = 0

        for right in range(len(s)):
            char = s[right]
            char_count[char] += 1
            max_count = max(max_count, char_count[char])
            
            if (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length