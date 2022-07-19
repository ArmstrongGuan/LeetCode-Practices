class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m=len(isConnected)
        n=len(isConnected[0])
        count=0
        for i in range(m):
            for j in range(i,n):
                if isConnected[i][j]==1:
                    count+=1
                    isConnected[i][j]=0
                    queue=[[i,j]]
                    while queue:
                        current=queue.pop(-1)
                        k,l=current[0], current[1]
                        for t in range(k, n):
                            if isConnected[k][t]==1:
                                isConnected[k][t]=0
                                queue.append([k,t])
                        for s in range(l+1):
                            if isConnected[s][l]==1:
                                isConnected[s][l]=0
                                queue.append([s,l])
        return count