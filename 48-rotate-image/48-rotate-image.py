class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def place(i,j,n):
            return(j, n-1-i)
        n=len(matrix)
        for i in range(n//2):
            for j in range(i,n-1-i):               
                row1, column1= place(i,j, n)
                row2, column2= place(row1, column1, n)
                row3, column3= place(row2, column2, n)
                matrix[i][j], matrix[row1][column1], matrix[row2][column2], matrix[row3][column3] = matrix[row3][column3], matrix[i][j], matrix[row1][column1], matrix[row2][column2]
    