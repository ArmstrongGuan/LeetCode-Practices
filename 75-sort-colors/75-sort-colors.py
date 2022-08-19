class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        loc=[0,0,0] #location of the first 0, 1, 2, possibly the same number if there is no certain number        
        for i in range(len(nums)):
            if nums[i]==1:
                nums[i], nums[loc[2]]=nums[loc[2]],nums[i] #for place with 1, exchange it with the first 2
                loc[2]+=1
            elif nums[i]==0:
                nums[i], nums[loc[2]], nums[loc[1]]=nums[loc[2]],nums[loc[1]], nums[i]#for place with 0, rotate the first 1, the first 2 and the currect place
                loc[1]+= 1
                loc[2]+= 1
        return(nums)
                
                
                
            
            