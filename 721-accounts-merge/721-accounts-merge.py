class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts.sort()
        result=[]
        name=""
        for cur in accounts:
            #print(cur, result)
            if cur[0]!=name:
                result.append(cur)
                name=cur[0]
                continue
            j=-1
            while j>=-len(result) and result[j][0]==name:
                #print("place 2", cur, j)
                if len(set(result[j][1:]).intersection(cur[1:]))>0:
                    result[j]=[name]+list(set(result[j][1:]).union(cur[1:]))
                    cur=result.pop(j)
                    j=-1
                    continue
                else:
                    j=j-1
            if j<-len(result) or result[j][0]!=name:
                result.append(cur)
                
        ret=[]
        for i in result:
            j=sorted(set(i[1:]))
            ret.append([i[0]]+j)
        return ret
                    