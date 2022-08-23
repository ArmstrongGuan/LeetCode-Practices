class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]* n
        for i in range(1, n):
            answer[i]=nums[i-1]*answer[i-1] #so far the answer[i] store the product of all numbers before nums[i]
        cur=nums[-1]
        for i in range(n-2, -1, -1):
            answer[i]*=cur
            cur*=nums[i]
        return answer
            