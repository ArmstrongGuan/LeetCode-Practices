class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count=len(nums)+1
        total=nums[0]
        i=0
        j=0
        while j<len(nums):
            if total<target:
                j=j+1
                if j<len(nums):
                    total+=nums[j]
            else:
                count=min(count, j-i+1)
                if i<j:
                    i=i+1
                    total=total-nums[i-1]
                else:
                    return 1
        if count==len(nums)+1:
            return 0
        else:
            return count