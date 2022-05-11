class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p_set = {}
        for chr in s1:
            if chr not in p_set:
                p_set[chr] = 0
            p_set[chr] += 1


        l, matches = 0, 0
        for r in range(len(s2)):
            if s2[r] in p_set:
                p_set[s2[r]] -= 1
                if p_set[s2[r]] == 0:
                    matches += 1

            if matches == len(p_set):
                return True

            if r >= len(s1)-1:
                if s2[l] in p_set:
                    if p_set[s2[l]] == 0:
                        matches -= 1 
                    p_set[s2[l]] += 1
                l += 1

        return False
        