def twoSum(nums, target):
    windowStart, windowSum = 0, 0
    twoSum = []
    for windowEnd in range(len(nums)):
        windowSum += nums[windowEnd]
        if windowEnd - windowStart == 1:
            if windowSum == target:
                twoSum.append(windowStart)
                twoSum.append(windowEnd)
            windowSum -= nums[windowStart]
            windowStart += 1
    return twoSum

def main():
    sum = [3,2,4]
    print(twoSum(sum,6))


main()