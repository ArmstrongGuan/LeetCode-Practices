class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:        
        #based on solution: instead of inserting the first element to different places recursively (which could cause problem that inserting the element in different places for different previous permutations could cause the same new permutation), it is a better idea to append different elements
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