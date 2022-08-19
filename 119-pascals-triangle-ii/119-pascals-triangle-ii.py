class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[1]
        n=rowIndex
        k=1
        a=1
        while n>0:
            a=a*n//k
            result.append(a)
            n-=1
            k+=1
        return result