class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dup = set(nums1)
            
        for n in nums2:
            if n in dup:
                res.append(n)
                dup.remove(n)
                
        return res
        