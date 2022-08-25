class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2*op1)

            elif char == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2+op1)

            elif char == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2-op1)

            elif char == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2/op1))
            else:
                stack.append(int(char))
        
        return stack[0]