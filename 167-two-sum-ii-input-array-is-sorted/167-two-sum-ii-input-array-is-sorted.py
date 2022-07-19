class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]>target:
                while i<j and numbers[j]==numbers[j-1]:
                    j=j-1
                j=j-1
            else:
                while i<j and numbers[i]==numbers[i+1]:
                    i=i+1
                i=i+1
        
            