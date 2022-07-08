class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #result[i] is the bigest sum ending at nums[i]
        result=nums[0:1]
        for i in range(1, len(nums)):
            if result[i-1]<=0:
                result.append(nums[i])
            else:
                result.append(result[-1]+nums[i])
        return max(result)