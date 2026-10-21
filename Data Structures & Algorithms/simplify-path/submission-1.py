class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        We're reapeatedly appending to a list of strings at the last spot, we got 3 conidtions:
        - .. removes the last appended item so basically a pop()
        - ., ..., string adds onto the stack
        - / is added except at last position, anything longer than / is ignored
        """
        split = path.split("/")
        pathString = "/"

        for s in split:
            if s == '..':
                slash_count = 0
                for i in range(len(pathString) - 1, -1, -1):
                    if pathString[i] == "/":
                        slash_count += 1
                    else:
                        pathString = pathString[:i]
                    if slash_count >= 2:
                        break
            elif s == ".":
                continue
            else:
                if s != "":
                    pathString = pathString + s + "/"

        if len(pathString) > 1:
            pathString = pathString[:len(pathString) - 1]

        return pathString