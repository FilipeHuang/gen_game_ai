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

    def check_win(self, player):
        #row win
        for row in self.board:
            if all(cell == player for cell in row): return True
        #col win
        for col in range(3):
            if all(self.board[row][col]==player for row in range(3)): return True
        #diagonal win
        if all(self.board[i][i]==player for i in range(3)): return True
        if all(self.board[i][3-i-1]==player for i in range(3)): return True
        #no win yet
        return False
    
    def check_draw(self):
        for row in self.board:
            #check in all line if there's a empty space or not
            if 0 in row: return False
        return True
    
    def switch(self):
        self.cur = 3 - self.cur
    
    def play(self):
        print("Tic Tac Toe - Player 1 = X and Player 2 = O")
        print("Enter moves as: row column (from 0 to 2)\n")
        while True:
            self.print_board()
            row,col = self.get_move()
            self.make_move(row,col)
            if self.check_win(self.cur):
                self.print_board()
                print(f"Player {self.cur} WINS!")
                break
            if self.check_draw():
                self.print_board()
                print("DRAW")
                break
            self.switch()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()