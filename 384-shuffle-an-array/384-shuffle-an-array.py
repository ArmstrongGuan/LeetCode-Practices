class Solution:

    def __init__(self, nums: List[int]):
        self.permuted=nums.copy()
        self.original=nums

    def reset(self) -> List[int]:
        return self.original
        

    def shuffle(self) -> List[int]:
        aux=self.original.copy()
        
        for i in range(len(self.original)):
            #print(i, self.permuted)
            removeindex=random.randrange(len(aux))
            self.permuted[i]=aux.pop(removeindex)
        return self.permuted
            
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()