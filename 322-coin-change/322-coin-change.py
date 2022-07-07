class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result=[-1]*(amount+1)
        result[0]=0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i>=coins[j] and result[i-coins[j]]>=0:
                    result[i]= result[i-coins[j]]+1 if result[i]==-1 else min(result[i], result[i-coins[j]]+1)
        return result[amount]
                    
                       