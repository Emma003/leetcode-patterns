class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        start, max_fruits = 0, -1

        for end in range(len(fruits)):
            r = fruits[end]
            if r not in baskets:
                baskets[r] = 0
            baskets[r] += 1

            while len(baskets) > 2:
                l = fruits[start]
                baskets[l] -= 1
                if baskets[l] == 0:
                    del baskets[l]
                start +=1

            max_fruits = max(max_fruits, end-start+1)
        return max_fruits

