class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        def rob1(nums):
            if len(nums)==0:
                return 0
            if len(nums)==1:
                return nums[0]
            i=len(nums)//2
            return max(rob1(nums[:i-1])+nums[i]+rob1(nums[i+2:]), rob1(nums[:i])+rob1(nums[i+1:]))    
        
        return max(nums[0]+rob1(nums[2:len(nums)-1]), rob1(nums[1:]))
    
        