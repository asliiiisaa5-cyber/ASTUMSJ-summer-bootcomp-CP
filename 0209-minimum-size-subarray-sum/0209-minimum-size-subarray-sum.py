class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_length = float("inf")
        for i in range(len(nums)):
            window_sum +=nums[i]
            while target<=window_sum:
                current_length = i-left +1
                if current_length < min_length:
                    min_length = current_length

                window_sum -= nums[left]
                left+=1
        if min_length == float("inf"):
            return 0
        return min_length
        