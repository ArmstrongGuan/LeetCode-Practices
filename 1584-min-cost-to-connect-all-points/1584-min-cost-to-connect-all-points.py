class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dp=[]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if i==j:
                    continue
                dp.append([abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), i, j])
        dp.sort()
        #print(dp)
        harshmap={}
        i=0
        count2=0
        result=0
        while count2<len(points)-1:            
            u=dp.pop(0)
            if (u[1] not in harshmap) or (u[2] not in harshmap):
                if (u[1] not in harshmap) and (u[2] not in harshmap):
                    harshmap[u[1]]=harshmap[u[2]]=i
                    i=i+1
                elif u[1] not in harshmap:
                    harshmap[u[1]]=harshmap[u[2]]
                else:
                    harshmap[u[2]]=harshmap[u[1]]
                result+=u[0]
                count2+=1
            elif harshmap[u[1]]!=harshmap[u[2]]:  
                b=harshmap[u[2]]
                for j in harshmap:
                    if harshmap[j]==b:
                        harshmap[j]=harshmap[u[1]]
                result+=u[0]
                count2+=1
            else:
                continue
        return result
                
        