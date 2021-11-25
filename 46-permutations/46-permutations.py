class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def swap(j,k, nums):
            output=nums[:]
            output[j]=nums[k]
            output[k]=nums[j]
            return output
        n=len(nums)
        if n==1:
            return([nums])
        output=[nums]
        for i in range(1,n):            
            for j in range(len(output)):
                for k in range(i):
                    output.append(swap(i,k,output[j]))
        return(output)
            