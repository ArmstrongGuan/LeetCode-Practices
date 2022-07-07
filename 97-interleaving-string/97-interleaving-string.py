class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3=len(s1), len(s2), len(s3)
        if l1+l2!=l3:
            return False
        if l1==0:
            if s2==s3:
                return True
            else:
                return False
        if l2==0:
            if s1==s3:
                return True
            else:
                return False
        result=[[False]*(l3) for _ in range(l3)]
        result[0][0]=True
        for k in range(1,l3+1):
            if k<=l2: result[0][k]= (result[0][k-1] and s2[k-1]==s3[k-1]) 
            if k<=l1: result[k][0]= (result[k-1][0] and s1[k-1]==s3[k-1])
            for i in range(1, min(k, l1+1)):
                if k-i<=l2:
                    result[i][k-i]= ((result[i-1][k-i] and s1[i-1]==s3[k-1]) or (result[i][k-i-1] and s2[k-i-1]==s3[k-1]))
        return result[l1][l2]