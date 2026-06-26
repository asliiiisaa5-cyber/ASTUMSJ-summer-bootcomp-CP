class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
         srt = 1
         ans = 1
         for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                srt += 1
            else:
                srt = 1
            ans += srt
         return ans
        