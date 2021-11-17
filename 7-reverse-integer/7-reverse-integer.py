class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x[0]=='-':
            y=-int(x[:0:-1])
        else:
            y=int(x[::-1])
        print(y)
        if y< - 2**31 or y >=2**31:
            return(0)
        else:
            return(y)