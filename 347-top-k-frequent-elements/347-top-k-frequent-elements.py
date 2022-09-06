class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for x in range(len(nums)+1)]
        
        
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
            
        
        for num, frequency in count.items():
            freq[frequency].append(num)
            
        res = []
        for i in range(len(freq)-1, 0, -1):
            curr = freq[i]
            
            for n in curr:
                res.append(n)
                if len(res) == k:
                    return res


#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
