class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #define a order while regarding k as kkkkkkk
        def isless(a,b):
            if int(str(a)+str(b))<int(str(b)+str(a)):
                return True
            else: return False
            
        result=""
        for i in range(len(nums)):
            for j in range(len(nums)-2,i-1,-1):
                if isless(nums[j], nums[j+1]):
                    nums[j], nums[j+1]=nums[j+1], nums[j]
            result=result+str(nums[i])
        if result[0]=="0":
            return "0"
        return result