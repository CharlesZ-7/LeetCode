class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, num = queue.popleft()

            if word == endWord:
                return num

            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + char + word[i+1:]

                    if newWord in word_set:
                        word_set.remove(newWord)
                        queue.append((newWord, num + 1))

        return 0