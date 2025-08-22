"""
Example showing how to create custom player implementations.

This example demonstrates:
1. Creating a custom AI with specific strategy
2. Using GameState enum for game logic
3. Implementing different player behaviors
4. Testing custom players against built-in ones
"""

from tictactoe import TicTacToe, Player, SmartAI, ConsoleInterface, GameStats, GameState

class CornerFirstAI(Player):
    """AI that prefers corners, then center, then edges."""
    
    def __init__(self, symbol: str, name: str = ""):
        super().__init__(symbol, name or f"Corner AI ({symbol})")
    
    def get_move(self, game: 'TicTacToe') -> int:
        """Get move prioritizing corners, then center, then edges."""
        available_moves = game.get_available_moves()
        
        # Priority order: corners -> center -> edges
        corners = [0, 2, 6, 8]
        center = [4]
        edges = [1, 3, 5, 7]
        
        # Try corners first
        for pos in corners:
            if pos in available_moves:
                return pos
        
        # Then center
        for pos in center:
            if pos in available_moves:
                return pos
                
        # Finally edges
        for pos in edges:
            if pos in available_moves:
                return pos
        
        # Fallback (shouldn't happen)
        return available_moves[0]

class DefensiveAI(Player):
    """AI that focuses on blocking opponent wins."""
    
    def __init__(self, symbol: str, name: str = ""):
        super().__init__(symbol, name or f"Defensive AI ({symbol})")
        self.opponent_symbol = 'O' if symbol == 'X' else 'X'
    
    def get_move(self, game: 'TicTacToe') -> int:
        """Get move that blocks opponent or makes winning move."""
        board = game.get_board_copy()
        available_moves = game.get_available_moves()
        
        # First, check if we can win
        for move in available_moves:
            board[move] = self.symbol
            if self._check_winner(board, self.symbol):
                return move
            board[move] = ' '  # Undo
        
        # Then, check if we need to block opponent
        for move in available_moves:
            board[move] = self.opponent_symbol
            if self._check_winner(board, self.opponent_symbol):
                return move
            board[move] = ' '  # Undo
        
        # Otherwise, take center or corner
        preferences = [4, 0, 2, 6, 8, 1, 3, 5, 7]
        for pos in preferences:
            if pos in available_moves:
                return pos
        
        return available_moves[0]
    
    def _check_winner(self, board: list, symbol: str) -> bool:
        """Check if the given symbol has won."""
        for pattern in TicTacToe.WIN_PATTERNS:
            if all(board[pos] == symbol for pos in pattern):
                return True
        return False

class PatternAI(Player):
    """AI that tries to create specific patterns."""
    
    def __init__(self, symbol: str, name: str = ""):
        super().__init__(symbol, name or f"Pattern AI ({symbol})")
    
    def get_move(self, game: 'TicTacToe') -> int:
        """Get move following a specific opening pattern."""
        board = game.get_board_copy()
        available_moves = game.get_available_moves()
        moves_made = 9 - len(available_moves)
        
        # Opening strategy based on move count
        if moves_made == 0:  # First move
            return 4  # Take center
        elif moves_made == 2:  # Second move (after opponent)
            # If opponent took center, take corner
            if board[4] != ' ':
                for corner in [0, 2, 6, 8]:
                    if corner in available_moves:
                        return corner
            else:
                if 4 in available_moves:
                    return 4  # Take center if available
        
        # Use defensive strategy for later moves
        return self._get_defensive_move(game)
    
    def _get_defensive_move(self, game: 'TicTacToe') -> int:
        """Get a defensive move (simplified)."""
        available_moves = game.get_available_moves()
        
        if not available_moves:
            return 0  # Should not happen in valid game
        
        # Simple preference: corners, then center, then edges
        for pos in [0, 2, 6, 8, 4, 1, 3, 5, 7]:
            if pos in available_moves:
                return pos
        
        return available_moves[0]

def demonstrate_custom_players():
    """Demonstrate different custom players."""
    print("🎯 Custom Player Demonstration\n")
    
    # Test each custom player against SmartAI
    custom_players = [
        CornerFirstAI('X'),
        DefensiveAI('X'), 
        PatternAI('X')
    ]
    
    opponent = SmartAI('O', "Smart AI")
    stats = GameStats()
    
    for custom_player in custom_players:
        print(f"\n--- Testing {custom_player.name} vs {opponent.name} ---")
        
        # Play 5 games
        for i in range(5):
            game = TicTacToe()
            players = {'X': custom_player, 'O': opponent}
            
            while not game.is_game_over():
                current_player = players[game.current_player]
                move = current_player.get_move(game)
                game.make_move(move)
            
            # Record result
            stats.record_game(game.game_state, game.moves_count)
            
            # Show result
            if game.game_state == GameState.X_WINS:
                print(f"  Game {i+1}: {custom_player.name} wins!")
            elif game.game_state == GameState.O_WINS:
                print(f"  Game {i+1}: {opponent.name} wins!")
            else:
                print(f"  Game {i+1}: Draw!")
        
        print()
    
    # Show overall statistics
    stats.print_stats()

def interactive_custom_game():
    """Let user play against a custom AI."""
    from tictactoe import HumanPlayer
    
    print("\n🎮 Play Against Custom AI!")
    print("Choose your opponent:")
    print("1. Corner-First AI (prefers corners)")
    print("2. Defensive AI (blocks your moves)")
    print("3. Pattern AI (follows opening patterns)")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    custom_ais = {
        '1': CornerFirstAI('O', "Corner-First AI"),
        '2': DefensiveAI('O', "Defensive AI"),
        '3': PatternAI('O', "Pattern AI")
    }
    
    if choice in custom_ais:
        game = TicTacToe()
        interface = ConsoleInterface(game)
        
        human = HumanPlayer('X', "Human Player")
        ai = custom_ais[choice]
        
        print(f"\nYou are playing against {ai.name}!")
        interface.play_game(human, ai)
    else:
        print("Invalid choice!")

def main():
    """Main function demonstrating custom players."""
    print("🚀 Custom Player Examples for Tic-Tac-Toe Library")
    print("=" * 50)
    
    print("\nThis example shows how to create custom player classes by:")
    print("- Inheriting from the Player base class")
    print("- Implementing the get_move() method")
    print("- Using game state information for decision making")
    print("- Accessing board state and available moves")
    
    # Demonstrate different strategies
    demonstrate_custom_players()
    
    # Interactive game option
    play_interactive = input("\nWould you like to play against a custom AI? (y/n): ").lower()
    if play_interactive.startswith('y'):
        interactive_custom_game()
    
    print("\n✨ Custom player examples completed!")
    print("\nTo create your own custom player:")
    print("1. Inherit from the Player class")
    print("2. Implement the get_move(game) method")
    print("3. Return a valid position (0-8)")
    print("4. Use game.get_available_moves() and game.get_board_copy()")

if __name__ == "__main__":
    main()