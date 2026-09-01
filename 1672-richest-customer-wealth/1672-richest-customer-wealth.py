class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # lst = []
        # row = len(accounts)
        # for i in range(row):
        #     smof = sum(accounts[i])
        #     lst.append(smof)
        # return max(lst)
        # inprove the i thinking
        
        richest = 0
        for i in accounts:
            sm = sum(i)
            if richest < sm:
                richest = sm
        return richest
        
        