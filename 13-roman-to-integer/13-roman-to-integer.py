class Solution:
    def romanToInt(self, s: str) -> int:
        map={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        answer=0
        for i in range(len(s)):
            answer=answer+map[s[i]]
        if "CD" in s or "CM" in s:
            answer=answer-200
        if "XL" in s or "XC" in s:
            answer=answer-20
        if "IV" in s or "IX" in s:
            answer=answer-2
        return(answer)