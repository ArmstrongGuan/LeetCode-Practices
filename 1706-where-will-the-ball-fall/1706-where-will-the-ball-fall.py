class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m=len(grid)
        n=len(grid[0])
        result=[]
        for i in range(n):
            loci, locj=0,i
            while 0<=loci<m and 0<=locj<n:
                temp=locj+grid[loci][locj]
                if 0<=temp<n and grid[loci][locj]==grid[loci][temp]:
                    loci+=1
                    locj=temp
                else:
                    loci=m
                    locj=-1
            result.append(locj)
        return result
                        
                