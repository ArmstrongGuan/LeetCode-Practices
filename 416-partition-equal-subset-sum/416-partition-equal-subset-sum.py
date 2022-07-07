class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #based on solution approach 4
        total=sum(nums)
        if total%2==1:
            return False
        goal=total//2
        result=[False] *(goal+1)
        result[0]=True
        for i in nums: #start the loop with i to avoid repetative use of elements in nums
            for j in range(goal, i-1, -1): #start from behind again to avoid repetative use of the current element i in nums
                result[j]=result[j] or result[j-i]
        return result[goal]
                
            