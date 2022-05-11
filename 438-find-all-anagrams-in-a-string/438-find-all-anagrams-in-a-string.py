class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result_indexes = []

        # loading all chars in pattern into a dict
        dict = {}
        for c in p:
            if c not in dict:
              dict[c] = 0
            dict[c] += 1


        window_start, matches = 0, 0
        # iterating through chars of the string
        for window_end in range(len(s)):
            right = s[window_end]

            # decrement char from dict if found in string, increment matches if all instances of that char are found
            if right in dict:
                dict[right] -= 1
                if dict[right] == 0:
                    matches += 1

            # record start index of perm. window 
            if matches == len(dict):
              result_indexes.append(window_start)

            # slide window forward
            if window_end >= len(p) - 1:
              left = s[window_start]
              if left in dict:
                if dict[left] == 0:
                  matches -= 1
                dict[left] += 1

              window_start += 1

        return result_indexes
        