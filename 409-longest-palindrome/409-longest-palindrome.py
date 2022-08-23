class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=[0]*58
        for i in s:
            count[ord(i)-65]+=1
        extra=0
        result=0
        for i in count:
            if i%2 ==1:
                extra=1
            result+=i-i%2
        result+=extra
        return result