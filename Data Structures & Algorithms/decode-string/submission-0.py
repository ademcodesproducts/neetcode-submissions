class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        k = ""

        for c in s:
            if c.isdigit():
                k += c

            elif c.isalpha():
                curr_string += c

            if c == '[':
                stack.append((curr_string, int(k)))
                curr_string, k = "", ""
            
            elif c == ']':
                if stack:
                    prev_string, multi = stack.pop()
                    curr_string *= multi
                    curr_string = prev_string + curr_string

        return curr_string