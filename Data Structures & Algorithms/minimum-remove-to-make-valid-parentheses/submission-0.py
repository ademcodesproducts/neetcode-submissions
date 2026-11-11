class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opener, closer = [], []
        for i, x in enumerate(s):
            if x == "(":
                opener.append(i)
            else:
                if opener and x == ")":
                    opener.pop()
                elif x == ")":
                    closer.append(i)

        remove = set(closer) | set(opener)
        output = ""
        for i, x in enumerate(s):
            if i not in remove:
                output += x
        return output