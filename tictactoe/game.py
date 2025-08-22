"""
Core tic-tac-toe game logic.
"""

from typing import List, Optional, Tuple, Union
from enum import Enum

class GameState(Enum):
    """Represents the current state of the game."""
    ONGOING = "ongoing"
    X_WINS = "x_wins"
    O_WINS = "o_wins"
    DRAW = "draw"

class TicTacToe:
    """
    Core tic-tac-toe game class that manages game state and logic.
    """
    
    WIN_PATTERNS = [
        # Rows
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Columns
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonals
        [0, 4, 8], [2, 4, 6]
    ]
    
    def __init__(self):
        """Initialize a new tic-tac-toe game."""
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_state = GameState.ONGOING
        self.moves_count = 0
        self.winner = None
        self.winning_pattern = None
    
    def reset(self):
        """Reset the game to initial state."""
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_state = GameState.ONGOING
        self.moves_count = 0
        self.winner = None
        self.winning_pattern = None
    
    def make_move(self, position: int) -> bool:
        """
        Make a move at the specified position.
        
        Args:
            position: Board position (0-8)
            
        Returns:
            bool: True if move was successful, False otherwise
        """
        if not self.is_valid_move(position):
            return False
        
        self.board[position] = self.current_player
        self.moves_count += 1
        
        # Check for win or draw
        self._update_game_state()
        
        # Switch player if game is still ongoing
        if self.game_state == GameState.ONGOING:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        return True
    
    def is_valid_move(self, position: int) -> bool:
        """
        Check if a move is valid.
        
        Args:
            position: Board position (0-8)
            
        Returns:
            bool: True if move is valid, False otherwise
        """
        return (
            0 <= position <= 8 and 
            self.board[position] == ' ' and 
            self.game_state == GameState.ONGOING
        )
    
    def get_available_moves(self) -> List[int]:
        """
        Get list of available move positions.
        
        Returns:
            List[int]: Available positions
        """
        return [i for i in range(9) if self.board[i] == ' ']
    
    def _update_game_state(self):
        """Update the game state after a move."""
        # Check for win
        for pattern in self.WIN_PATTERNS:
            if (self.board[pattern[0]] == self.board[pattern[1]] == 
                self.board[pattern[2]] != ' '):
                self.winner = self.board[pattern[0]]
                self.winning_pattern = pattern
                self.game_state = (GameState.X_WINS if self.winner == 'X' 
                                 else GameState.O_WINS)
                return
        
        # Check for draw
        if self.moves_count == 9:
            self.game_state = GameState.DRAW
    
    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.game_state != GameState.ONGOING
    
    def get_board_copy(self) -> List[str]:
        """Get a copy of the current board state."""
        return self.board.copy()
    
    def __str__(self) -> str:
        """String representation of the board."""
        board_str = ""
        for i in range(0, 9, 3):
            row = " | ".join(self.board[i:i+3])
            board_str += row + "\n"
            if i < 6:
                board_str += "---------\n"
        return board_str