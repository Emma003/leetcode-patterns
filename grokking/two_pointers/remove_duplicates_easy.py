# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates
# in-place return the length of the subarray that has no duplicate in it.

def remove_duplicates(arr):
    next_non_dup = 0
    for next in range(len(arr)):
        if arr[next] != arr[next_non_dup]:
            next_non_dup += 1
            arr[next_non_dup] = arr[next]
    return next_non_dup + 1



# Given an unsorted array of numbers and a target ‘key’, remove all instances of
# ‘key’ in-place and return the new length of the array.

def remove_key(arr, key):
    non_key = 0
    for next in range(len(arr)):
        if arr[next] != key:
            arr[non_key] = arr[next]
            non_key += 1
    return non_key

def main():
    arr = [2,11,2,2,1]
    print(remove_key(arr,2))

if __name__ == '__main__':
    main()