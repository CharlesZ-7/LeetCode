class Solution:
    def alienOrder(self, words):
        adjacency = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            word, next_word = words[i], words[i + 1]
            min_len = min(len(word), len(next_word))

            if len(word) > len(next_word) and word[:min_len] == next_word[:min_len]:
                return ""

            for j in range(min_len):
                if word[j] != next_word[j]:
                    if next_word[j] not in adjacency[word[j]]:
                        adjacency[word[j]].add(next_word[j])
                        in_degree[next_word[j]] += 1
                    break


        zero_in_degree = deque([char for char in in_degree if in_degree[char] == 0])
        alphabet = []

        while zero_in_degree:
            cur_char = zero_in_degree.popleft()
            alphabet.append(cur_char)
            for next_char in adjacency[cur_char]:
                in_degree[next_char] -= 1
                if in_degree[next_char] == 0:
                    zero_in_degree.append(next_char)


        if len(alphabet) == len(in_degree):
            return "".join(alphabet)
        
        return ""