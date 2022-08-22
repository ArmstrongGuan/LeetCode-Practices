class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        best=[nums[0]]
        for i in range(1, len(nums)):
            if nums[i]>best[0]:
                best.append(nums[i])
                break
            else:
                best[0]=nums[i]
        #print(i, best)
        if len(best)==1:
            return False
        else:
            for j in range(i+1, len(nums)):
                if nums[j]>best[1]:
                    return True
                elif nums[j]>best[0]:
                    best[1]=nums[j]
                else:
                    best[0]=nums[j]
        return False