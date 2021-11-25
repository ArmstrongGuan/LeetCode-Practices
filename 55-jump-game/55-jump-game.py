class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur=0
        reach=0
        while cur in range(len(nums)) and cur<= reach and reach< len(nums)-1:
            reach = max(reach, cur+nums[cur])
            cur+=1
            print(cur, reach)
        if reach>= len(nums)-1:
            return(True)
        else:
            return(False)