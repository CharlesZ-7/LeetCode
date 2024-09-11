class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for string in strs:
            reps = ''.join(sorted(string))
            if reps not in anagram:
                anagram[reps] = []
            anagram[reps].append(string)

        return list(anagram.values())