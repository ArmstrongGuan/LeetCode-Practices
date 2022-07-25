class Solution:
    def integerBreak(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 1
        if n==3:
            return 2
        dp=[1]*(n+1)
        dp[3]=2
        for i in range(4, n+1):
            print(dp)
            for j in range(2, i//2+1):
                dp[i]= max(dp[i], max(i-j, dp[i-j])*j)
        print(dp)
        return dp[-1]