class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def rot(matrix, l, r):
            if l >= r:
                return 
            
            top, bottom = l, r
            
            for i in range(r-l):
                #keep top left in tmp var before rotating
                topLeft = matrix[top][l+i]
                
                #rotate clockwise starting from bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l] 
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft
            
            
            l+=1
            r-=1
            rot(matrix, l, r)
            
        rot(matrix, 0, len(matrix)-1)