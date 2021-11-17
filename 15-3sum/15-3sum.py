class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        if len(nums)<3:
            return [] 
        for i in range(len(nums)):
            map={}
            for j in range(i+1,len(nums)):
                if -nums[i]-nums[j] in map:
                    temp=[nums[i], nums[j], -nums[i]-nums[j]]
                    temp.sort()
                    output= (output+[temp] if temp not in output else output)
                else:
                    map[nums[j]]=j
        return(output)