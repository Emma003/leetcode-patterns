class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # return empty string if |pattern| > |str|
        if len(t) > len(s):
            return ""
        
        # loading all chars into a dict
        dict = {}
        for c in t:
            if c not in dict:
              dict[c] = 0
            dict[c] += 1


        window_start, curr_word, min_word, matches, found = 0, "", s, 0, False
        #s.replace('a', '')

        # iterating through chars of string
        for window_end in range(len(s)):
            right = s[window_end]
            curr_word += right
            if right in dict:
              dict[right] -= 1
              if dict[right] == 0:
                matches += 1

            while matches == len(dict):
              # all chars in pattern have been found at least once
              found = True

              # update smallest substring
              if len(curr_word) < len(min_word):
                min_word = curr_word

              # decrement char from dict
              left = s[window_start]
              if left in dict:
                if dict[left] == 0:
                  matches -= 1
                dict[left] += 1

              # slide window forward
              window_start += 1
              curr_word = curr_word[1:]


        if not found:
            return ""
        return min_word
        