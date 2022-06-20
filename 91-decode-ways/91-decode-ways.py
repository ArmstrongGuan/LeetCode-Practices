class Solution:
    def numDecodings(self, s: str) -> int:
        #recursive calculation
        def decoding(s):
            if s=='':
                return 1
            if s[0]=='0':
                return 0
            if len(s)==1:
                return 1
            if len(s)==2:
                if int(s)<=26:
                    return 1+decoding(s[0])*decoding(s[1])
                else:
                    return decoding(s[0])*decoding(s[1])
            i=len(s)//2
            return decoding(s[:i])*decoding(s[i:i+1])*decoding(s[i+1:])+decoding(s[:i-1])*int(s[i-1]!="0" and int(s[i-1:i+1]) <=26)*decoding(s[i+1:])+decoding(s[:i])*int(s[i]!="0" and int(s[i:i+2])<=26)*decoding(s[i+2:])
        return decoding(s)