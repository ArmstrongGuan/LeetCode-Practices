class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp1=[1]*n #the length of LIS ending at the i-th position
        dp2=[1]*n #the number of LIS ending at the i-th position
        for i in range(n):
            #print(dp1, dp2)
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp1[i]>dp1[j]+1:
                        continue
                    elif dp1[i]==dp1[j]+1:
                        dp2[i]+=dp2[j]
                    else:
                        dp1[i]=dp1[j]+1
                        dp2[i]=dp2[j]
        maxlength=max(dp1)
        count=0
        for i in range(n):
            if dp1[i]==maxlength:
                count+=dp2[i]
        return count
            
        