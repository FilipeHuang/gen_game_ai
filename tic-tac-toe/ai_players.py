import sys
from utils import check_win, check_draw
'''MiniMax implementation'''
def minimax(board, is_max, ai, op):
    sys.setrecursionlimit(10000)    #limit the time when ai is the first player
    #terminal states
    if check_win(board,ai): return 10
    if check_win(board,op): return -10
    if check_draw(board): return 0

    if is_max:
        best = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j]==0:
                    board[i][j] = ai
                    score = minimax(board, False, ai, op)
                    board[i][j] = 0
                    best = max(score, best)
        return best
    else:
        best = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j]==0:
                    board[i][j] = op
                    score = minimax(board, True, ai, op)
                    board[i][j] = 0
                    best = min(score, best)
        return best
    
def get_best_move(board, ai, pruning=False):
    best_score = -float('inf')
    best_move = (-1, -1)
    op = 3 - ai
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = ai
                if pruning:
                    #use alpha beta cut
                    pass
                else: score = minimax(board, False, ai, op)
                board[i][j] = 0   #undo the move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move