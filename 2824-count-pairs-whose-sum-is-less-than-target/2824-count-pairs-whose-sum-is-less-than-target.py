class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        numspair = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i] + nums[j] < target:
                    numspair+=1
        return numspair 