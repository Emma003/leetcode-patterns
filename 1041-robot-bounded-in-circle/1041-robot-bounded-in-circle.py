class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #execute set of movements 4 times
            #if the robot is back to initial pos, its a circle
            
        x,y = 0, 0
        dx, dy = 0, 1
        
        for i in range(4):
            for ins in instructions:
                if ins == 'G':
                    x += dx
                    y += dy

                elif ins == 'L':
                    dx, dy = -dy, dx
                elif ins == 'R': 
                    dx, dy = dy, -dx
                
        return x == 0 and y == 0
        