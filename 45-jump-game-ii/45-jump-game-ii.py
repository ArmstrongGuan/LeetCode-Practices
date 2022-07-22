class Solution:
    def jump(self, nums: List[int]) -> int:
        count=0
        cur=0
        pre=-1
        n=len(nums)
        while cur<n-1:
            count+=1
            new=0
            for i in range(pre+1, cur+1):
                new=max(new, i+nums[i])
            pre, cur=cur,new
        return count