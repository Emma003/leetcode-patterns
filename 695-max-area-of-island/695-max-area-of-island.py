def explore(grid, r, c, visited):
    #out of bounds
    if r < 0 or r >= len(grid):
        return 0
    if c < 0 or c >= len(grid[0]):
        return 0
    
    #water
    if grid[r][c] == 0:
        return 0
    
    #already visited
    curr = str(r) + ',' + str(c)
    if curr in visited:
        return 0
    visited.add(curr)
    
    #explore neighbors
    size = 1
    size += explore(grid, r-1, c, visited)
    size += explore(grid, r+1, c, visited)
    size += explore(grid, r, c-1, visited)
    size += explore(grid, r, c+1, visited)
    
    return size
    
    
    


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxSize = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                size = explore(grid, row, col,visited)
                maxSize = max(maxSize, size)
                
        return maxSize
    