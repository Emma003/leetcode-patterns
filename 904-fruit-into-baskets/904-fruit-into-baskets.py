class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
        baskets = {}
        start, max_fruits = 0, 0
        
        for end in range(len(fruits)):
            right = fruits[end]
            
            if right not in baskets:
                baskets[right] = 0
            baskets[right] += 1
            
            while len(baskets) > 2:
                left = fruits[start]
                
                baskets[left] -= 1
                if baskets[left] == 0: 
                    del baskets[left]
                    
                start += 1
                    
        
            max_fruits = max(max_fruits, end - start + 1)
            
        return max_fruits
            
            
        