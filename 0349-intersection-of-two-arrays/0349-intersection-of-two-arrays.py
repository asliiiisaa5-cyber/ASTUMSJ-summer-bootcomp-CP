class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set(nums1) 
        rse = set(nums2)
        x = res.intersection(rse)
        return list(x)
        
        