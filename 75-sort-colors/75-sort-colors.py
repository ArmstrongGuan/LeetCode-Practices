class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        loc=[0,0,0] #location of the first 0, 1, 2        
        print(type(loc))
        print(loc)
        for i in range(len(nums)):
            if nums[i]==1:
                nums[i], nums[loc[2]]=nums[loc[2]],nums[i]
                loc[2]+=1
            elif nums[i]==0:
                nums[i], nums[loc[2]], nums[loc[1]]=nums[loc[2]],nums[loc[1]], nums[i]
                loc[1]+= 1
                loc[2]+= 1
        return(nums)
                
                
                
            
            