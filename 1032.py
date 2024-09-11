class TrieNode:

    def __init__(self):
        self.children = {}
        self.failure = None
        self.output = []

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.cur_node = self.root

        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.output.append(word)

        queue = deque()

        for node in self.root.children.values():
            node.failure = self.root
            queue.append(node)

        while queue:
            node = queue.popleft()

            for char, next_node in node.children.items():
                failure_node = node.failure
                while failure_node is not None and char not in failure_node.children:
                    failure_node = failure_node.failure
                if failure_node is None:
                    next_node.failure = self.root
                else:
                    next_node.failure = failure_node.children[char]

                next_node.output.extend(next_node.failure.output)
                queue.append(next_node)

    def query(self, letter: str) -> bool:

        while self.cur_node is not None and letter not in self.cur_node.children:
            self.cur_node = self.cur_node.failure
        if self.cur_node is None:
            self.cur_node = self.root
        else:
            self.cur_node = self.cur_node.children[letter]

        return bool(self.cur_node.output)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)