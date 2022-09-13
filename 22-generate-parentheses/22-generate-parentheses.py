class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parentheses if open < n
        # only add closing par if closed < open
        # valid if open == closed == n
        
        stack = []
        res = []
        
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                
                #backtrack
                stack.pop()
                
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                
                #backtrack
                stack.pop()
                
        backtrack(0,0)
        return res