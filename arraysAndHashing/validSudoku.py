def isValidSudoku(self, board):

    #check rows
    for i in range(0,9):
        seen_row_set = set()
        for j in range(0,9):
            if board[i][j] == ".":
                continue
            if board[i][j] in seen_row_set:
                return False
            seen_row_set.add(board[i][j])
    
    #check columns
    for i in range(0,9):
        seen_column_set = set()
        for j in range(0,9):
            if board[j][i] == ".":
                continue
            if board[j][i] in seen_column_set:
                return False
            seen_column_set.add(board[j][i])
    
    #check boxes
    #using //
    # rows: 1,2,3,4,5,6,7,8,9
    # rows//3 : 0,0,0,1,1,1,2,2,2

    boxes = {}
    for i in range (0,9):
        for j in range (0,9):
            box_key = (i //3, j //3)
            if box_key not in boxes:
                boxes[box_key] = set()
            if board[i][j] == ".":
                continue
            if board[i][j] in boxes[box_key]:
                return False
            boxes[box_key].add(board[i][j])

    return True
            
            


    

