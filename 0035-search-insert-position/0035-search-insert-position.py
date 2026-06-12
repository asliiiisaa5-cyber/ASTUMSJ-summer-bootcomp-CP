class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x = 0
        t = len(nums)-1
        while x<=t:
            m = (x+t)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                x=m+1
            else:
                t=m-1
        return x
        


        