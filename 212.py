class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

    def remove(self, word):

        stack = []
        node = self.root
        for char in word:
            stack.append((node, char))
            node = node.children[char]
        node.word = None

        while stack:
            node, char = stack.pop()
            child = node.children[char]
            if not child.children and child.word is None:
                del node.children[char]
            else:
                break

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        visited = set()
        m, n = len(board), len(board[0])

        trie = Trie()

        for word in words:
            trie.insert(word)

        def dfs(r, c, node):

            is_valid = (0 <= r < m) and (0 <= c < n)
            if not is_valid:
                return

            char = board[r][c]
            if char not in node.children:
                return

            node = node.children[char]

            if node.word:
                visited.add(node.word)
                trie.remove(node.word)

            board[r][c] = "#"
            dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in dirc:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, node)

            board[r][c] = char

            return

        for r in range(m):
            for c in range(n):
                dfs(r, c, trie.root)

        return list(visited)
