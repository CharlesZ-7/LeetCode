class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        p_len = len(p)
        s_len = len(s)

        if p_len > s_len:
            return result

        p_count = Counter(p)
        s_count = Counter(s[:p_len])

        if p_count == s_count:
            result.append(0)

        for i in range(1, s_len - p_len + 1):
            s_count[s[i - 1]] -= 1
            if s_count[s[i - 1]] == 0:
                del s_count[s[i - 1]]
            
            s_count[s[i + p_len - 1]] += 1

            if p_count == s_count:
                result.append(i)

        return result