
def explore(grid, r,c,visited):

    #make sure none of the neighbors is out of bounds
    if r < 0 or r >= len(grid): 
        return False
    if c < 0 or c >= len(grid[0]):
        return False

    #if curr is water, leave
    if grid[r][c] == "0":
        return False

    #translate to string so it can be hashed and check visited
    currStr = str(r) + "," + str(c)
    if currStr in visited:
        return False

    visited.add(currStr)

    #explore neighbors
    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r, c+1, visited)
    
    return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islandCount = 0

        #traverse grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if explore(grid, row, col, visited):
                    islandCount += 1

        return islandCount