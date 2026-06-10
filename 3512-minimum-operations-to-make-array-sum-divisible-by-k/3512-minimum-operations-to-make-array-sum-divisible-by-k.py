class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = sum(nums)
        count = 0
        while x > 0 and x % k != 0:
            x-=1
            count += 1
        return count
        