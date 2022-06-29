class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #print(nums)
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[0]<nums[1]:
                return 1
            if nums[0]> nums[1]:
                return 0
        i=len(nums)//2
        #print(i)
        if nums[i-1]<nums[i] and nums[i+1]<nums[i]:
            return i
        if nums[i-1]>nums[i]:
            return self.findPeakElement(nums[:i])
        if nums[i]< nums[i+1]:
            return i+1+self.findPeakElement(nums[i+1:])
        