class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high=0, len(matrix)-1
        while low<high:
            mid=(low+high)//2
            if matrix[mid][0]<=target:
                if matrix[mid][-1]>=target:
                    low=mid
                    break
                else:
                    low=mid+1
            else:
                high=mid-1
        
        i=low
        low, high=0, len(matrix[0])-1
        while low<high:
            mid=(low+high)//2
            if matrix[i][mid]==target:
                return True
            if matrix[i][mid]>target:
                high=mid-1
            else:
                low=mid+1
        if matrix[i][low]==target:
            return True
        else:
            return False