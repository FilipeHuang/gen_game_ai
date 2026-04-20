from game import TicTacToe
from ai_players import get_best_move

def main():
    print("Tic Tac Toe with MiniMax and Alpha-Beta Pruning")
    print("="*47)
    print("Choose one mode:\n")
    print("- 1) Human vs Human")
    print("- 2) Human vs AI")
    print("- 3) AI vs Human")
    print("- 4) AI vs AI")
    mode = int(input("\nEnter 1, 2, 3 or 4: "))
    p1_ai = p2_ai = False
    p1_pruning = False
    p2_pruning = False
    match mode:
        case 1: p1_ai = p2_ai = False
        case 2:
            p1_ai = False
            p2_ai = True
            p2_pruning = input("\nUse Alpha-Beta Pruning for the AI? (y/n): ").strip().lower() == 'y'
        case 3: 
            p1_ai = True
            p2_ai = False
            p1_pruning = input("\nUse Alpha-Beta Pruning for the AI? (y/n): ").strip().lower() == 'y'
        case 4: 
            p1_ai = p2_ai = True
            print("\nAI Settings:")
            p1_pruning = input("Player 1 (X) - Use Alpha-Beta Pruning? (y/n): ").strip().lower() == 'y'
            p2_pruning = input("Player 2 (O) - Use Alpha-Beta Pruning? (y/n): ").strip().lower() == 'y'
        case _: print("Invalid number")
    
    game = TicTacToe()
    while True:
        game.print_board()
        is_ai_turn = (game.cur==1 and p1_ai) or (game.cur==2 and p2_ai)
        if is_ai_turn:
            pruning = p1_pruning if game.cur == 1 else p2_pruning
            print(f"AI (Player {game.cur})thinking...")
            row, col = get_best_move(game.board, game.cur,pruning)
            game.make_move(row, col)
        else:
            row, col = game.get_move()
            game.make_move(row, col)
        if game.check_win(game.cur):
            game.print_board()
            print(f"Player {game.cur} WINS!")
            break
        if game.check_draw():
            game.print_board()
            print("DRAW")
            break
        game.switch()
if __name__ == "__main__": main()