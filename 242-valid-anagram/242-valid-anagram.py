class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         set = {}
#         for c in s: 
#             if c not in set:
#                 set[c] = 0
#             set[c] += 1
        
#         matches = 0
        
#         for r in range(len(t)):
#             if t[r] in set:
#                 set[t[r]] -= 1
#                 if set[t[r]] == 0:
#                     matches += 1
                    
#             if matches == len(set):
#                 return True
            
#         return False
            
        
        # if they are not the same length
        if len(s) != len(t):
            return False
        
        # if they are the same length
        # count the number of each letter in s using a dictionary
        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 0
            letters[letter] += 1
        
        
        # go through t and make sure it matches the number of letters in s
        for i in range(len(t)):
            if t[i] not in letters:
                return False
            else:
                letters[t[i]] -= 1
        
        for count in letters.values():
            if count != 0:
                return False
        
        return True
    
    #time complexity: 
        # putting every letter of s in dictionary:      O(n)
        # going through t:                              O(n)
        # making sure the values are all 0:             O(n)
        #                                               = O(3n) = O(n)
            
    #space complexity:
        # putting every letter of s in dictionary:      O(n)
                                