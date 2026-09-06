class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0)+1
        for i in range(len(nums)):
            if seen[nums[i]] == 1:
                return nums[i]
        