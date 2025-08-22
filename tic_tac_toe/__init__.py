"""
Tic Tac Toe Library

A comprehensive Python library for creating tic-tac-toe games.
Supports human vs human, human vs AI, and AI vs AI gameplay.
"""

from .board import Board
from .players import HumanPlayer, AIPlayer
from .game import Game
from .ai import TicTacToeAI

__version__ = "1.0.0"
__author__ = "AlienFromMars-itzme"

__all__ = [
    "Board",
    "HumanPlayer", 
    "AIPlayer",
    "Game",
    "TicTacToeAI"
]