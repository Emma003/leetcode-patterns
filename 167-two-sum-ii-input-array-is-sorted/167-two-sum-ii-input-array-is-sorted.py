class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r, sum = 0, len(numbers)-1, 0

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1,r+1]
            elif sum > target:
                r -= 1 
            else :
                l += 1