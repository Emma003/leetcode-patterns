class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def explore(r, c, currColor):
            #check out of bounds
            if r < 0 or r >= len(image):
                return
            if c < 0 or c >= len(image[0]):
                return 
            
            #check current cell is same color as starting cell
            if image[r][c] != currColor:
                return
            
            
            #cell was already visited
            if image[r][c] == color:
                return 
            
            #fill cell
            image[r][c] = color
            
            #visit neighbors
            
            #north
            explore(r-1, c, currColor)
            
            #west
            explore(r, c-1, currColor)
            
            #south
            explore(r+1, c, currColor)
            
            #east
            explore(r, c+1, currColor)
            
        explore(sr, sc, image[sr][sc])
        return image
            
            