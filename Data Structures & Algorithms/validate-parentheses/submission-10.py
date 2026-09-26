class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for c in s:
            if c in hash_map:
                if stack and stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return len(stack) == 0