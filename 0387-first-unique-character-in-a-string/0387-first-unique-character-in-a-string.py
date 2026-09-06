class Solution:
    def firstUniqChar(self, s: str) -> int:
# first option 
        seen = {}
        for char in s:
            seen[char] = seen.get(char,0)+1
        for num in range(len(s)):
            if seen[s[num]] == 1:
                return num
        return -1
        



        
        
        