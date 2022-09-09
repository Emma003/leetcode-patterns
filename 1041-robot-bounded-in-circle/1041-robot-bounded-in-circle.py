


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #if it hasnt changed positions: TRUE
        #if it has changed positions AND directions
        
        dx, dy = 0, 1
        x, y = 0, 0
        
        
        for i in instructions:
            if i == 'G':
                x += dx
                y += dy

            if i == 'L':
                dx, dy = -dy, dx
            if i == 'R':
                dx, dy = dy, -dx
            
        return (x, y) == (0,0) or (dx, dy) != (0,1)
    
    


                