class MinStack:

    def __init__(self):
        self.stack = []
        
        #this array will mirror the stack and keep track of what was the smallest value when x was added to the stack
        self.minSoFar = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        #if minStack is empty, then current value is the smallest
        if not self.minSoFar:
            self.minSoFar.append(val)
        #append the min val between curr val and curr min
        else:
            currMin = self.minSoFar[-1]
            self.minSoFar.append(min(currMin, val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minSoFar.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minSoFar[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()