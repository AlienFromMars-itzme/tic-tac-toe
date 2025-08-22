"""
Utility functions and classes for tic-tac-toe games.
"""

from typing import Dict, List
from collections import defaultdict
from .game import GameState

class GameStats:
    """Track game statistics across multiple games."""
    
    def __init__(self):
        """Initialize game statistics."""
        self.games_played = 0
        self.wins = defaultdict(int)
        self.draws = 0
        self.total_moves = 0
    
    def record_game(self, game_state: GameState, total_moves: int):
        """
        Record the result of a game.
        
        Args:
            game_state: Final state of the game
            total_moves: Total number of moves in the game
        """
        self.games_played += 1
        self.total_moves += total_moves
        
        if game_state == GameState.X_WINS:
            self.wins['X'] += 1
        elif game_state == GameState.O_WINS:
            self.wins['O'] += 1
        elif game_state == GameState.DRAW:
            self.draws += 1
    
    def get_stats(self) -> Dict:
        """Get current statistics."""
        return {
            'games_played': self.games_played,
            'x_wins': self.wins['X'],
            'o_wins': self.wins['O'],
            'draws': self.draws,
            'average_moves': round(self.total_moves / max(1, self.games_played), 1)
        }
    
    def print_stats(self):
        """Print formatted statistics."""
        stats = self.get_stats()
        print("\n📊 Game Statistics:")
        print(f"Games played: {stats['games_played']}")
        print(f"X wins: {stats['x_wins']}")
        print(f"O wins: {stats['o_wins']}")
        print(f"Draws: {stats['draws']}")
        print(f"Average moves per game: {stats['average_moves']}")
    
    def reset(self):
        """Reset all statistics."""
        self.games_played = 0
        self.wins.clear()
        self.draws = 0
        self.total_moves = 0

def analyze_board(board: List[str]) -> Dict:
    """
    Analyze a board position.
    
    Args:
        board: Current board state
        
    Returns:
        Dict with analysis results
    """
    analysis = {
        'empty_spaces': board.count(' '),
        'x_count': board.count('X'),
        'o_count': board.count('O'),
        'center_occupied': board[4] != ' ',
        'corners_occupied': sum(1 for i in [0, 2, 6, 8] if board[i] != ' '),
        'edges_occupied': sum(1 for i in [1, 3, 5, 7] if board[i] != ' ')
    }
    
    return analysis

def get_board_hash(board: List[str]) -> str:
    """
    Get a hash representation of the board for caching.
    
    Args:
        board: Current board state
        
    Returns:
        String hash of the board
    """
    return ''.join(board)