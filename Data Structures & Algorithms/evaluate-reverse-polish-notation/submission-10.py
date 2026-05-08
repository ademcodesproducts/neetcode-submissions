class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):

            if tokens[i] in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
            else:
                stack.append(int(tokens[i]))
            
            if tokens[i] == '+':
                stack.append(a + b)
            elif tokens[i] == '*':
                stack.append(a * b)
            elif tokens[i] == '-':
                stack.append(a - b)
            elif tokens[i] == '/':
                stack.append(int(a / b))

        return stack[0]