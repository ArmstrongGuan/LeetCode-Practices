class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #excellent explanation in solution
        #note that approach 2 is collecting a sequence for the smallest end for all sequences of length i
        #the following is approach 2
        result=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>result[-1]:
                result.append(nums[i])
            else:
                low, high=0, len(result)-1
                while low<high:
                    cur=(low+high)//2
                    if nums[i]>result[cur]:
                        low=cur+1
                    elif nums[i]<result[cur]:
                        high=cur
                    elif nums[i]==result[cur]:
                        break
                if low==high:
                    result[low]=nums[i]
        return len(result)
                    
                    
                    
            