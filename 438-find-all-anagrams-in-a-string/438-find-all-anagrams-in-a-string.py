class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result=[]
        if len(s)<len(p):
            return result
        p_count= [0]*26
        for i in range(len(p)):
            p_count[ord(p[i])-97]+=1
        s_count= [0]*26
        for i in range(len(p)):
            s_count[ord(s[i])-97]+=1
        if s_count==p_count:
            result.append(0)
        for i in range(1,len(s)-len(p)+1):
            s_count[ord(s[i-1])-97]-=1
            s_count[ord(s[i+len(p)-1])-97]+=1
            if s_count==p_count:
                result.append(i)
        return result
            