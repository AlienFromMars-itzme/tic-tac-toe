"""
Basic example of using the tic-tac-toe library.
"""

from tictactoe import TicTacToe, HumanPlayer, ConsoleInterface

def main():
    # Create a new game
    game = TicTacToe()
    interface = ConsoleInterface(game)
    
    # Create players
    player1 = HumanPlayer('X', "Player 1")
    player2 = HumanPlayer('O', "Player 2")
    
    # Play the game
    interface.play_game(player1, player2)

if __name__ == "__main__":
    main()