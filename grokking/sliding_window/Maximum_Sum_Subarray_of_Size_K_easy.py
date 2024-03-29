
# PROBLEM STATEMENT
# Given an array of positive numbers and a positive number ‘k,’
# find the maximum sum of any contiguous subarray of size ‘k’.

def max_sub_array_of_size_k(k, arr):
  window_start, window_sum, max_sum = 0, 0.0, -1
  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    if window_end >= k-1:
      max_sum = max(window_sum, max_sum)
      window_sum -= arr[window_start]
      window_start+= 1
  return max_sum


def main():
  arr = [2,1,5,1,3,2]
  max_sub_array_of_size_k(3,arr)

main()