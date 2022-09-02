class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        grids = {}
        
        for r in range(len(board)):
            for c in range(len(board)):
                cell = board[r][c]
                
                #empty cell
                if not cell.isdigit():
                    continue
                    
                #create sets as values to the map keys
                if r not in rows:
                    rows[r] = set()
                    
                if c not in cols:
                    cols[c] = set()
                    
                if (r//3, c//3) not in grids:
                    grids[(r//3, c//3)] = set()
                    
                
                #check its in there
                if cell in rows[r] or cell in cols[c] or cell in grids[(r//3, c//3)]:
                    return False
                
                rows[r].add(cell)
                cols[c].add(cell)
                grids[(r//3, c//3)].add(cell)
        
        return True