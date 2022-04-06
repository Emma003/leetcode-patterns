# PROBLEM STATEMENT
# Given a string, find the length of the longest substring, which has all distinct characters.

def non_repeat_substring(str):
  window_start, max_window = 0,0
  set = {}
  # extend the range
  for window_end in range (len(str)):
    right_char = str[window_end]
    # shrinking the window until there are no existing duplicates of right_char
    while right_char in set:
      max_window = max(max_window, window_end - window_start)
      del set[str[window_start]]
      window_start += 1
    # add unique char to set
    set[right_char] = 1
  return max_window

def main():
    print(non_repeat_substring("abcchbebcde"))
main()