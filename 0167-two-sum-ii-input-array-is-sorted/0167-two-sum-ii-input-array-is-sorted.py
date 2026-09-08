class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # first option 
# two pointer concept
        left = 0
        right = len(numbers)-1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif target < total:
                right-=1
            else:
                left+=1
    # second option
# hash map concept
        #   seen = {}
        #   for i, num in enumerate(numbers):
        #     foundnum = target - num
        #     if foundnum in seen:
        #         return [seen[foundnum]+1,i+1]
        #     seen[num] = i