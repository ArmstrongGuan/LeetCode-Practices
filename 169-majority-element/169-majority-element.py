class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # the solution is based on Boyer-Moore Voting Algerithm as in the solution
        count=0
        for number in nums:
            if count==0:
                candidate=number
            if number==candidate:
                count+=1
            else:
                count-=1
        return candidate