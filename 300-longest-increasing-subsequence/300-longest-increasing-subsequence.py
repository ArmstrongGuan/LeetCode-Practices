class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #excellent explanation in solution
        #note that approach 2 is collecting a sequence for the smallest end for all sequences of length i
        result=[]
        count=0
        for i in range(len(nums)):
            result.append(1)
            for j in range(i-1,-1,-1):
                if nums[j]<nums[i]:
                    result[i]=max(result[i], result[j]+1)
        return max(result)
            