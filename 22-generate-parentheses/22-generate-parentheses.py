class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return['()']
        output=[]
        for i in range(2**(2*n-2)):
            a=[]
            l=1
            r=0
            p=i
            good=1
            for j in range(2*n-3,-1,-1):
                a += [p // 2**j]
                p = p % 2**j
                #print([p,i,j])
                #print(a)
                if a[-1]==0:
                    r=r+1
                else:
                    l=l+1
                #print([l,r])
                if l<r or l>n:
                    good=0
                    break
            if good==1:
                print(a)
                temp='('
                for k in range(2*n-2):
                    if a[k]==1:
                        temp += '('
                    else:
                        temp += ')'
                output+=[temp+')']
        return(output)
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # map=[]
        # for i in range(n):
        #     map+=[[i,'(']]
        # for i in range(n):
        #     map+=[[i,')']]
        # def gp(map,n):
        #     tostr=''
        #     for i in range(2*n):
        #         tostr=tostr + map[i][1]
        #     output=[tostr]
        #     for i in range(2*n):
        #         #tostr1=''
        #         #for j in range(2*n):
        #         #    tostr1=tostr1 + map[j][1]
        #         #print(tostr1)
        #         #print(i)
        #         if map[i][1]==')' and map[i-1][1]=='(' and map[i-1][0]>map[i][0]:
        #             #print(True)
        #             temp=map.copy()
        #             temp[i], temp[i-1]=map[i-1], map[i]
        #             output= output+gp(temp, n) #still need to kill the same ones
        #     return output
        # return gp(map, n)