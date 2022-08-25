class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        #first binary search
        top, bottom = 0, ROWS-1
        
        while top <= bottom:
            mid = (top+bottom) // 2
            
            if target < matrix[mid][0]:
                bottom = mid -1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
                
        #check that the item is within bounds:
        if top > bottom:
            return False
        
        #second binary search
        left, right = 0, COLS-1
        arr = matrix[mid]
        
        while left <= right:
            m = (left+right) // 2
            
            if target < arr[m]:
                right = m-1
            elif target > arr[m]:
                left = m+1
            else:
                return True
            
        return False
                