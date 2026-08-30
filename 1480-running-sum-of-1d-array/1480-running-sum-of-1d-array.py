class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
#         arry = []
#         x = 0
#         arry.append(nums[0])
#         for i in range(1,len(nums)):
#             arry.append(arry[x]+nums[i])
#             x+=1
#         return arry
# One thing I want to improve
            total = 0
            answer = []
            for num in nums:
                total += num
                answer.append(total)
            return answer
        