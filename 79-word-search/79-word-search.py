class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #recursive solution: find the first letter, replace it by 0 and solve the question with remaining board and remining string 
        def findnext(board, word, current):
            m = len(board)
            n = len(board[0])
            if current==[]:
                for i in range(m):
                    for j in range(n):
                        if board[i][j]==word[0]:
                            if findnext(board, word[1:], current+[[i,j]])== True:
                                return True
            elif word=="":
                return True
            else:
                k=current[-1][0]
                l=current[-1][1]
                if k >=1 and board[k-1][l]==word[0] and [k-1, l] not in current:                
                    if findnext(board, word[1:], current+[[k-1,l]])== True:
                        return True
                if k <=m-2 and board[k+1][l]==word[0] and [k+1, l] not in current:
                    if findnext(board, word[1:], current+[[k+1,l]])== True:
                        return True
                if l >=1 and board[k][l-1]==word[0] and [k, l-1] not in current:
                    if findnext(board, word[1:], current+[[k,l-1]])== True:
                        return True
                if l <=n-2 and board[k][l+1]==word[0] and [k, l+1] not in current:
                    if findnext(board, word[1:], current+[[k,l+1]])== True:
                        return True
            return False
        return findnext(board, word, [])
            
                