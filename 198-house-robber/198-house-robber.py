class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        i=len(nums)//2
        return max(self.rob(nums[:i-1])+nums[i]+self.rob(nums[i+2:]), self.rob(nums[:i])+self.rob(nums[i+1:]))