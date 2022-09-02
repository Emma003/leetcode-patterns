class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l,r = 0, len(matrix)-1
        while l < r:
            
            for i in range(r-l):
                #bc its a square matrix, l==top and r==bottom
                top, bottom = l, r
                
                #keep topleft in tmp var
                topLeft = matrix[top][l+i]
                
                #replace nums
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft
                
            
            #update l and r
            l += 1
            r -= 1

                
