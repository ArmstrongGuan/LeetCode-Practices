class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def map(m,n, a ,control):
            if control==0:
                return(n-1-a)
            if control==1:
                return(m-1-a)
            return(a)
        m = len(matrix)
        n = len(matrix[0])
        output=[]
        a, b=0,1
        i,j=0,0
        count=[0,0,0,1] #r,d,l,u
        bound=[m-1,n-1,0,0]
        control=0        
        while 1:
            while (j,i)[control%2]!=map(m,n,count[control%4], control%4):
                output.append(matrix[i][j])
                i,j=i+a,j+b
            if ((j,i)[control%2])==map(m,n,count[control%4], control%4):
                output.append(matrix[i][j])
                a,b=b,-a
                count[control%4]+=1
                control+=1   
            if (j,i)[control%2]==map(m,n,count[control%4], control%4):
                break
            else:
                i,j=i+a,j+b
        return(output)
                
            
        