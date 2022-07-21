class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n=len(candidates)
        result=[]
        
        
        
        def recur(candidates, start, goal):
            if goal==0:
                return [[]]
            u=candidates[start]
            if start==n-1:
                return [[u]*(goal//u)] if goal%u==0 else []
            if goal<candidates[start]:
                return []
            return [[u]+x for x in recur(candidates, start, goal-u)]+recur(candidates, start+1, goal)
        
        return recur(candidates, 0, target)
            
                
            