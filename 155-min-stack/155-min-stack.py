class MinStack:

    def __init__(self):
        self.q = deque()
        self.mindeq = deque()

    def push(self, val: int) -> None:
        self.q.append(val)
        
        if self.mindeq:
            val = min(val, self.mindeq[-1])
            
        self.mindeq.append(val)
            

    def pop(self) -> None:
        self.mindeq.pop()
        self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.mindeq[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()