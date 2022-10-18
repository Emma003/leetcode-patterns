class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        chars = {}
        
        for c in s:
            if c not in chars:
                chars[c] = 0
            chars[c] += 1
            
        unique = set()
        for n in chars.values():
            if n not in unique:
                unique.add(n)
            
            if len(unique) > 1:
                return False
            
        return True
            