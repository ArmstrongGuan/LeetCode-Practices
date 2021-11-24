class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if target==nums[0]:
                return(0)
            else:
                return(-1)
        head=nums[0]
        tail=nums[-1]
        map={}
        if head<tail:
            if target >= head:
                for i in range(len(nums)):
                    map[nums[i]]=i
                    print(map)
                    if target in map:
                        return(map[target])
        if head>tail:
            if target >= head:
                for i in range(len(nums)):
                    map[nums[i]]=i
                    if target in map:
                        return(map[target])
                    if nums[i+1]< nums[i]:
                        return(-1)
            elif target <= tail:
                for i in range(len(nums)-1, 0, -1):
                    map[nums[i]]=i
                    if target in map:
                        return(map[target])
                    if nums[i-1]> nums[i]:
                        return(-1)
            else:
                return(-1)
        return(-1)
                        
        
                        