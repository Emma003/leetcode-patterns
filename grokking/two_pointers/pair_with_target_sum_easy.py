# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.


def pair_with_target_sum(arr, target_sum):
    left, right, sum = 0, len(arr) - 1, 0
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target_sum:
            return [left,right]
        # move right pointer towards the left if current sum > target
        if sum > target_sum:
            right -= 1
        # move left pointer towards the right if current sum < target
        else:
            left += 1
        sum = 0
    return [-1, -1]

def main():
    arr = [1,2,3,4,6]
    print(pair_with_target_sum(arr,6))

if __name__ == '__main__':
    main()