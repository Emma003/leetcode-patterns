# "))"
# "(("


class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {']':'[', '}':'{', ')':'('}
        stack = []
        
        for char in s:
            #closing brackets
            if char in parentheses_map:
                if stack and parentheses_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            #opening brackets
            else:
                stack.append(char)
                
        if stack:
            return False
        return True
                
        
        