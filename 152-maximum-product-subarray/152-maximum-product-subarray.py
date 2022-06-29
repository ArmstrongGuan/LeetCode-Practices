class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        count=0 #count for negative numbers in a interval without 0
        maxprod=0
        cur=0
        firstneg=1
        maxpos=0
        mark=0
        for i in nums:
            #print(cur,maxprod, firstneg, maxpos)
            if i==0:
                maxprod=max(maxprod, cur, cur//firstneg, maxpos)
                firstneg=1
                maxpos=0
                count=0
                cur=0
                mark=0
                continue
            else:
                if count ==1 and mark ==0:
                    firstneg=cur
                    mark=1
                a=cur*i if cur!=0 else i
                if i<0:
                    count+=1                    
                    if cur!=0 and count %2==1:
                        maxpos=cur
                cur=a
        return max(maxprod, cur, cur//firstneg, maxpos)
                    
                
                
                
        