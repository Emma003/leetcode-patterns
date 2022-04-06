# PROBLEM STATEMENT
# You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets,
# and your goal is to pick as many fruits as possible to be placed in the given baskets.
#
# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:
#
# 1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# 2. You can start with any tree, but you can’t skip a tree once you have started.
# 3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.

import math

def fruits_into_baskets(fruits):
  window_start, max_fruit = 0, -math.inf
  baskets = {}

  # expand sliding window until we reach the max types of fruits (2)
  for window_end in range (len(fruits)):
    # add fruits to baskets (add to basket if missing, otherwise increment)
    if fruits[window_end] not in baskets:
      baskets[fruits[window_end]] = 0
    baskets[fruits[window_end]] += 1

    # shrink the window until there are only two types of fruit left
    while len(baskets) > 2:
      #shrinking window from the left
      if baskets[fruits[window_start]] == 1:
        del baskets[fruits[window_start]]
      else:
        baskets[fruits[window_start]] -= 1
      window_start += 1
    max_fruit = max(max_fruit, window_end - window_start +1)
  return max_fruit