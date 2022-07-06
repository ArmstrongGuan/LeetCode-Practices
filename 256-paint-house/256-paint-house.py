class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        total=[0,0,0]
        for i in range(len(costs)):
            total[0], total[1], total[2]=costs[i][0]+min(total[1], total[2]), costs[i][1]+min(total[0], total[2]), costs[i][2]+min(total[0], total[1])
        return min(total)