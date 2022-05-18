class Solution:
    def backspaceCompare(self, str1: str, str2: str) -> bool:
        p1 = len(str1) - 1
        p2 = len(str2) - 1
        count1 = count2 = 0
        
        while p1 >= 0 or p2 >= 0:
            while p1 >= 0:
                if str1[p1] == '#' :
                    count1 += 1
                    p1 -= 1
                elif count1>0:
                    count1 -= 1
                    p1 -= 1
                else:
                    break

            while p2 >= 0:
                if str2[p2] == '#' :
                    count2 += 1
                    p2 -= 1
                elif count2>0:
                    count2 -= 1
                    p2 -= 1
                else:
                    break

            # out of bounds
            if (p1 < 0 and p2>= 0) or (p2 < 0 and p1 >=0):
                return False
            if (p1 >= 0 and p2>=0) and str1[p1] != str2[p2]:
                return False
    
            p1 -=1
            p2 -=1

        return True
       
     
        