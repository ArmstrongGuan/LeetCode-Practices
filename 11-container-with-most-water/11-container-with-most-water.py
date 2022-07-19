class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0, len(height)-1
        vol=min(height[j],height[i])*(j-i)
        while i<j:
            if height[i]<=height[j]:
                while i < j and height[i]<=height[j]:
                    vol=max(vol, min(height[j],height[i])*(j-i))
                    i+=1                
            else:
                while i < j and height[j]<=height[i]:
                    vol=max(vol, min(height[j],height[i])*(j-i))
                    j-=1                   
        return vol