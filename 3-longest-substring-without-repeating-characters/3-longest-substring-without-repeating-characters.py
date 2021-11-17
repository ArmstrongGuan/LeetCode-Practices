class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer=0
        sub=''
        for i in range(len(s)):
            if s[i] in sub:
                answer= max(answer, len(sub))
                sub=sub[sub.index(s[i])+1 : ]+s[i]
            else:
                sub=sub+s[i]
        return(max(answer,len(sub)))
                