class Solution:
    def isPalindrome(self, s: str) -> bool:
# first option
        s1 = ""
        for char in s:
            if char.isalnum():
                s1+=char
        if s1.lower() == s1.lower()[::-1]:
            return True
        else:
            return False
# second option 
        # left = 0
        # right = len(s1)-1
        # while right >= left:
        #     if s1[left] != s1[right]:
        #         return False
        #     left+=1
        #     right-=1
        # return True
        
            
        
        

        