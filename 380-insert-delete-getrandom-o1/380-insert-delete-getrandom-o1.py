class RandomizedSet:

    def __init__(self):
        #map value to arrIndex
        self.randomSet = {}
        
        #keeps keys to map
        self.keys = []
        
    def insert(self, val: int) -> bool:
        if val not in self.randomSet:
            #add val to end of arr
            self.keys.append(val)
            
            #add index as value of key
            self.randomSet[val] = len(self.keys)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            
            #find index of target object
            idx = self.randomSet[val]
            lastVal = self.keys[-1]
            
            #delete from array (replace it with element at last index and pop last)
            self.keys[idx] = lastVal
            
            #delete last element
            self.keys.pop()
            
            #update the map index of the last element in the array
            self.randomSet[lastVal] = idx
            
            #delete from map
            del self.randomSet[val]
            
            return True
        
        return False
    
    def getRandom(self) -> int:
        randIndex = randint(0, len(self.keys) -1)
        
        return random.choice(self.keys)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()