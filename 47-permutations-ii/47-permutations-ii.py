class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:        
        if len(nums)==1:
            return [nums]
        nums.sort()
        cur=-11
        result=[]
        for i in range(len(nums)):
            x=nums[i]
            if x!=cur:
                cur=x
                for u in self.permuteUnique(nums[:i]+nums[i+1:]):
                    result.append(u+[x])
        return result