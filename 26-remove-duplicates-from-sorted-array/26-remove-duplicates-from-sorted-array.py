class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur=-101
        curnum=0
        for i in range(len(nums)):
            if nums[i]!=cur:
                cur=nums[i]
                nums[curnum]=nums[i]
                curnum+=1
        return(curnum)