class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # declaring some variables
        baskets = {}
        window_start, max_fruits = 0, -math.inf

        # going through the row of trees
        for window_end in range(len(fruits)):
          right_fruit = fruits[window_end]

          # adding the new fruit to the baskets if not already there
          if right_fruit not in baskets:
            baskets[right_fruit] = 0
          baskets[right_fruit] += 1

          # shrink basket until it fulfills condition (only two fruit types)
          while len(baskets) > 2:
            left_fruit = fruits[window_start]

            # remove the fruit from the basket
            baskets[left_fruit] -= 1
            if baskets[left_fruit] == 0:
              baskets.pop(left_fruit)

            # move window forward
            window_start += 1

          # update max number of fruits
          max_fruits = max(max_fruits, window_end + 1 - window_start)

        return max_fruits
