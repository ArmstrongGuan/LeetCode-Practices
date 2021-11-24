class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return([-1, -1])
        low, low1, low2, high, high1, high2 = 0, 0, 0, len(nums)-1, len(nums)-1, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid]>target:
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                low1, low2=low, mid
                high1,high2=mid, high
                break
        print([low, high])
        if low>=high and nums[low]==target:
            return([low, low])
        if low>=high and nums[low]!=target:
            return([-1, -1])
        print([low1, high1, low2, high2])
        while low1< high1:
            mid = (low1+high1)//2
            if nums[mid]==target:
                high1=mid
            else:
                low1=mid+1
        while low2< high2:
            mid = (low2+high2)//2+1
            if nums[mid]==target:
                low2=mid
            else:
                high2=mid-1
        return([low1, low2])

            