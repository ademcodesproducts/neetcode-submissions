class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        We're reapeatedly appending to a list of strings at the last spot, we got 3 conidtions:
        - .. removes the last appended item so basically a pop()
        - ., ..., string adds onto the stack
        - / is added except at last position, anything longer than / is ignored
        """
        stack = ["/"]

        for s in path.split("/"):
            if s == '..' and len(stack) > 1:
                if stack[-1] == "/":
                    stack.pop()
                stack.pop()
            elif s not in ("", ".", ".."):
                stack.append(s)
                stack.append("/")

        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()

        return "".join(stack)