class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        harshmap={}
        for letter in pattern:
            if s=="":
                return False
            if letter in harshmap:
                if " " in s:
                    loc=s.index(" ")
                    cur=s[:loc]
                    s=s[loc+1:]
                else:
                    cur=s
                    s=""
                if cur==harshmap[letter]:
                    continue
                else:
                    return False
            else:
                if " " in s:
                    loc=s.index(" ")
                    cur=s[:loc]                    
                    s=s[loc+1:]
                else:
                    cur=s                    
                    s=""
                if cur in harshmap.values():
                    return False
                harshmap[letter]=cur
        if s!="":
            return False
        else:
            return True
                    
            