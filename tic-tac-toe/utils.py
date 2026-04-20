def check_win(board, player):
    #row win
    for row in board:
        if all(cell == player for cell in row): return True
    #col win
    for col in range(3):
        if all(board[row][col]==player for row in range(3)): return True
    #diagonal win
    if all(board[i][i]==player for i in range(3)): return True
    if all(board[i][3-i-1]==player for i in range(3)): return True
    #no win yet
    return False

def check_draw(board):
    for row in board:
        #check in all line if there's a empty space or not
        if 0 in row: return False
    return True