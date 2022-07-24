class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for i in text2] for j in text1] #record length of longest common subsequence using for text1[:i+1], text2[:j+1]
        for i in range(len(text1)):
            if text1[i]==text2[0]:
                for j in range(i, len(text1)):
                    dp[j][0]=1
                break
        for i in range(len(text2)):
            if text2[i]==text1[0]:
                for j in range(i, len(text2)):
                    dp[0][j]=1
                break
        
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i]==text2[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                    
        #print(dp)
        return dp[len(text1)-1][len(text2)-1]