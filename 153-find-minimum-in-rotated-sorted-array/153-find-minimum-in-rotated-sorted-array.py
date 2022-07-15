class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high=0, len(nums)-1
        while low<high:
            if nums[low]<=nums[high]:
                return nums[low]
            if high-low==1:
                return nums[high]
            mid=(low+high)//2
            if nums[mid]>nums[low]:
                low=mid+1
            else:
                high=mid
        return nums[low]