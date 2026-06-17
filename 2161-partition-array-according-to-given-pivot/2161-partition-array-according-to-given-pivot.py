class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        x = []
        r = []
        y = []
        for i in range(len(nums)):
            if nums[i]>pivot:
                y.append(nums[i])
            elif nums[i]==pivot:
                r.append(nums[i])
            else:
                x.append(nums[i])
        z = x+r+y
        return z
    
        