class Solution:
    def isHappy(self, n: int) -> bool:
        harshmap={}
        while n not in harshmap:
            squaresum=0
            quotient=n
            while quotient>0:
                quotient, remainder=quotient//10, quotient%10
                squaresum+=remainder**2
            harshmap[n]=squaresum
            n=squaresum
        if n==1:
            return True
        return False