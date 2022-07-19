class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0, len(height)-1
        left, right=height[i], height[j]
        vol=min(height[j],height[i])*(j-i)
        while i<j:
            if height[i]<=height[j]:
                while i < j and height[i]<=height[j]:                    
                    if height[i]>left:
                        vol=max(vol, min(height[j],height[i])*(j-i))
                        left=height[i]
                    i+=1
                vol=max(vol, min(height[j],height[i])*(j-i))
            else:
                while i < j and height[j]<=height[i]:
                    if height[j]>right:
                        vol=max(vol, min(height[j],height[i])*(j-i))
                        right=height[j]                    
                    j-=1   
                vol=max(vol, min(height[j],height[i])*(j-i))
        return vol