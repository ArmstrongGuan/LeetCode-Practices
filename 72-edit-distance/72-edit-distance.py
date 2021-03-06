class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        dp=[[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)] #record length of longest common subsequence using for text1[:i], text2[:j]
        
        for i in range(len(text1)+1):
            dp[i][0]=i
            
        for i in range(len(text2)+1):
            dp[0][i]=i
        
        #print(dp)
        
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])+1
                    
        #print(dp)
        return dp[len(text1)][len(text2)]