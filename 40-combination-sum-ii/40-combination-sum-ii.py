class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        elements=list(set(candidates))
        multiplicity=[]
        cur=0
        for x in candidates:
            if x==cur:
                multiplicity[-1]+=1
            else:
                cur=x
                multiplicity.append(1)
        
        print(multiplicity)
        n=len(elements)
        result=[]
        
        
        
        def recur(elements, start, goal):
            if goal==0:
                return [[]]
            u=elements[start]
            if start==n-1:
                return [[u]*(goal//u)] if goal%u==0 and goal//u<=multiplicity[start] else []
            if goal<elements[start]:
                return []
            return recur(elements, start+1, goal)+ [[u]*i+x for i in range(1, multiplicity[start]+1) for x in recur(elements, start+1, goal-u*i) if u*i<=goal] 
        
        return recur(elements, 0, target)