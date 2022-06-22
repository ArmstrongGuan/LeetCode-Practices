class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalgas=0
        totalcost=0
        current=0
        minimal=10**4
        minimalloc=0
        for i in range(len(gas)):
            totalgas+=gas[i]
            totalcost+=cost[i]
            current=current+gas[i]-cost[i]
            if current<minimal:
                minimal=current
                minimalloc=(i+1) % len(gas)
        if totalcost>totalgas:
            return -1
        else:
            return minimalloc
            
            