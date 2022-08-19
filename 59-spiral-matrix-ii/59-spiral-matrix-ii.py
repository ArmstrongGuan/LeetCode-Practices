class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        lb, rb, ub, db=0, n-1, 0, n-1
        shift=[[0,1], [1,0], [0, -1], [-1, 0]]
        boundshift=[[1,0,0,0], [0,0,1,0], [0,-1,0,0],[0,0,0,-1]]
        count=0
        i,j=0,0
        result=[[0 for j in range(n)] for i in range(n)]
        cur=0
        while ub<=i<=db and lb<=j<=rb:
            cur=cur+1
            result[i][j]=cur
            i+=shift[count][0]
            j+=shift[count][1]
            if ub<=i<=db and lb<=j<=rb:
                continue
            else:
                #print("here")
                i-=shift[count][0]
                j-=shift[count][1]
                count=(count+1)%4
                i+=shift[count][0]
                j+=shift[count][1]
                lb+=boundshift[count][0]
                rb+=boundshift[count][1]
                ub+=boundshift[count][2]
                db+=boundshift[count][3]
                #print(i,j, lb, rb, ub, db)
        return result