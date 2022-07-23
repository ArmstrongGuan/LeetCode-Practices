class Solution:
    def numDecodings(self, s: str) -> int:
        
        #recursive calculation
        def decoding(s):
            if s[0]=='0':
                return 0
            if len(s)==1:
                return 1
            if len(s)==2:
                if int(s)<=26:
                    return 1
                else:
                    return 0
            
        if len(s)==1:
            return decoding(s)
        if len(s)==2:
            return decoding(s[0])*decoding(s[1])+decoding(s)
        
        result=[]
        result.append(decoding(s[0]))
        result.append(decoding(s[0])*decoding(s[1])+decoding(s[0:2]))
        
        end=2
        
        while end<len(s):
            a=s[end]
            b=s[end-1:end+1]
            #print(end, result, a,b)
            result.append(result[-1]*decoding(a)+result[-2]*decoding(b))
            end+=1
        return result[-1]
