class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        cur=nums[0]-1
        count=0
        n=(len(nums)+1)//2
        for x in nums:
            if x==cur:
                count+=1
            else:
                cur=x
                count=1
            if count>=n:
                return x