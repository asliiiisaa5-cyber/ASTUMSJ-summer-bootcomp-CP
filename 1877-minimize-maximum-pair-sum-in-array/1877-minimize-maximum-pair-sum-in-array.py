class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        mx = 0
        y = len(nums)-1
        while x<y:
            if nums[x]+nums[y]>mx:
               mx = nums[x]+nums[y]
            x+=1
            y-=1
        return mx   


        

        