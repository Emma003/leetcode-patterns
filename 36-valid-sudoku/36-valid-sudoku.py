class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check rows
        for i in range(len(board)):
            lot = set()
            for j in range(len(board)):
                    cell = board[i][j]
                    if cell.isdigit():
                        if cell in lot:
                            return False
                        lot.add(cell)
            
            
        #check cols
        for i in range(len(board)):
            lot = set()
            for j in range(len(board)):
                cell = board[j][i]
                if cell.isdigit():
                    if cell in lot:
                        return False
                    lot.add(cell)
                
        
        #check 3x3 grids
        gridMap = {}
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].isdigit():
                    gridRow = i//3
                    gridCol = j//3

                    gridKey = str(gridRow) + "," + str(gridCol)
                    if gridKey not in gridMap:
                        gridMap[gridKey] = set()

                    gridSet = gridMap[gridKey]
                    if board[i][j] in gridSet:
                        return False
                    gridSet.add(board[i][j])
                
                
        return True
                
                