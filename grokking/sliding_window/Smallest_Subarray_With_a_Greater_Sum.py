
# PROBLEM STATEMENT
# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest
# contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

import math

def smallest_subarray_sum(s, arr):
  window_start, window_sum, window_size = 0, 0.0, math.inf

  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    while window_sum >= s:
      window_size = min(window_size, window_end-window_start+1)
      window_sum -= arr[window_start]
      window_start+= 1
  if window_size == math.inf:
    return 0
  return window_size


def main():
  array = [2,1,5,2,3,2]
  smallest_subarray_sum(7,array)

main()