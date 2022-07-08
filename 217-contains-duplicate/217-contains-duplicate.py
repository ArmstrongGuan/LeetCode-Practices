class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        harshmap={}
        for i in nums:
            if i in harshmap:
                return True
            else:
                harshmap[i]=True