class TwoSum:

    def __init__(self):
        self.stream = []

    def add(self, number: int) -> None:
        self.stream.append(number)

    def find(self, value: int) -> bool:
        return self.findSum(value)
    
    def findSum(self, t):
        visited = {}
        
        for i,n in enumerate(self.stream):
            
            diff = t - n
            
            if diff in visited:
                return True
            
            visited[n] = i	
            
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)