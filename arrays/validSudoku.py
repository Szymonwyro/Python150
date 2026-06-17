def isValidSudoku(self, board):
    #check rows
    for i in range(0,9):
        seen_row_set = set()
        for j in range(0,9):
            if board[i][j] in seen_row_set:
                return False
            seen_row_set.add(board[i][j])
    

