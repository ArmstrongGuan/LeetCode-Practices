class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        if n==1:
            return 1
        
        queue=[[0,0]]
        grid[0][0]=-1
        
        while queue:
            u=queue.pop(0)
            i,j=u[0], u[1]
            for k in range(max(i-1, 0), min(n, i+2)):
                for l in range(max(j-1, 0), min(n, j+2)):
                    if (k,l)==(n-1, n-1):
                        return 1-grid[i][j]
                    if k==i and l==j:
                        continue                       
                    if grid[k][l]==0:
                        grid[k][l]=grid[i][j]-1                        
                        queue.append([k,l])
        return -1
                