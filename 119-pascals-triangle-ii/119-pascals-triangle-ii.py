class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[1]
        n=rowIndex
        k=1
        
        while n>0:
            result.append(result[-1]*n//k)
            n-=1
            k+=1
        return result