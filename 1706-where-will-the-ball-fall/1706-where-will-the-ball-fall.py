class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m=len(grid)
        n=len(grid[0])
        result=[]
        for i in range(n):
            loci, locj=0,i
            while 0<=loci<m and 0<=locj<n:
                if grid[loci][locj]==1:
                    if locj+1<n and grid[loci][locj+1]==1:
                        loci+=1
                        locj+=1
                    else:
                        break
                else:
                    if locj-1>=0 and grid[loci][locj-1]==-1:
                        loci+=1
                        locj-=1
                    else:
                        break
            if loci==m:
                result.append(locj)
            else:
                result.append(-1)
        return result
                        
                