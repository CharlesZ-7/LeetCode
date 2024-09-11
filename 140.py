class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        wordSet = set(wordDict)

        def backtrack(start: int) -> List[str]:
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start: end]
                if word in wordSet:
                    remaining_sentences = backtrack(end)
                    for sentence in remaining_sentences:
                        new_sentence = word + ("" if sentence == "" else " " + sentence)
                        sentences.append(new_sentence)

            memo[start] = sentences

            return sentences

        return backtrack(0)
