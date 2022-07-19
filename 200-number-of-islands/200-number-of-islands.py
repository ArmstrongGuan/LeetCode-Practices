class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #see 130, connected component
        #method of BFS
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    grid[i][j]="0"
                    queue=[[i,j]]
                    while queue:
                        current=queue.pop(0)
                        k,l=current[0], current[1]
                        if k-1>=0 and grid[k-1][l]=="1":
                            grid[k-1][l]="0"
                            queue.append([k-1,l])
                        if l-1>=0 and grid[k][l-1]=="1":
                            grid[k][l-1]="0"
                            queue.append([k,l-1])
                        if k+1<len(grid) and grid[k+1][l]=="1":
                            grid[k+1][l]="0"
                            queue.append([k+1,l])
                        if l+1<len(grid[0]) and grid[k][l+1]=="1":
                            grid[k][l+1]="0"
                            queue.append([k,l+1])
        return count
                        