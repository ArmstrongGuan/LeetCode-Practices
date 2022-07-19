class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1
        count=0
        while i>=0 or j>=0:
            while i>=0 and (count>0 or s[i]=='#'):
                if i>=0 and s[i]=='#':
                    count=count+1
                    i=i-1
                else:
                    i=i-1
                    count=count-1
            count=0
            while j>=0 and (count>0 or t[j]=='#'):
                if j>=0 and t[j]=='#':
                    count=count+1
                    j=j-1
                else:
                    j=j-1
                    count=count-1
            if i>=0 and j>=0:
                if s[i]==t[j]:
                    i=i-1
                    j=j-1
                else:
                    return False
            else:
                if i<0 and j<0:
                    return True
                else:
                    return False                
        if i<0 and j<0:
            return True
        else:
            return False