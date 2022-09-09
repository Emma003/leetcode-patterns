


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #if it hasnt changed positions: TRUE
        #if it has changed positions AND directions
        
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)
        
        # xDir, yDir = 0, 1
        # xPos, yPos = 0, 0
        
        
#         for instr in instructions:
#             if instr == 'G':
#                 xPos += xDir
#                 yPos += yDir

#             elif instr == 'L':
#                 xDir = -1*yDir
#                 yDir = xDir
#             elif instr == 'R':
#                 xDir = yDir
#                 yDir = -1*xDir
            
#         return (xPos, yPos) == (0,0) or (xDir, yDir) != (0,1)
    
    


                