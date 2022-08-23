class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #harshmap[i] saves how many time the total sum from the beginning to a position is equal to i
        n=len(nums)
        total=0
        count=0
        harshmap={}
        harshmap[0]=1
        for i in range(n):
            total+=nums[i]
            if total-k in harshmap:
                count+=harshmap[total-k]
            if total in harshmap:
                harshmap[total]+=1
            else:
                harshmap[total]=1        
        return count