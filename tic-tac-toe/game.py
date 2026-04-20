from utils import check_win, check_draw

class TicTacToe:
    def __init__(self):
        self.board = [[0 for i in range(3)] for _ in range(3)]
        self.cur = 1    #inicialize as player 1

    def print_board(self):
        print("\nCurrent Board:")
        s = {0:" ",1:"X",2:"O"}   #visula symbols
        for i in range(3):
            row = self.board[i]
            print(f" {s[row[0]]} | {s[row[1]]} | {s[row[2]]} ")
            if i<2: print("---+---+---")
        print()
    
    def get_move(self):
        while True:
            try:
                row, col= map(int, input(f"Player {self.cur}, enter a pair row col (0-2): ").strip().split())
                if row<0 or row>2 or col<0 or col>2:
                    print("Row and Collumn must be 0, 1 or 2!")
                    continue
                if self.board[row][col]!=0:
                    print("Place already taken")
                    continue
                return row, col
            except ValueError:
                print("Please enter valid numbers in the following structure:\n1 2\nRepresenting row=1 and col=2")
    
    def make_move(self, row, col): self.board[row][col] = self.cur

    def check_win(self, player): return check_win(self.board, player)
    
    def check_draw(self): return check_draw(self.board)
    
    def switch(self): self.cur = 3 - self.cur