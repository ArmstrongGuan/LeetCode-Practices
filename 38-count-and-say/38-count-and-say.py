class Solution:
    def countAndSay(self, n: int) -> str:
        def convert(num):
            cur=num[0]
            mul=1
            output=""
            for i in range(len(num)):
                cur=num[i]
                if i< len(num)-1 and num[i+1]==cur:                    
                    mul=mul+1
                #elif num[i+1]!=cur:
                #    output+=str(mul)+str(num[i])
                #    mul=1
                #else: 
                #    output+=str(mul)+str(num[i])
                else:
                    output+=str(mul)+str(num[i])
                    mul=1
            return(output)
        a='1'
        while n-1:
            a=convert(a)
            n-=1
        return(a)