"""
Player implementations for tic-tac-toe games.
"""

import random
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .game import TicTacToe

class Player(ABC):
    """Abstract base class for all player types."""
    
    def __init__(self, symbol: str, name: str = ""):
        """
        Initialize a player.
        
        Args:
            symbol: Player's symbol ('X' or 'O')
            name: Player's display name
        """
        self.symbol = symbol
        self.name = name or f"Player {symbol}"
    
    @abstractmethod
    def get_move(self, game: 'TicTacToe') -> int:
        """
        Get the player's next move.
        
        Args:
            game: Current game state
            
        Returns:
            int: Position to play (0-8)
        """
        pass

class HumanPlayer(Player):
    """Human player that gets input from user."""
    
    def get_move(self, game: 'TicTacToe') -> int:
        """Get move from human input."""
        while True:
            try:
                position = int(input(f"{self.name} ({self.symbol}), enter position (1-9): ")) - 1
                if game.is_valid_move(position):
                    return position
                else:
                    print("Invalid move! Try again.")
            except (ValueError, KeyboardInterrupt):
                print("Please enter a number between 1-9.")

class RandomAI(Player):
    """AI player that makes random moves."""
    
    def __init__(self, symbol: str, name: str = ""):
        super().__init__(symbol, name or f"Random AI ({symbol})")
    
    def get_move(self, game: 'TicTacToe') -> int:
        """Get a random valid move."""
        available_moves = game.get_available_moves()
        return random.choice(available_moves)

class SmartAI(Player):
    """AI player that uses minimax algorithm."""
    
    def __init__(self, symbol: str, name: str = "", difficulty: str = "hard"):
        super().__init__(symbol, name or f"Smart AI ({symbol})")
        self.difficulty = difficulty
        self.opponent_symbol = 'O' if symbol == 'X' else 'X'
    
    def get_move(self, game: 'TicTacToe') -> int:
        """Get the best move using minimax algorithm."""
        if self.difficulty == "easy":
            # Mix random and smart moves
            if random.random() < 0.3:
                return random.choice(game.get_available_moves())
        
        _, best_move = self._minimax(game.get_board_copy(), self.symbol, True)
        return best_move if best_move is not None else game.get_available_moves()[0]
    
    def _minimax(self, board: list, player: str, is_maximizing: bool) -> tuple:
        """
        Minimax algorithm implementation.
        
        Returns:
            tuple: (score, best_move)
        """
        # Check terminal states
        score = self._evaluate_board(board)
        if score != 0 or ' ' not in board:
            return score, None
        
        best_move = None
        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = player
                    current_score, _ = self._minimax(
                        board, 
                        self.opponent_symbol if player == self.symbol else self.symbol, 
                        False
                    )
                    board[i] = ' '  # Undo move
                    
                    if current_score > best_score:
                        best_score = current_score
                        best_move = i
            return best_score, best_move
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = player
                    current_score, _ = self._minimax(
                        board, 
                        self.opponent_symbol if player == self.symbol else self.symbol, 
                        True
                    )
                    board[i] = ' '  # Undo move
                    
                    if current_score < best_score:
                        best_score = current_score
                        best_move = i
            return best_score, best_move
    
    def _evaluate_board(self, board: list) -> int:
        """Evaluate the board position."""
        from .game import TicTacToe
        
        # Check all win patterns
        for pattern in TicTacToe.WIN_PATTERNS:
            if (board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != ' '):
                winner = board[pattern[0]]
                if winner == self.symbol:
                    return 10
                else:
                    return -10
        return 0  # No winner