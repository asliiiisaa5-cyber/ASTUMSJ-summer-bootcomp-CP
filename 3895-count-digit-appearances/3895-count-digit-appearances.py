class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        for i in nums:
            lis=list(str(i))
            for j in lis:
                if int(j)==digit:
                    count+=1
        return count
