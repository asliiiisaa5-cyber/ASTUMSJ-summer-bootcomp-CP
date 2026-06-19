class Solution:
    def reverseWords(self, s: str) -> str:
        x = ' '.join(word[::-1] for word in s.split())
        return x
        