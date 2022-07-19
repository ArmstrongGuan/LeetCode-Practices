class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        count=0
        prod=nums[0]
        i=0
        j=0
        while j<len(nums):
            if prod<k:
                count+=j-i+1
                j=j+1
                if j<len(nums):
                    prod=prod*nums[j]
            else:
                if i<j:
                    i=i+1
                    prod=prod//nums[i-1]
                else:
                    i=j=j+1
                    if j<len(nums):
                        prod=nums[i]
        return count
                    
            