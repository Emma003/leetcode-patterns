class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        #binary search on rows (O(logM))
        top, bot = 0, ROWS-1
        while (top <= bot):
            row = (top + bot) // 2
            
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        
        #checking if the number wasnt found at all (failed while loop condition):
        if (top > bot):
            return False
        
        #doing binary search on the row found(O(log(N)))
        row = (top + bot) // 2
        l, r = 0, COLS-1
        arrOfInterest = matrix[row]
        
        while(l <= r):
            m = (l+r) // 2
            if target > arrOfInterest[m]:
                l = m+1
            elif target < arrOfInterest[m]:
                r = m-1
            else:
                return True
        
        return False
    




























        
        
        