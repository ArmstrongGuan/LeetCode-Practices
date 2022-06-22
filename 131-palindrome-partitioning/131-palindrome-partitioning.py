class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s=="":
            return [[]]
        if len(s)==1:
            return [[s]]
        result=[]
        for i in range(1,len(s)+1):
            if s[:i]==s[i-1::-1]:
                result=result+ [[s[:i]]+rest for rest in self.partition(s[i:])]
        return result
            
                

                