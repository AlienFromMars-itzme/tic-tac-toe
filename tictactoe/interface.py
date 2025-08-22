"""
Game interface implementations.
"""

from typing import TYPE_CHECKING
from .game import GameState

if TYPE_CHECKING:
    from .game import TicTacToe
    from .players import Player

class ConsoleInterface:
    """Console-based interface for playing tic-tac-toe."""
    
    def __init__(self, game: 'TicTacToe'):
        """
        Initialize the console interface.
        
        Args:
            game: TicTacToe game instance
        """
        self.game = game
    
    def display_board(self):
        """Display the current board state."""
        print("\nCurrent Board:")
        print("   1 | 2 | 3 ")
        print("  -----------")
        
        board = self.game.get_board_copy()
        for i in range(0, 9, 3):
            row_nums = f" {i//3 + 1} "
            row_content = " | ".join([cell if cell != ' ' else str(i + j + 1) 
                                    for j, cell in enumerate(board[i:i+3])])
            print(f"{row_nums}{row_content}")
            if i < 6:
                print("  -----------")
        print()
    
    def display_result(self):
        """Display the game result."""
        print("\n" + "="*30)
        if self.game.game_state == GameState.X_WINS:
            print(f"🎉 Player X wins!")
        elif self.game.game_state == GameState.O_WINS:
            print(f"🎉 Player O wins!")
        elif self.game.game_state == GameState.DRAW:
            print("🤝 It's a draw!")
        
        if self.game.winning_pattern:
            print(f"Winning pattern: {[p+1 for p in self.game.winning_pattern]}")
        print("="*30)
    
    def play_game(self, player_x: 'Player', player_o: 'Player'):
        """
        Play a complete game between two players.
        
        Args:
            player_x: Player using 'X' symbol
            player_o: Player using 'O' symbol
        """
        players = {'X': player_x, 'O': player_o}
        
        print(f"\n🎮 Starting new game: {player_x.name} vs {player_o.name}")
        
        while not self.game.is_game_over():
            self.display_board()
            
            current_player = players[self.game.current_player]
            print(f"\n{current_player.name}'s turn ({self.game.current_player})")
            
            try:
                move = current_player.get_move(self.game)
                if not self.game.make_move(move):
                    print("Invalid move! Try again.")
                    continue
            except KeyboardInterrupt:
                print("\n\nGame interrupted by user.")
                return
        
        self.display_board()
        self.display_result()
        
        return self.game.game_state