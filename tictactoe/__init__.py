"""
Tic Tac Toe Library
A comprehensive Python library for creating tic-tac-toe games.
"""

from .game import TicTacToe, GameState
from .players import HumanPlayer, RandomAI, SmartAI, Player
from .interface import ConsoleInterface
from .utils import GameStats

__version__ = "1.0.0"
__author__ = "AlienFromMars-itzme"

__all__ = [
    'TicTacToe',
    'GameState',
    'HumanPlayer', 
    'RandomAI', 
    'SmartAI', 
    'Player',
    'ConsoleInterface',
    'GameStats'
]