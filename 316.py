class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()

        count = {char: 0 for char in s}
        for char in s:
            count[char] += 1

        for char in s:
            count[char] -= 1
            if char in visited:
                continue

            while stack and char < stack[-1] and count[stack[-1]] > 0:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return "".join(stack)
            

