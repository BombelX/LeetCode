class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            tab = [False]*10
            tab2 = [False]*10
            for j in range(9):
                if board[i][j] == ".":
                    pass
                elif tab[int(board[i][j])] == True:
                    return False
                else:
                    tab[int(board[i][j])] = True 
                if board[j][i] == ".":
                    continue
                if tab2[int(board[j][i])] == True:
                    return False
                else:
                    tab2[int(board[j][i])] = True 
        for i in range(0,9,3):
            for j in range(0,9,3):
                tab3 = [False]*10
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] == ".":
                            continue
                        if tab3[int(board[i+x][j+y])] == True:
                            return False
                        else:
                            tab3[int(board[i+x][j+y])] = True
        return True
            
