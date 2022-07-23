class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        start=0
        count=0
        while start<=n-3:
            if nums[start]+nums[start+2]==nums[start+1]*2:
                step=nums[start+1]-nums[start]
                stop=start+2
                while stop<n and nums[stop]-nums[start] == step*(stop-start):
                    stop+=1
                count= count+ (stop-start-1)*(stop-start-2)//2
                start=stop-1
            else:
                start+=1
        return count
        