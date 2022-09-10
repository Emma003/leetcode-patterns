class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda i:i[1], reverse = True)
        
        maxUnits = 0
        
        for numBoxes, unitsPerBox in boxTypes:
            
            for i in range(numBoxes):
                if truckSize <= 0:
                    break
                    
                maxUnits += unitsPerBox
                truckSize -= 1
                
            if truckSize <= 0:
                    break
                    
        return maxUnits
        