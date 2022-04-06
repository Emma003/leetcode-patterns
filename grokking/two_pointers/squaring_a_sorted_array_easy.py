#Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

def make_squares(arr):
    left, right = 0, len(arr) - 1
    squares = []
    while left <= right:
        left_sq, right_sq = arr[left]**2, arr[right]**2
        if left_sq > right_sq:
            squares.insert(0, left_sq)
            left += 1
        else:
            squares.insert(0, right_sq)
            right -= 1
    return squares

def main():
    arr = [-3, -1, 0, 1, 2]
    print(make_squares(arr))

if __name__ == '__main__':
    main()
