class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m= len(matrix)
        n= len(matrix[0]) #let m,n be the dimensions
        zerocolumns=[1]*n # to record columns with zeroes
        #print(m,n)
        for i in range(m):
            ifzero=0 # if there are zeroes in a row, 0 for no and 1 for yes
            for j in range(n):
                if matrix[i][j]==0:
                    ifzero=1
                    zerocolumns[j]=0
            if ifzero==1:
                matrix[i]=[0]*n
        for i in range(m):
            matrix[i]=[matrix[i][j]*zerocolumns[j] for j in range(n)]

                        
                    
                