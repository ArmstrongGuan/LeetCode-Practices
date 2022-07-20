class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        result=[]
        queue=[[0]]
        while queue:
            u=queue.pop(0)
            for x in graph[u[-1]]:
                if x==n-1:
                    result.append(u+[n-1])
                else:
                    queue.append(u+[x])
        return result