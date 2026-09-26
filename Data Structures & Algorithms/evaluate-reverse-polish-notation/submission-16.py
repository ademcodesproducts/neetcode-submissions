class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def is_number(x):
            if x not in "+*-/":
                return True
            else:
                return False

        stack = []

        for t in tokens:
            if is_number(t):
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()

                if t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(a / b))
                elif t == "+":
                    stack.append(a + b)
                else:
                    stack.append(a - b)

        return int(stack[-1]) if stack else 0