class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        #print(nums)
        output=[]
        i=0
        while i in range(len(nums)-3):
            j=len(nums)-1
            while j in range(len(nums)-1,i+2,-1):
                a=target-nums[i]-nums[j]
                l,r=i+1, j-1
                while l<r:
                    #print([i,l,r,j])
                    if nums[l]+nums[r]<a:
                        l+=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    elif nums[l]+nums[r]==a:
                        output=output+[[nums[i], nums[j], nums[l], nums[r]]]
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    else:
                        r-=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                j-=1
                while j>i+2 and nums[j]==nums[j+1]:
                    j-=1
            i+=1
            while i <len(nums)-3 and nums[i]==nums[i-1]:
                i+=1
        return(output)
            
         
            
                    