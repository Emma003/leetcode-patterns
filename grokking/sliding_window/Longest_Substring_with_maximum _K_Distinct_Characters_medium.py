# PROBLEM STATEMENT
# Given a string, find the length of the longest substring in it with no more than K distinct characters.

import math
def longest_substring_with_k_distinct(str1, k):
  set = {}
  window_start, max_window = 0, -math.inf

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    last_char = str1[window_end]
    if str1[window_end] in set:
      set[str1[window_end]] += 1
    else:
      set[str1[window_end]] = 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(set) > k:
      # remember the maximum length so far
      max_window = max(max_window, window_end - window_start)
      if set[str1[window_start]] == 1:
        del set[str1[window_start]]
      else:
        set[str1[window_start]] -= 1
      window_start += 1 # shrink the window
  if max_window == -math.inf:
    return len(str1)
  return max_window