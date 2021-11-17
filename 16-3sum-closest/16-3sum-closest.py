class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        output=nums[0]+nums[1]+nums[2]-target
        for i in range(len(nums)):
            l,r=i+1, len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==target:
                    return target
                elif nums[i]+nums[l]+nums[r]>target:
                    if abs(nums[i]+nums[l]+nums[r]-target)<abs(output-target):
                        output = nums[i]+nums[l]+nums[r]
                    r -= 1
                else: 
                    if abs(nums[i]+nums[l]+nums[r]-target)<abs(output-target):
                        output = nums[i]+nums[l]+nums[r]
                    l += 1
                print(output)
        return(output)