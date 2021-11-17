class Solution:
    def longestPalindrome(self, s: str) -> str:
        output =s[0]
        maxlen=1
        i=0
        while i+maxlen< len(s):
            for j in range(i+maxlen, len(s)):
                if s[i]==s[j]:
                    sub=s[i:j+1]
                    a=(j+1-i)//2
                    if sub[:a]==sub[-1:-a-1:-1]:
                        output=sub
                        maxlen=j-i+1
                        i=-1
                        break
            i=i+1
        return(output)
        