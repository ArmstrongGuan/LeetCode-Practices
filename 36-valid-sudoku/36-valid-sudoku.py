class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={}
        column={}
        group={}
        for i in range(9):
            for j in range(9):
                #print(board[i][j])
                if board[i][j]=='.': continue
                #print([i,j])
                r=int(board[i][j])*10 + i
                c=int(board[i][j])*10+ j
                g=int(board[i][j])*10+ 3*(i//3) + (j//3)
                #print([r,c,g])                
                if r in row or c in column or g in group:
                    return(False)
                else:
                    row[r]=i
                    column[c]=j
                    group[g] = 3*i+j
                    #print(row)
                    #print(group)
        return(True)
    
    
    #or ([board[i][j], j] in column) or ([board[i][j], 3i+j] in group)