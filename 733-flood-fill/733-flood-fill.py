
def explore(grid, r, c, currColor, newColor, visited):
    #out of bounds
    if r < 0 or r >= len(grid):
        return
    if c < 0 or c >= len(grid[0]):
        return
    
    #visited
    curr = str(r) + "," + str(c)
    if curr in visited:
        return 
    visited.add(curr)
    
    #not same color
    if grid[r][c] != currColor:
        return
    
    
    #change color
    grid[r][c] = newColor
    
    #explore neighbors
    explore(grid, r+1, c, currColor, newColor, visited)
    explore(grid, r-1, c, currColor, newColor, visited)
    explore(grid, r, c+1, currColor, newColor, visited)
    explore(grid, r, c-1, currColor, newColor, visited)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        explore(image, sr, sc, image[sr][sc], color, visited)
        
        return image