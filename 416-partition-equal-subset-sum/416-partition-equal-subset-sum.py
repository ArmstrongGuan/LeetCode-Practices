class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2==1:
            return False
        goal=total//2
        result=[False] *(goal+1)
        result[0]=True
        for i in nums:
            for j in range(goal, i-1, -1):
                result[j]=result[j] or result[j-i]
        return result[goal]
                
            