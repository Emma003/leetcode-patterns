class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict = {}
        for letter in s1:
            if letter not in dict:
                dict[letter] = 0
            dict[letter] += 1


        matches, left = 0, 0
        for right in range(len(s2)):
            if s2[right] in dict:
                dict[s2[right]] -= 1
                if dict[s2[right]] == 0:
                    matches += 1

            if matches == len(dict):
                return True

            if right >= len(s1) - 1:
                if s2[left] in dict:
                    if dict[s2[left]] == 0:
                        matches -= 1
                    dict[s2[left]] += 1

                left += 1

        return False
        