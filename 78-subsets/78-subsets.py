class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        output=[]
        for i in range(2**n):
            element=[]
            for j in range(n):
                if i%2==1: element.append(nums[j])
                i=i//2
            output.append(element)
        return(output)