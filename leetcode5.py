class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth=len(s)
        while lenth>0:
            for i in range(len(s)-lenth+1):
                if s[i:i+lenth]==s[i:i+lenth][::-1]:
                    return s[i:i+lenth]
            lenth-=1
pass

solu=Solution()
s='babad'
print(solu.longestPalindrome(s))