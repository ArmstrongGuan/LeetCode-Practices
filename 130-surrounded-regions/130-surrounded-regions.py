class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def paintneighbor(board, i, j, stack):
            stack.append([i,j])
            if i+1<m and board[i+1][j]=="O" and [i+1,j] not in stack:
                stack=paintneighbor(board, i+1, j, stack)
            if i>0 and board[i-1][j]=="O" and [i-1,j] not in stack:
                stack=paintneighbor(board, i-1, j, stack)
            if j+1<n and board[i][j+1]=="O" and [i,j+1] not in stack:
                stack=paintneighbor(board, i, j+1, stack)
            if j>0 and board[i][j-1]=="O" and [i,j-1] not in stack:
                stack=paintneighbor(board, i, j-1, stack)
            return stack
         

        m=len(board)
        n=len(board[0])
        stack=[]
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=="O" and [i,j] not in stack:
                    stack=paintneighbor(board, i, j, stack)
        
        for i in range(m):
            for j in range(n):
                if [i,j] not in stack and board[i][j]=="O":
                    board[i][j]="X"
        return board
                    
        